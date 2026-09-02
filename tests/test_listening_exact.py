from html.parser import HTMLParser
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    13: ROOT / "lesson-7-challenge-1.html",
    17: ROOT / "lesson-9-challenge-1.html",
    24: ROOT / "lesson-12-challenge-1.html",
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.inputs = []

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            self.inputs.append(dict(attrs))

    def handle_data(self, data):
        self.text.append(data)


def state(number):
    html = PAGES[number].read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)
    return html, parser, re.sub(r"\s+", " ", "".join(parser.text)).strip()


def test_listening_transcripts_keep_the_supplied_wording_in_full():
    """Catches transcript summarisation or removal of consecutive source lines."""
    required = {
        13: [
            "which is where you'll probably spend most of your trip",
            "and he or she will look for me.",
            "including a short stop before we get there to pick up some more passengers",
            "which I'll tell you about",
            "All the family can enjoy a day out at Manham",
            "and especially how children studied, worked and played.",
            "before the end of the year",
            "all sorts of activities",
        ],
        17: [
            "Is that OK?", "J: Sure.", "I know it shouldn't really, but it does.",
            "Mobiles are usually sort of rectangular, aren't they?",
            "more expensive mobile phones are more difficult to use than cheaper ones.",
            "So 10 out of 10 for that.", "Well, thanks, Joe, for your comments.",
            "When the students come into the museum foyer we ask them to check in their backpacks",
            "And I think that's all I have to tell you.",
        ],
        24: [
            "Remember, you need to attend one of these sessions.",
            "the lecture room, no sorry, correct that, here in the main hall",
            "our resident reptile expert", "could I remind you",
            "Don't go any further, or you'll be in the sports hall.",
            "perhaps meet some of our own students",
            "has its source in the common", "this ancient craft has recently been reintroduced",
            "Okay, that's enough from me",
        ],
    }
    for number, fragments in required.items():
        _, _, visible = state(number)
        missing = [fragment for fragment in fragments if fragment not in visible]
        assert not missing, f"lesson {number} missing transcript text: " + " | ".join(missing)


def test_listening_forms_start_blank_and_answers_stay_inside_collapsed_key():
    expected_fields = {13: 18, 17: 23, 24: 30}
    for number, count in expected_fields.items():
        html, parser, _ = state(number)
        answer_inputs = [item for item in parser.inputs if "data-answer" in item]
        assert len(answer_inputs) == count
        assert all(not item.get("value") for item in answer_inputs)
        assert '<details class="collapse answer-key-collapse">' in html
        assert "font-safe" in html


def test_listening_transcript_is_immediately_below_each_available_audio():
    expected_audio = {13: 4, 17: 5, 24: 2}
    for number, count in expected_audio.items():
        html, _, _ = state(number)
        assert html.count("<audio") == count
        cursor = 0
        for _ in range(count):
            audio = html.find("<audio", cursor)
            card_end = html.find("</div>", audio)
            transcript = html.find("Xem transcript", audio, card_end)
            assert audio >= 0 and transcript > audio
            cursor = card_end + 6


def test_listening_pages_keep_valid_utf8_text():
    for number in PAGES:
        html, _, visible = state(number)
        assert "�" not in html and "Ã" not in visible and "áº" not in visible and "Ä‘" not in visible
        assert html == unicodedata.normalize("NFC", html)


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
