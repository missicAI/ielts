from html.parser import HTMLParser
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    12: "lesson-6-challenge-2.html",
    14: "lesson-7-challenge-2.html",
    15: "lesson-8-challenge-2.html",
    18: "lesson-9-challenge-2.html",
    20: "lesson-10-challenge-2.html",
    23: "lesson-11-challenge-2.html",
    25: "lesson-12-challenge-2.html",
}


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def state(number):
    html = (ROOT / FILES[number]).read_text(encoding="utf-8")
    parser = Text()
    parser.feed(html)
    return html, re.sub(r"\s+", " ", "".join(parser.parts)).strip()


def test_speaking_prompts_keep_the_exact_supplied_questions():
    required = {
        12: ["which city you would like to visit", "how you would travel there", "And explain why you would like to visit this city."],
        15: ["How long you have had it", "How often you have used it", "What you have used it for", "And explain why you use it so often"],
        20: ["Do you like to travel on your own or with your family?", "Do you like to travel abroad?", "Are there any special places for visiting in your country?", "Do you use any gadgets on a daily basis?", "Has the Internet made your job/studies easier?"],
        23: ["Describe a place you have visited where you can see interesting animals.", "Why you went there", "What the place looked like", "And say which animals you found particularly interesting."],
    }
    for number, fragments in required.items():
        _, visible = state(number)
        missing = [item for item in fragments if item not in visible]
        assert not missing, f"lesson {number} missing speaking text: " + " | ".join(missing)


def test_writing_lessons_use_the_supplied_content_charts_not_text_substitutes():
    expected_images = {
        14: ["assets/bai-14/vietnamese-students-chart.png"],
        25: ["assets/bai-25/australian-exports-chart.png", "assets/bai-25/france-electricity-chart.png"],
    }
    for number, images in expected_images.items():
        html, _ = state(number)
        for source in images:
            assert f'src="{source}"' in html
            assert f'<img class="content-graphic" src="{source}"' in html


def test_lesson18_keeps_all_eight_original_writing_steps():
    _, visible = state(18)
    required = [
        "B1: HV gõ trực tiếp Draft 1 vào link google docs, không copy nội dung từ các nguồn khác.",
        "HV tự viết 100%, có thể tham khảo ideas và từ vựng trong file gợi ý nhưng tuyệt đối không copy y nguyên",
        "B2: Truy cập vào link sau:", "IELTS Writing Xpert", "B3: Nhập đề bài và bài làm.",
        'B4: Vào phần "Kết quả chấm (Result)", đọc phần chấm điểm theo từng tiêu chí.',
        'B5: Vào phần "Lỗi chính tả và ngữ pháp (Grammar & Spelling Mistakes)", check các lỗi sai và cân nhắc sửa lại vào bài của chính mình.',
        'B6: Đọc "Gợi ý cải thiện (Suggestions for Improvement)" để chỉnh sửa bài làm.',
        "B7: Tự viết lại Draft 2 và highlight rõ những chỗ đã sửa so với draft 1, nộp cùng link google docs ở B1 để được GV nhận xét thêm",
        "B8: Sau khi GV nhận xét, nếu còn gì cần chỉnh sửa thì HV viết lại bản cuối cùng và lưu ý kĩ các lỗi sai để tránh mắc phải những lần sau.",
        "Hướng dẫn sử dụng IELTS Writing Xpert",
    ]
    missing = [item for item in required if item not in visible]
    assert not missing, "lesson 18 missing workflow text: " + " | ".join(missing)


def test_simple_lessons_keep_two_scroll_panels_links_and_unicode_safe_font():
    for number in FILES:
        html, visible = state(number)
        assert html.count('class="panel-body') >= 2
        assert "font-safe" in html
        assert "�" not in html and "Ã" not in visible and "áº" not in visible and "Ä‘" not in visible
        assert html == unicodedata.normalize("NFC", html)
        assert '<details class="collapse answer-key-collapse">' in html
    for number in (12, 15, 18, 23):
        html, _ = state(number)
        assert '>LINK</a>' in html


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
