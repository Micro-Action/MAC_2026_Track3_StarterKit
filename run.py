import os
import json
import base64
import re
from typing import Any, Dict, List, Set, Tuple

import cv2
from tqdm import tqdm
from openai import OpenAI

from prompts import SYSTEM_PROMPTS

# python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3.5-9B --port 8000 --trust-remote-code

MODEL = os.getenv("MODEL_NAME", "Qwen/Qwen3.5-9B")
INPUT_JSON = os.getenv("INPUT_JSON", "./datasets/MABench_v3.json")
VIDEO_DIR = os.getenv("VIDEO_DIR", "./datasets/videos")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))
TARGET_FPS = float(os.getenv("TARGET_FPS", "3"))
MAX_FRAMES = int(os.getenv("MAX_FRAMES", "8"))
JPEG_QUALITY = int(os.getenv("JPEG_QUALITY", "95"))

BACKEND = os.getenv("LLM_BACKEND", "vllm").lower()  # vllm / api / openai
BASE_URL = os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1")
API_KEY = os.getenv("OPENAI_API_KEY", "EMPTY")

OUTPUT_JSON = os.getenv("OUTPUT_JSON", f"./outputs/{MODEL}_results.json")


def get_client() -> OpenAI:
    if BACKEND == "openai":
        return OpenAI(api_key=API_KEY)
    return OpenAI(api_key=API_KEY, base_url=BASE_URL)


CLIENT = get_client()


def load_dataset(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt_records() -> List[Dict[str, str]]:
    return [
        {
            "task": task,
            "system_prompt": system_prompt,
        }
        for task, system_prompt in SYSTEM_PROMPTS.items()
    ]


def to_answer_record(result: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "qid": result.get("qid"),
        "pred_answer": result.get("pred_answer", ""),
    }


def load_existing_answers(path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        answers = data.get("answers", [])
        if not isinstance(answers, list):
            raise ValueError(f"Invalid answers format in {path}")
        return [to_answer_record(item) for item in answers if isinstance(item, dict)]

    if isinstance(data, list):
        return [to_answer_record(item) for item in data if isinstance(item, dict)]

    raise ValueError(f"Invalid results format in {path}")


def save_results(path: str, answers: List[Dict[str, Any]]) -> None:
    output_dir = os.path.dirname(path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    output = {
        "prompts": build_prompt_records(),
        "answers": answers,
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


def encode_jpeg(frame) -> str:
    ok, buf = cv2.imencode(
        ".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY]
    )
    if not ok:
        raise RuntimeError("JPEG encoding failed")
    return "data:image/jpeg;base64," + base64.b64encode(buf.tobytes()).decode("utf-8")


def sample_video_frames(video_path: str) -> List[str]:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Failed to open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    step = max(
        1,
        min(
            int(round(fps / max(TARGET_FPS, 1e-6))),
            max(1, total // max(MAX_FRAMES, 1)),
        ),
    )

    frames = []
    idx = 0
    while len(frames) < MAX_FRAMES:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ok, frame = cap.read()
        if not ok:
            break
        frames.append(encode_jpeg(frame))
        idx += step

    cap.release()

    if not frames:
        raise RuntimeError(f"No valid frames extracted: {video_path}")
    return frames


def build_messages(item: Dict[str, Any]) -> List[Dict[str, Any]]:
    video_path = os.path.join(VIDEO_DIR, f"{item['video']}.mp4")
    content = [
        {"type": "image_url", "image_url": {"url": image}}
        for image in sample_video_frames(video_path)
    ]
    content.append({"type": "text", "text": item["question"]})

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPTS.get(item["task"], ""),
        },
        {
            "role": "user",
            "content": content,
        },
    ]


def split_reasoning_and_answer(text: str) -> Tuple[str, str]:
    """
    兼容常见 reasoning 输出格式：
    1) <think>...</think>最终答案
    2) 只有普通答案
    """
    text = (text or "").strip()

    m = re.search(r"<think>(.*?)</think>\s*(.*)", text, flags=re.DOTALL)
    if m:
        reasoning = m.group(1).strip()
        answer = m.group(2).strip()
        return reasoning, answer

    return "", text


def infer_one(item: Dict[str, Any]) -> Dict[str, Any]:
    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=build_messages(item),
        max_tokens=MAX_TOKENS,
    )

    raw_text = response.choices[0].message.content or ""
    _, pred_answer = split_reasoning_and_answer(raw_text)

    return {
        "qid": item.get("qid"),
        "pred_answer": pred_answer,
    }


def main() -> None:
    dataset = load_dataset(INPUT_JSON)

    answers = load_existing_answers(OUTPUT_JSON)
    done_qids: Set[Any] = {item.get("qid") for item in answers if "qid" in item}

    for item in tqdm(dataset, desc="Processing", unit="sample"):
        if item.get("qid") in done_qids:
            continue

        try:
            answer = infer_one(item)
        except Exception as e:
            answer = {"qid": item.get("qid"), "pred_answer": ""}
            tqdm.write(f"{item.get('qid')}: {type(e).__name__}: {e}")

        answers.append(answer)
        done_qids.add(item.get("qid"))
        save_results(OUTPUT_JSON, answers)

    save_results(OUTPUT_JSON, answers)

    print(f"Saved to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
