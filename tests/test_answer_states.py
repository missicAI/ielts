from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def test_unanswered_fields_are_grey_and_checked_states_are_explicit():
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    assert ".font-safe input[data-answer]{background:#f1f3f8" in css
    assert ".font-safe input[data-answer].field-correct" in css
    assert ".font-safe input[data-answer].field-wrong" in css


def test_reference_answers_are_green_inside_click_to_open_blocks():
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    assert ".answer-key-collapse>.collapse-body>p" in css
    assert ".answer-key-collapse>.collapse-body>ol" in css
    lesson_pages = [
        ROOT / "lesson-6-challenge-1.html", ROOT / "lesson-6-challenge-2.html",
        ROOT / "lesson-7-challenge-1.html", ROOT / "lesson-7-challenge-2.html",
        ROOT / "lesson-8-challenge-2.html", ROOT / "lesson-8-challenge-1.html",
        ROOT / "lesson-9-challenge-1.html", ROOT / "lesson-9-challenge-2.html",
        ROOT / "lesson-10-challenge-1.html", ROOT / "lesson-10-challenge-2.html",
        ROOT / "break-2-challenge.html", ROOT / "lesson-11-challenge-1.html",
        ROOT / "lesson-11-challenge-2.html", ROOT / "lesson-12-challenge-1.html",
        ROOT / "lesson-12-challenge-2.html",
    ]
    for page in lesson_pages:
        html = page.read_text(encoding="utf-8")
        if "answer-key-collapse" in html:
            blocks = re.findall(r'<details\b[^>]*class="[^"]*answer-key-collapse[^"]*"[^>]*>', html)
            assert blocks
            assert all(" open" not in block for block in blocks)


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
