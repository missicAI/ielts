from pathlib import Path
from html import unescape


ROOT = Path(__file__).resolve().parents[1]

LESSONS = {
    11: ("lesson-6-challenge-1.html", "[FOUNDATION B] LESSON 6 - CHALLENGE 1"),
    12: ("lesson-6-challenge-2.html", "[FOUNDATION B] LESSON 6 - CHALLENGE 2"),
    13: ("lesson-7-challenge-1.html", "[FOUNDATION B] LESSON 7 - CHALLENGE 1"),
    14: ("lesson-7-challenge-2.html", "[FOUNDATION B] LESSON 7 - CHALLENGE 2"),
    15: ("lesson-8-challenge-2.html", "[FOUNDATION B] LESSON 8 - CHALLENGE 2"),
    16: ("lesson-8-challenge-1.html", "[FOUNDATION B] LESSON 8 - CHALLENGE 1"),
    17: ("lesson-9-challenge-1.html", "[FOUNDATION B] LESSON 9 - CHALLENGE 1"),
    18: ("lesson-9-challenge-2.html", "[FOUNDATION B] LESSON 9 - CHALLENGE 2"),
    19: ("lesson-10-challenge-1.html", "[FOUNDATION B] LESSON 10 - CHALLENGE 1"),
    20: ("lesson-10-challenge-2.html", "[FOUNDATION B] LESSON 10 - CHALLENGE 2"),
    21: ("break-2-challenge.html", "[FOUNDATION B] BREAK 2 - CHALLENGE"),
    22: ("lesson-11-challenge-1.html", "[FOUNDATION B] LESSON 11 - CHALLENGE 1"),
    23: ("lesson-11-challenge-2.html", "[FOUNDATION B] LESSON 11 - CHALLENGE 2"),
    24: ("lesson-12-challenge-1.html", "[FOUNDATION B] LESSON 12 - CHALLENGE 1"),
    25: ("lesson-12-challenge-2.html", "[FOUNDATION B] LESSON 12 - CHALLENGE 2"),
}

LINKS = {
    11: "https://drive.google.com/file/d/1ODzBYY0MRqHQXmmYeWJGivRiJSkTe6f1/view?usp=sharing",
    12: "https://docs.google.com/document/d/1MIWIhogOwHjaMXWJ6QV0mc8r-7iFU76V/edit?tab=t.0",
    15: "https://docs.google.com/document/d/1mLtCqhcyFVndpBLQcyl3kdIBbfau9bvS/edit?usp=sharing&ouid=116302764779051951830&rtpof=true&sd=true",
    16: "https://drive.google.com/file/d/19QjBsrmIL5-O4FAlVMbPiUFMzGzE1q_r/view",
    18: "https://docs.google.com/document/d/1tjZGUHP-wrRfsChFU6a6J4tG7nqh1JQ9o57IHdmIFYc/edit?usp=sharing",
    19: "https://drive.google.com/file/d/1zjsALHIKI67jjQ2MMQNOD0OlOyiAmOqh/view?usp=drive_link",
    22: "https://drive.google.com/file/d/1kPglUEj1HHAPxIFnKRhRJoMhltMFvzzM/view?usp=sharing",
    23: "https://drive.google.com/drive/folders/1vpIh3PiXrGW9MyfsFiGGrRR0hSTtwoj4?usp=sharing",
}


def read(number):
    return (ROOT / LESSONS[number][0]).read_text(encoding="utf-8")


def test_all_pages_are_linked_and_reconstructed_as_html():
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    for number, (filename, title) in LESSONS.items():
        page = ROOT / filename
        assert page.exists(), f"missing lesson {number}: {filename}"
        html = page.read_text(encoding="utf-8")
        assert title in html
        assert f"Bài số {number}" in html
        assert html.count('class="panel-body') >= 2
        assert "<img" not in html.lower(), f"lesson {number} embeds a screenshot"
        assert filename in index


def test_supplied_links_are_attached_to_visible_link_text():
    for number, url in LINKS.items():
        html = unescape(read(number))
        assert f'href="{url}"' in html
        assert ">LINK<" in html or ">Link<" in html


def test_listening_has_audio_then_transcript_for_every_supplied_track():
    expected = {13: 4, 17: 5, 24: 2}
    for number, count in expected.items():
        html = read(number)
        assert html.count("<audio") == count
        assert html.count("Xem transcript") >= count
        cursor = 0
        for _ in range(count):
            audio = html.find("<audio", cursor)
            transcript = html.find("Xem transcript", audio)
            assert audio >= 0 and transcript > audio
            cursor = transcript + 1


def test_reading_pages_have_detailed_solution_structure():
    required = ["Question", "Answer", "Loại câu hỏi", "Dịch nghĩa", "Phân tích", "Đoạn chứa thông tin", "Từ khóa paraphrase", "Giải thích chi tiết"]
    for number in (11, 16, 19, 22):
        html = read(number)
        for label in required:
            assert label in html, f"lesson {number} missing {label}"
        assert "<mark>" in html


def test_every_page_exposes_an_answer_or_reference_key():
    for number in LESSONS:
        html = read(number).lower()
        assert "đáp án" in html or "dàn ý tham khảo" in html


def test_shared_interaction_rules_are_preserved():
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    js = (ROOT / "app.js").read_text(encoding="utf-8")
    assert ".panel>.panel-body" in css and "overflow-y:auto" in css
    assert "field-correct" in js and "field-wrong" in js
    assert "mark.textContent='✓ Đúng'" in js
    assert "mark.textContent='✕ Sai'" in js
    assert "input.dataset.answer" in js
    assert "mark.textContent=input.dataset.answer" not in js


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS {len(tests)} validation groups")
