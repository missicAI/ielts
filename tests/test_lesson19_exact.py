from html.parser import HTMLParser
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "lesson-10-challenge-1.html"


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


class LessonParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


def page_state():
    html = PAGE.read_text(encoding="utf-8")
    parser = LessonParser()
    parser.feed(html)
    return html, parser, compact("".join(parser.text))


def test_lesson19_keeps_every_original_reading_paragraph():
    """Catches replacing the supplied passages with a shortened paraphrase."""
    _, _, visible = page_state()
    required_paragraphs = [
        "Each year in many countries around the world, clocks are set forward in spring and then back again in autumn in an effort to 'save' daylight hours.",
        "This practice fell out of favour, however, and the concept was renewed only when, in 1784, the American inventor Benjamin Franklin wrote a jocular article for The Journal of Paris exhorting the city's residents to make more use of daylight hours in order to reduce candle use.",
        "Over the next several decades, global use of DST was sporadic and inconsistent.",
        "Today, DST is used in some form by over 70 countries worldwide, affecting around one sixth of the world's population.",
        "In general, the benefits of DST are considerable and well documented.",
        "Many industries are supportive of DST due to the opportunities it provides for increased revenue.",
        "Some research casts doubt on the advantages of DST, however.",
        "A further health concern involves the disruption of our body clock.",
        "Finally, safety issues have arisen in parts of Latin America relating to a suspected relationship between DST and higher incidences of street crime.",
        "Isaac Newton was born on January 4, 1643, in Lincolnshire, England.",
        "Newton returned to Cambridge in 1667. He constructed the first reflecting telescope in 1668",
        "In 1684, English astronomer Edmund Halley paid a visit to the reclusive Newton.",
        "As a now influential figure, Newton opposed King James II's attempts to reinstate Catholic teachings at English Universities",
        "The death of Hooke in 1703 allowed Newton to take over as president of the Royal Society",
        "Around this time, the debate over Newton's claims to originating the field of calculus",
        "Newton was also obsessed with history and religious doctrines",
    ]
    missing = [paragraph for paragraph in required_paragraphs if paragraph not in visible]
    assert not missing, "missing original reading text: " + " | ".join(missing)


def test_lesson19_exercises_start_unanswered_and_keep_answers_collapsed():
    """Catches pre-filling the green source answers instead of rendering grey inputs."""
    html, parser, _ = page_state()
    inputs = [attrs for tag, attrs in parser.tags if tag == "input" and "data-answer" in attrs]
    assert len(inputs) >= 60, f"expected all main, keyword and vocabulary fields; found {len(inputs)}"
    assert all(not attrs.get("value") for attrs in inputs)
    assert html.count('class="answer-key-collapse') >= 2
    assert 'data-section="keyword-answer-key"' in html
    assert 'data-section="vocabulary-answer-key"' in html
    assert html.count('class="answer-reference"') >= 38


def test_lesson19_keeps_every_keyword_and_vocabulary_source_row():
    """Catches dropping rows from the two source tables."""
    _, _, visible = page_state()
    required = [
        "after work", "use less power in their homes", "better lighting", "fewer",
        "car crashes", "industries", "earn more money", "upsets", "dangerous",
        "re-setting", "loss of sleep", "inferior performance at work",
        "poorer general health", "fatigue", "Heated academic disputes",
        "crowning achievement", "Continued breakthroughs in research", "originality",
        "an exceptional mind", "created", "constitute", "Joint founder",
        "This practice fell out of favour, however, ...",
        "Over the next several decades, global use of DST was sporadic and inconsistent.",
        "In general, the benefits of DST are considerable and well-documented.",
        "With extended daylight hours, office workers coming off a 9 to 5 shift can often take part in outdoor recreational activities for an hour or two.",
        "This has other positive effects, such as reducing domestic electricity consumption as more opportunities become available to use sunlight instead of artificial lighting.",
        "A further benefit is a reduction in the overall rate of automobile accidents, as DST ensures that streets are well-lit at peak hours.",
        "Some research casts doubt on the advantages of DST",
        "Although this shift does in turn make streets safer in early mornings, the risk to pedestrians is not offset simply because fewer pedestrians use the streets at that time",
        "In 2008, a Swedish study found that heart attack rates spike in the few days following the switch to DST for summer.",
        "Tiredness may also be a factor behind the increase in road accidents in the week after DST begins.",
        "Following an education interrupted by a failed attempt to turn him into a farmer, he attended the King's School in Grantham.",
        "Newton returned home and began formulating his theories on calculus, light and color.",
        "Newton returned to Cambridge in 1667. He constructed the first reflecting telescope in 1668.",
        "the same year he was elected to the prestigious Society",
        "Through his experiments, Newton determined that white light was a composite of all the colors on the spectrum.",
        "Known for his temperamental defense of his work, Newton engaged in heated correspondence with Hooke",
        "Principia made Newton a star in intellectual circles, eventually earning him widespread acclaim as one of the most important figures in modern science.",
        "As a now influential figure, Newton opposed King James II's attempts to reinstate Catholic teachings at English Universities.",
        "Around this time, the debate over Newton's claims to originating the field of calculus, the mathematical study of change, exploded into a nasty dispute.",
        "A giant even among the brilliant minds that drove the Scientific Revolution, Newton is remembered as an extraordinary scholar, inventor and writer.",
    ]
    missing = [item for item in required if item not in visible]
    assert not missing, "missing table rows: " + " | ".join(missing)


def test_lesson19_has_complete_detailed_solutions_and_safe_unicode():
    """Catches generic/missing solution cards and broken Vietnamese encoding."""
    html, _, visible = page_state()
    assert html.count('class="solution-card"') == 20
    for label in (
        "Question", "Answer", "Loại câu hỏi", "Dịch nghĩa", "Phân tích",
        "Đoạn chứa thông tin", "Từ khóa paraphrase", "Giải thích chi tiết",
    ):
        assert label in visible
    assert "�" not in html
    assert "Ã" not in visible and "áº" not in visible and "Ä‘" not in visible
    assert html == unicodedata.normalize("NFC", html)
    work_panels = [attrs for tag, attrs in page_state()[1].tags if tag == "div" and "reading-work" in attrs.get("class", "").split()]
    assert work_panels and "font-safe" in work_panels[0].get("class", "").split()


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
