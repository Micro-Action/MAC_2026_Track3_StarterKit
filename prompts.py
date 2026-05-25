CMAC = """

"""

FMAC = """

"""

AS = """

"""

SAD = """

"""

MAD = """

"""

PPR = """

"""

VCC_LS = """

"""

LRC_LS = """

"""


SYSTEM_PROMPTS = {
    "CMAC": CMAC,      # [Multiple choice] Coarse-grained classification, 7 in 1
    "FMAC": FMAC,      # [Multiple choice] Fine-grained classification, 5 in 1
    "AS": AS,          # [Judgment] Action occurrence order judgment
    "SAD": SAD,        # [Judgment] Single-part action description judgment
    "MAD": MAD,        # [Judgment] Multi-part action description judgment
    "PPR": PPR,        # [Judgment] Spatial relation judgment between body parts
    "VCC-LS": VCC_LS,  # [Visual understanding] Describe human actions in the video
    "LRC-LS": LRC_LS,  # [Visual understanding] Reasoning for micro-action classification
}
