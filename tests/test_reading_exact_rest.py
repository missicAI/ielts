from html.parser import HTMLParser
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]


PAGES = {
    11: ROOT / "lesson-6-challenge-1.html",
    16: ROOT / "lesson-8-challenge-1.html",
    22: ROOT / "lesson-11-challenge-1.html",
}


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def page(number):
    html = PAGES[number].read_text(encoding="utf-8")
    parser = VisibleText()
    parser.feed(html)
    return html, re.sub(r"\s+", " ", "".join(parser.parts)).strip()


def test_reading_passages_are_not_shortened_in_lessons_11_16_22():
    """Catches replacing any supplied paragraph with a shortened summary."""
    required = {
        11: [
            "The reason for the division of Class E and Class A airspace stems from the type of planes operating in them.",
            "few of which can climb above 5,490m anyway",
            "since jet engines operate more efficiently at higher altitudes.",
            "No explicit permission from ATC to enter is needed",
        ],
        16: [
            "Large sample international comparisons of pupils' attainments since the 1960s have established",
            "Classrooms are large and pupils sit at single desks in rows.",
            "which gives the pupils a chance to let off steam.",
            "Pupils attend the school in their own neighbourhood, which in theory removes ranking by school.",
            "One teacher was particularly keen to introduce colour and pictures into maths textbooks",
            "No one minds mistakes or ignorance as long as you are prepared to learn from them.",
            "It seems to work, at least for 95 per cent of the school population.",
        ],
        22: [
            "Respondents to the survey noted that many of their olfactory likes and dislikes were based on emotional associations.",
            "The perception of smell, therefore, consists not only of the sensation of the odours themselves, but of the experiences and emotions associated with them.",
            "Most of the subjects would probably never have given much thought to odour as a cue for identifying family members",
            "The reason often given for the low regard in which smell is held",
            "Most of the research on smell undertaken to date has been of a physical scientific nature.",
            "Questions like these mean that interest in the psychology of smell is inevitably set to play an increasingly important role for researchers.",
            "the value that we attach to these experiences is interiorised by the members of society in a deeply personal way.",
        ],
    }
    for number, fragments in required.items():
        _, visible = page(number)
        missing = [fragment for fragment in fragments if fragment not in visible]
        assert not missing, f"lesson {number} missing source text: " + " | ".join(missing)


def test_reference_tables_are_real_unanswered_exercises_with_collapsed_keys():
    """Catches static filled keyword/vocabulary answers and dropped source rows."""
    minimum_fields = {11: 70, 16: 58, 22: 81}
    required_rows = {
        11: ["allow for sth", "motorised vehicles", "predict", "the arrival of", "out-of-town retail zones", "metropolitan", "restrictions imposed by"],
        16: ["consistent", "state school", "private sector", "in theory", "on the whole", "brought up", "struggler", "adequate", "play a part in"],
        22: ["badger", "fascinating", "odour", "fragrant", "feeble", "fundamental", "in the realm of", "essence"],
    }
    for number in PAGES:
        html, visible = page(number)
        assert html.count("data-answer=") >= minimum_fields[number]
        assert html.count('data-section="keyword-answer-key"') == 1
        assert html.count('data-section="vocabulary-answer-key"') == 1
        assert html.count('class="answer-reference"') >= 30
        for row in required_rows[number]:
            assert row in visible, f"lesson {number} missing reference row: {row}"


def test_reading_pages_use_unicode_safe_font_and_encoding():
    """Catches reintroducing mojibake or an unsafe font for Vietnamese tables."""
    for number in PAGES:
        html, visible = page(number)
        assert "font-safe" in html
        assert "�" not in html and "Ã" not in visible and "áº" not in visible and "Ä‘" not in visible
        assert html == unicodedata.normalize("NFC", html)


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
