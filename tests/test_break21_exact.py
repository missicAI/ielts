from html.parser import HTMLParser
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "break-2-challenge.html"


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.inputs = []

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            self.inputs.append(dict(attrs))

    def handle_data(self, data):
        self.parts.append(data)


def test_break21_keeps_full_theory_exercises_and_hidden_answer_key():
    """Catches shortened grammar theory, missing questions, or pre-filled answers."""
    html = PAGE.read_text(encoding="utf-8")
    parser = Parser()
    parser.feed(html)
    visible = re.sub(r"\s+", " ", "".join(parser.parts)).strip()
    required = [
        "Câu điều kiện loại 0 (Zero conditional)", "Câu điều kiện loại 1 (First conditional)",
        "Câu điều kiện loại 2 (Second conditional)", "Câu điều kiện loại 3 (Third conditional)",
        "Unless = if ... not", "Provided that", "Providing that", "CÂU BỊ ĐỘNG (PASSIVE VOICE)",
        "Present continuous", "Past continuous", "Present perfect", "Past perfect", "Modal verb",
        "Exercise 1 — Conditional form", "Exercise 2 — Relative clauses", "Exercise 3 — Active to passive",
        "Unless conservation efforts reduce habitat loss in this national park",
        "We planned our trip beforehand, but the bad weather prevented us from enjoying ourselves.",
    ]
    missing = [item for item in required if item not in visible]
    assert not missing, "missing grammar content: " + " | ".join(missing)
    answers = [item for item in parser.inputs if "data-answer" in item]
    assert len(answers) == 34
    assert all(not item.get("value") for item in answers)
    assert '<details class="collapse answer-key-collapse">' in html
    assert "font-safe" in html
    assert "�" not in html and "Ã" not in visible and "áº" not in visible and "Ä‘" not in visible
    assert html == unicodedata.normalize("NFC", html)


if __name__ == "__main__":
    test_break21_keeps_full_theory_exercises_and_hidden_answer_key()
    print("PASS test_break21_keeps_full_theory_exercises_and_hidden_answer_key")
