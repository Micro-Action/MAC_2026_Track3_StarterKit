

# Competition Evaluation and Final Scoring



## Micro-Action Descriptive Understanding (MAUE)

### Evaluation Dimensions and Scoring (0–5, integer):

#### L1 Behavioral Semantic Alignment

Focus: whether the **dominant body part** is consistent; whether the **dominant action type** matches (e.g., Head Tilting vs Nodding); whether the **lead–follow** relationship is preserved; whether the **action trend** (continuous/repetitive/single) is consistent.
Typical deductions: wrong dominant body part; micro-action confusion; missing or reversed lead–follow logic; overly generic description.

| Score | Core fulfillment conditions (all must be met)                | Acceptable omissions / error limits (exceeding causes downgrade) |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **5** | Dominant body part, dominant action type (micro-action label), lead–follow relation, and action trend (continuous/single/repetitive) all consistent with GT; no conflicting statements. | Minor phrasing differences allowed if they still uniquely map to the same micro-action category as GT. |
| **4** | Dominant body part and action type consistent; action trend consistent; may slightly simplify or omit secondary body part or lead–follow detail. | Must not contradict GT’s body part or action type; must not introduce new dominant actions. |
| **3** | Dominant body part consistent, but: (1) micro-action type approximate but not exact (e.g., *Nodding* vs “slight up-down head motion”), or (2) trend/detail deviates slightly, or (3) lead–follow missing. Overall still reflects same behavioral semantics. | Must not change dominant body part or describe multiple unrelated dominant actions. |
| **2** | Only matches at broader body-region level (e.g., both upper limbs/head) but dominant part differs or mixes multiple dominant actions; hard to map uniquely to GT. | Must not express an entirely different behavioral meaning (else lower score). |
| **1** | Only a vague sense of “moving/action occurring,” or semantically unclear; or points to irrelevant body part but still indicates a human movement. | If describing “no action” or opposite meaning, rate **0**.   |
| **0** | Completely inconsistent with GT (e.g., GT has an action but description says “no action”), or dominant part/type completely opposite. | —                                                            |

#### L2 Spatial-Topological Fidelity

Focus: left/right, up/down, front/back, close or away from body; relation to torso or midline; correctness of path (e.g., “from right to midline”).
Typical deductions: direction reversal (left↔right), level confusion (high↔low), missing or incorrect path/midline info.

| Score | Core fulfillment conditions (all must be met)                | Acceptable omissions / error limits (exceeding causes downgrade) |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **5** | Key orientations (left/right, up/down, front/back, near–far) correct; proper relation to torso/midline; correct and complete path start–end and direction (“from right to midline, then down”). | Minor wording variations allowed if orientation and path judgment unaffected. |
| **4** | Main orientation and path largely match; may omit one secondary dimension (e.g., “slightly upward” missing) or simplify details; no critical reversals. | Must not reverse key directions (left↔right, up↔down, inward↔outward). |
| **3** | Only partial spatial info correct: at least one key dimension right (e.g., left/right correct but up/down wrong/omitted); path incomplete but similar spatial framework. | One key reversal tolerated if others correct and position still interpretable; multiple reversals score lower. |
| **2** | Only coarse region info (e.g., “upper body/near face”) with vague space; lacks midline/body-relative or path direction. | Must not contain systemic contradictions (else 1).           |
| **1** | Critical spatial errors or reversals (left↔right, up↔down, front↔back) or multiple confusions breaking topological coherence. | If no spatial info at all, score 0.                          |
| **0** | No spatial/directional info; orientation or path indeterminable. | —                                                            |

#### L3 Temporal-Structural Coherence

Focus: reproduces “start–change–stabilize” phases; maintains temporal order and rhythm (continuous/intermittent/repetitive); correct lead–follow timing between parts.
Typical deductions: missing phase; reversed order; multi-stage reduced to static.

| Score | Core fulfillment conditions (all must be met)                | Acceptable omissions / error limits (exceeding causes downgrade) |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **5** | Clearly reproduces GT’s phase structure (e.g., “rise–change–steady” or “early–mid–late”); temporal order consistent; rhythm type (continuous/intermittent/repetitive) and cycle match; multi-part lead–follow consistent. | Phase boundaries may differ slightly in wording if structure and rhythm interpretation unchanged. |
| **4** | Shows clear temporal evolution and return/convergence (e.g., “then returns to neutral”); order mostly consistent; rhythm roughly matching though segmentation blurred or missing minor detail. | Must not reverse key order or misstate repetition type.      |
| **3** | Contains temporal cues (first/then/after) but lacks full segmentation or slightly mismatched rhythm/cycle; overall trend still clear. | Must not rewrite to entirely different rhythm (e.g., repetitive→single) with no return cue. |
| **2** | Multi-stage GT simplified to single/static action (e.g., only “moves up” while GT = “up→down→steady”); or missing crucial “return/stabilize.” | If order reversed, rate 1.                                   |
| **1** | Wrong temporal order (e.g., GT “extend→return” but output “return→extend”), or “start–change–steady” sequence broken into illogical order. | If no temporal expression, score 0.                          |
| **0** | No temporal dynamics: purely static or described as “no movement.” | —                                                            |

### General Judgment Rules

1. **Text-only basis**: judge strictly from visible `gt_answer` and `pred_answer`; **do not infer** unseen video details.
2. **Accept equivalence, penalize contradiction**: synonymous expressions acceptable; any **contradiction/reversal** results in downgrade.
3. **Match GT granularity**: if GT includes midline/path/phase details not covered in prediction, **reduce score accordingly**.
4. **Uncertainty → lower score**: when unsure, give a **slightly lower score**.
5. **Integer only**: each dimension must be an **integer (0–5)**.

---

## Micro-Action Reasoning and Explanation (MARE)

### Evaluation Dimensions and Scoring (0–5, integer):

#### L1 Coarse-Grained Label Accuracy

Focus on selecting the correct dominant body-part category and applying cross-part contact priority, while clarifying lead–follow and differentiating torso vs. head changes (e.g., turning around vs. turning head). 
Typical deductions: misclassifying head–hand/leg–hand as upper/lower limb, listing multiple dominant parts without hierarchy, using overgeneral phrases (“upper body moves”), or treating static posture as a dynamic action.

| Score | Core fulfillment conditions (all must be met)                | Acceptable omissions / error limits (exceeding causes downgrade) |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **5** | Dominant **major body part** matches the GT; if cross-part contact exists, correctly elevated to higher priority (e.g., head-hand, leg-hand, body-hand); identifies main–sub relationships when needed, with no contradictions. | Synonyms or hypernyms allowed as long as they can be **uniquely** mapped to the GT category. |
| **4** | Main body category correct; may omit secondary parts or not explicitly state main–sub relationships; no information contradicting GT. | Must not introduce new dominant parts; regional generalization allowed (e.g., “upper body” referring to head) but should not cause ambiguity with neighboring categories. |
| **3** | Falls within the correct body region overall but includes **parallel/mixed** descriptions making dominance unclear, or only reaches a **neighboring level** that still roughly indicates the GT. | Must not change the dominant category; should not include multiple unrelated dominant parts. |
| **2** | Only matches broad body areas (e.g., “upper limb/head” level), or mixes multiple dominant parts, making unique correspondence to GT difficult. | Must not alter the behavioral meaning (otherwise lower).     |
| **1** | Only vaguely states “a human body part moves” or points to an **irrelevant/adjacent** part but still within body movement. | If describes “no action” or contradicts GT part, score **0**. |
| **0** | Completely inconsistent with GT (e.g., GT shows movement but description says “no action”), or dominant body part entirely opposite/missing. | —                                                            |

#### L2 Fine-Grained Label Accuracy

Focus on pinpointing the exact micro-action label with trend/temporal pattern (single/continuous/repetitive), contact attribute (contact vs. non-contact), direction, and object involvement; explicitly separate common confusions (Tilt vs. Turn, Touch vs. Scratch, Stretch vs. Retract, Waving vs. Illustrative, hands-together vs. interlaced fingers). 
Typical deductions: using generic verbs only, flipping contact/direction/trend, confusing object manipulation with gestures, and mixing similar hand/foot subtypes (e.g., tiptoe vs. leg shaking).

| Score | Core fulfillment conditions (all must be met)                | Acceptable omissions / error limits (exceeding causes downgrade) |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **5** | **Micro-action label** matches the GT, and **direction/trend (single/continuous/reciprocating)** aligns with **contact attributes**; distinguishes neighboring concepts (e.g., Tilt vs. Turn, Touch vs. Scratch, Stretch vs. Retract) with no contradictions. | Minor wording differences allowed as long as it can be **uniquely** mapped to the same micro-action category. |
| **4** | Main action type is correct; trend consistent; may omit minor modifiers (amplitude/intensity/details) or secondary contact details without altering category judgment. | Must not contradict GT in action type or trend; must not introduce a new dominant action. |
| **3** | Action semantics are close but **not precise enough** (e.g., “slight up-and-down nodding” ≈ Nodding), or show minor deviation in trend/details; overall still reflects the same behavioral meaning. | Must not change the dominant body part; must not include multiple unrelated dominant actions. |
| **2** | Only provides generalized verbs (move/adjust), or **reverses contact vs. non-contact**; or mixes multiple dominant actions, making it hard to uniquely map to GT. | Must not express a completely different behavioral meaning (otherwise lower). |
| **1** | Similar to GT but **semantically opposite or reversed** (e.g., extend ↔ retract, head down ↔ look up), or very vague motion description. | If describing “no action” or contradicting GT, score **0**.  |
| **0** | Micro-action category completely wrong or missing, or explicitly states “no action” opposite to GT. | —                                                            |

#### L3 Causal Reasoning Consistency

Focus on a clear chain “observations → intermediate inference/near-neighbor exclusion → label,” citing at least 2–3 evidence elements (body part, direction/trend, contact, temporal pattern). 
Typical deductions: label-only or evidence lists with no causality, evidence that contradicts or under-supports the conclusion, missing near-neighbor exclusion, speculative motives, or muddled time windows for concurrent actions.

| Score | Core fulfillment conditions (all must be met)                | Acceptable omissions / error limits (exceeding causes downgrade) |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **5** | A clear **causal chain** is present: **observational evidence** (location/direction–trend/contact/temporal pattern ≥3 items) → **intermediate inference/exclusion of nearby possibilities** → **correct label**; fully consistent throughout. | Wording may be slightly condensed, but must include at least one explicit **exclusion of a confusing label**. |
| **4** | Causal chain is complete but more concise; evidence covers ≥2 items; may omit comparative exclusion or minor details without breaking logical integrity. | No evidence may contradict the ground truth (GT); excessive omission will lower the score. |
| **3** | Basic “observation → conclusion” structure present but transitions are loose or lack explicit causal terms; missing main–sub or contrast elements; overall still self-consistent. | Must not contradict its own description or conclusion.       |
| **2** | Mostly a list of coexisting facts (observation and label stated together) rather than causal reasoning; key evidence missing; or includes **speculative causes** not based on observation. | Any clear contradiction or reasoning leap should drop to **1** or below. |
| **1** | Analysis and label **inconsistent or disconnected**; self-contradictory or empty description such as “only moving.” | If no reasoning at all and only the label is given, score **0**. |
| **0** | No reasoning process (only reports label/score), or reasoning entirely conflicts with GT or observations. | —                                                            |

### General Judgment Rules

1. **Text-only basis**: judge strictly from visible `gt_answer` and `pred_answer`; **do not infer** unseen video details.
2. **Accept equivalence, penalize contradiction**: synonymous expressions acceptable; any **contradiction/reversal** results in downgrade.
3. **Match GT granularity**: if GT includes midline/path/phase details not covered in prediction, **reduce score accordingly**.
4. **Uncertainty → lower score**: when unsure, give a **slightly lower score**.
5. **Integer only**: each dimension must be an **integer (0–5)**.

---

## Final Scoring

The final score is computed from **12 normalized sub-scores**: 6 closed-ended accuracy metrics and 6 open-ended evaluation dimensions. The two `AVG` columns are reported only for reference and are **not directly included** in the final score.

Let

$$
\mathcal{C}=\{\mathrm{CMAR},\mathrm{FMAR},\mathrm{SAD},\mathrm{MAD},\mathrm{MAS},\mathrm{PPR}\}
$$

be the set of closed-ended tasks, and let

$$
\mathcal{O}=\{\mathrm{MADU}_{L1},\mathrm{MADU}_{L2},\mathrm{MADU}_{L3},\mathrm{MARE}_{L1},\mathrm{MARE}_{L2},\mathrm{MARE}_{L3}\}
$$

be the set of open-ended evaluation dimensions.

Each sub-score is first normalized to the range $[0,100]$:

$$
\widetilde{s}_i=
\begin{cases}
s_i, & i\in\mathcal{C},\quad s_i\text{ is reported as percentage accuracy},\\
20s_i, & i\in\mathcal{O},\quad s_i\in[0,5].
\end{cases}
$$

The final score is the average of all 12 normalized sub-scores:

$$
\mathrm{Final\ Score}=\frac{1}{12}\left(\sum_{i\in\mathcal{C}}\widetilde{s}_i+\sum_{i\in\mathcal{O}}\widetilde{s}_i\right).
$$

## [Supplemental](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Li_MA-Bench_Towards_Fine-grained_CVPR_2026_supplemental.pdf)
