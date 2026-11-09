import json
from pathlib import Path

SCORES_PATH = Path("scores.json")
EMPTY_SCORES = {"X": 0, "O": 0, "draws": 0}


def load_scores() -> dict[str, int]:
    """Read scores from disk; return zeros if the file is missing or corrupt."""
    if not SCORES_PATH.exists():
        return EMPTY_SCORES.copy()

    try:
        data = json.loads(SCORES_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return EMPTY_SCORES.copy()  # corrupt file -> start fresh

    # Merge with defaults so missing keys don't KeyError later
    result = EMPTY_SCORES.copy()
    result.update({k: v for k, v in data.items() if k in EMPTY_SCORES})
    return result


def save_scores(scores: dict[str, int]) -> None:
    """Write scores atomically (write temp, then replace)."""
    tmp = SCORES_PATH.with_suffix(".json.tmp")
    tmp.write_text(
        json.dumps(scores, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    tmp.replace(SCORES_PATH)  # atomic on POSIX and Windows


def record_win(state: str) -> dict[str, int]:
    scores = load_scores()
    scores[state] += 1
    save_scores(scores)
    return scores


def record_draw() -> dict[str, int]:
    scores = load_scores()
    scores["draws"] += 1
    save_scores(scores)
    return scores
