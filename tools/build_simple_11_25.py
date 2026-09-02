from html import escape
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def shell(number, title, skill, source, work, filename):
    html = f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title><link rel="stylesheet" href="styles.css?v=13"></head>
<body class="lesson-page"><div class="shell"><header class="topbar compact-topbar">
<a class="back" href="index.html">← Quay lại danh sách</a><div class="title-wrap"><div><div class="eyebrow">FOUNDATION B • {skill.upper()}</div><h1 class="lesson-heading">{escape(title)}</h1></div><div class="original-top-actions"><button class="original-report-btn" type="button">Báo lỗi</button><a class="original-back-btn" href="index.html">← Quay lại</a></div><span class="lesson-badge">Bài số {number}</span></div></header>
<main class="lesson-grid"><section class="panel"><h2>Đề bài</h2><div class="panel-body reading-source font-safe"><div class="section-label">{skill.upper()}</div>{source}</div></section>
<section class="panel"><h2>Bài làm</h2><div class="panel-body reading-work font-safe"><div class="banner">{skill.title()}</div>{work}</div></section></main>
<footer class="page-footer">Hai cột Đề bài / Bài làm cuộn độc lập trên máy tính.</footer></div><script src="app.js?v=12"></script></body></html>'''
    (ROOT / filename).write_text(unicodedata.normalize("NFC", html), encoding="utf-8")


def submit(number, prompt="Submit your link here:"):
    return f'''<div class="submission-card"><h3>{prompt}</h3><textarea data-count="b{number}-count" aria-label="Bài nộp số {number}"></textarea><div id="b{number}-count" class="counter">Số từ: 0</div></div>'''


shell(12, "[FOUNDATION B] LESSON 6 - CHALLENGE 2", "Speaking", '''
<div class="original-reading-heading"><span class="reading-pass-label">SPEAKING PART 2</span></div>
<h3>Describe a city you would like to visit.</h3><p>You should say:</p><ul><li>which city you would like to visit</li><li>how you would travel there</li><li>what you would do there</li></ul><p><strong>And explain why you would like to visit this city.</strong></p>
<p><strong>Suggested vocabulary:</strong> <a class="inline-link" href="https://docs.google.com/document/d/1MIWIhogOwHjaMXWJ6QV0mc8r-7iFU76V/edit?tab=t.0" target="_blank" rel="noopener">LINK</a></p>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p>Không có một đáp án cố định. Bài nói cần đủ bốn ý: tên thành phố, cách đi, hoạt động dự định và lý do cá nhân; triển khai thành một bài nói liền mạch khoảng 1–2 phút.</p></div></details>''', submit(12, "Submit your video link here:"), "lesson-6-challenge-2.html")

shell(14, "[FOUNDATION B] LESSON 7 - CHALLENGE 2", "Writing", '''
<div class="original-reading-heading"><span class="reading-pass-label">WRITING TASK 1</span></div>
<p><strong>The graph below shows the average number of Vietnamese students studying in France, Russia and America between 2000 and 2015.</strong></p>
<p>Summarise the information by selecting and reporting the main features, and make comparisons where relevant.</p>
<figure class="content-figure"><img class="content-graphic" src="assets/bai-14/vietnamese-students-chart.png" alt="Line graph of Vietnamese students studying in France, Russia and America, 2000–2015"><figcaption>Average number of Vietnamese students studying in France, Russia and America, 2000–2015.</figcaption></figure>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p><strong>Overview:</strong> America rises markedly and finishes highest; France grows then levels off; Russia falls before a slight recovery.</p><p>Body 1: compare France and Russia. Body 2: describe the sustained rise in America and its final lead.</p></div></details>''', submit(14, "Submit your essay here:"), "lesson-7-challenge-2.html")

shell(15, "[FOUNDATION B] LESSON 8 - CHALLENGE 2", "Speaking", '''
<div class="original-reading-heading"><span class="reading-pass-label">SPEAKING PART 2</span></div><h3>Describe an electronic device you use often.</h3><p>You should say:</p><ul><li>How long you have had it</li><li>How often you have used it</li><li>What you have used it for</li></ul><p><strong>And explain why you use it so often</strong></p>
<p><strong>Suggested vocabulary:</strong> <a class="inline-link" href="https://docs.google.com/document/d/1mLtCqhcyFVndpBLQcyl3kdIBbfau9bvS/edit?usp=sharing&amp;ouid=116302764779051951830&amp;rtpof=true&amp;sd=true" target="_blank" rel="noopener">LINK</a></p>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p>Giới thiệu thiết bị, thời điểm sở hữu, tần suất, 2–3 công dụng và lý do nó cần thiết trong sinh hoạt/học tập. Part 2 không có đáp án duy nhất.</p></div></details>''', submit(15, "Submit your video link here:"), "lesson-8-challenge-2.html")

shell(18, "[FOUNDATION B] LESSON 9 - CHALLENGE 2", "Writing", '''
<div class="original-reading-heading"><span class="reading-pass-label">WRITING TASK 2</span></div><p><strong>Write two body paragraphs for the following topic:</strong></p>
<blockquote>In some countries the average weight of people is increasing and their levels of health and fitness are decreasing. What do you think are the causes of these problems and what measures could be taken to solve them?</blockquote>
<p><strong><em>Suggested ideas:</em></strong> <a class="inline-link" href="https://docs.google.com/document/d/1tjZGUHP-wrRfsChFU6a6J4tG7nqh1JQ9o57IHdmIFYc/edit?usp=sharing" target="_blank" rel="noopener">LINK</a></p>
<h3 class="red-heading">Các bước làm bài Writing</h3>
<div class="writing-steps">
  <p><strong>B1:</strong> HV gõ trực tiếp Draft 1 vào link google docs, <strong>không copy nội dung từ các nguồn khác.</strong><br>(HV tự viết 100%, có thể tham khảo ideas và từ vựng trong file gợi ý nhưng tuyệt đối không copy y nguyên)</p>
  <p><strong>B2:</strong> Truy cập vào link sau:</p>
  <p><span class="inline-link">IELTS Writing Xpert</span></p>
  <p><strong>B3:</strong> Nhập đề bài và bài làm.</p>
  <p><strong>B4:</strong> Vào phần "Kết quả chấm (Result)", đọc phần chấm điểm theo từng tiêu chí.</p>
  <p><strong>B5:</strong> Vào phần "Lỗi chính tả và ngữ pháp (Grammar &amp; Spelling Mistakes)", check các lỗi sai và cân nhắc sửa lại vào bài của chính mình.</p>
  <p><strong>B6:</strong> Đọc "Gợi ý cải thiện (Suggestions for Improvement)" để chỉnh sửa bài làm.</p>
  <p><strong>B7:</strong> Tự viết lại Draft 2 và highlight rõ những chỗ đã sửa so với draft 1, nộp cùng link google docs ở B1 để được GV nhận xét thêm</p>
  <p><strong>B8:</strong> Sau khi GV nhận xét, nếu còn gì cần chỉnh sửa thì HV viết lại bản cuối cùng và lưu ý kĩ các lỗi sai để tránh mắc phải những lần sau.</p>
  <p><span class="inline-link">Hướng dẫn sử dụng IELTS Writing Xpert</span></p>
</div>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p><strong>Body 1 – Causes:</strong> calorie-dense processed food, sedentary work and entertainment, limited exercise.</p><p><strong>Body 2 – Measures:</strong> nutrition education, clearer food labels, accessible sports facilities and active-transport policies.</p></div></details>''', submit(18, "Submit your writing link here:"), "lesson-9-challenge-2.html")

shell(20, "[FOUNDATION B] LESSON 10 - CHALLENGE 2", "Speaking", '''
<div class="original-reading-heading"><span class="reading-pass-label">SPEAKING PART 1</span></div><h3>Traveling</h3><ol><li>Do you like to travel on your own or with your family?</li><li>Do you like to travel abroad?</li><li>Are there any special places for visiting in your country?</li><li>When you visit new places, what do you like to do?</li><li>In which season do you prefer to travel?</li></ol>
<h3>Technology</h3><ol><li>Do you use any gadgets on a daily basis?</li><li>How much time do you spend using a computer at work or at home?</li><li>Have you ever bought anything online?</li><li>Has the Internet made your job/studies easier?</li></ol>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p>Part 1 không có đáp án cố định. Mỗi câu nên trả lời trực tiếp, nêu lý do và thêm một ví dụ cá nhân ngắn.</p></div></details>''', submit(20, "Submit your video link here:"), "lesson-10-challenge-2.html")

shell(23, "[FOUNDATION B] LESSON 11 - CHALLENGE 2", "Speaking", '''
<div class="original-reading-heading"><span class="reading-pass-label">SPEAKING PART 2</span></div><h3>Describe a place you have visited where you can see interesting animals.</h3><p>You should say:</p><ul><li>Why you went there</li><li>What the place looked like</li><li>What you did there</li></ul><p><strong>And say which animals you found particularly interesting.</strong></p>
<p><strong>Suggested vocabulary:</strong> <a class="inline-link" href="https://drive.google.com/drive/folders/1vpIh3PiXrGW9MyfsFiGGrRR0hSTtwoj4?usp=sharing" target="_blank" rel="noopener">LINK</a></p>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p>Chọn một địa điểm cụ thể; miêu tả lý do đi, không gian, hoạt động, rồi tập trung vào một hoặc hai loài vật và lý do chúng đáng nhớ.</p></div></details>''', submit(23, "Submit your video link here:"), "lesson-11-challenge-2.html")

shell(25, "[FOUNDATION B] LESSON 12 - CHALLENGE 2", "Writing", '''
<div class="original-reading-heading"><span class="reading-pass-label">WRITING</span></div><h3>Exercise 1</h3><p>The line graph shows the percentage of Australian exports to four countries between 1990 and 2012. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.</p>
<figure class="content-figure"><img class="content-graphic" src="assets/bai-25/australian-exports-chart.png" alt="Percentage of Australian exports to Japan, the US, China and India from 1990 to 2012"><figcaption>Australian exports to Japan, the US, China and India, 1990–2012.</figcaption></figure>
<h3>Exercise 2</h3><p>The line graph shows electricity production in France measured in terawatt-hours from 1980 to 2010. Summarise the main features and compare Thermal, Nuclear, Hydroelectric and Renewables.</p>
<figure class="content-figure"><img class="content-graphic" src="assets/bai-25/france-electricity-chart.png" alt="Electricity production in France by source, in terawatt-hours, from 1980 to 2010"><figcaption>Electricity production in France from Thermal, Nuclear, Hydroelectric and Renewables, 1980–2010.</figcaption></figure>
<details class="collapse answer-key-collapse"><summary>Đáp án / dàn ý tham khảo</summary><div class="collapse-body"><p><strong>Exercise 1 overview:</strong> China rises dramatically while Japan loses share; the US and India remain much lower.</p><p><strong>Exercise 2 overview:</strong> Nuclear power becomes dominant, while the other sources remain far lower or decline.</p></div></details>''', submit(25, "Submit your link here (Exercises 1 &amp; 2):"), "lesson-12-challenge-2.html")
