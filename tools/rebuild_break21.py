from html import escape
from pathlib import Path
import unicodedata

ROOT = Path(__file__).resolve().parents[1]

def field(n, prompt, answer):
    return f'<label class="question-row"><strong>{n}.</strong><span>{prompt}</span><input type="text" data-answer="{escape(answer, quote=True)}" autocomplete="off"></label>'

def exercise(title, instruction, fields):
    return f'''<section class="exercise-block"><h3>{title}</h3><p><strong>{instruction}</strong></p><form data-reading-form>{''.join(fields)}<div class="actions"><button class="btn green" type="button" data-check-reading>Kiểm tra</button><button class="btn" type="reset" data-reset-reading>Làm lại</button></div><div class="result" data-reading-result></div></form></section>'''

source = '''
<div class="section-label">GRAMMAR</div>
<h3 class="red-heading">CÂU ĐIỀU KIỆN (CONDITIONAL)</h3>
<h4>Câu điều kiện loại 0 (Zero conditional)</h4>
<p>Diễn tả sự việc luôn đúng hoặc các thói quen nói chung.</p>
<p><strong>Công thức:</strong> If + S + V(s/es), S + V(s/es).</p>
<p><em>Example:</em> If travelers want to climb a mountain, they have to train rigorously to prepare for that type of trip.</p>
<p>Có thể đảo hai mệnh đề: Travelers have to train rigorously to prepare for a trip if they want to climb a mountain.</p>
<h4>Câu điều kiện loại 1 (First conditional)</h4>
<p>Diễn tả sự việc có khả năng xảy ra trong tương lai.</p>
<p><strong>Công thức:</strong> If + S + V/V(s/es), S + will/can/must + V.</p>
<p><em>Example:</em> If you buy a new technological device, you will get a 3-year guarantee for the product.</p>
<p><strong>Chú ý:</strong> có thể dùng <em>might, could, may</em> thay cho <em>will</em> để diễn tả khả năng thấp hơn.</p>
<h4>Câu điều kiện loại 2 (Second conditional)</h4>
<p>Diễn tả sự việc không có thật hoặc khó có thể xảy ra ở hiện tại/tương lai.</p>
<p><strong>Công thức:</strong> If + S + V-ed/P.I, S + would/could/might + V.</p>
<p><em>Example:</em> If I were you, I'd choose Da Lat as my next travel destination.</p>
<p>Với động từ <em>to be</em>, có thể dùng <strong>were</strong> cho mọi chủ ngữ. Cấu trúc <strong>were to + V</strong> nhấn mạnh tính bất khả thi: If I were to win the lottery, I would travel around the world.</p>
<h4>Câu điều kiện loại 3 (Third conditional)</h4>
<p>Diễn tả sự việc không có thật trong quá khứ.</p>
<p><strong>Công thức:</strong> If + S + had + V-ed/P.II, S + would/could/might + have + V-ed/P.II.</p>
<p><em>Example:</em> If I had stayed in New York last year, I would have found a job there long ago.</p>
<h4>Other words used as a condition</h4>
<ul><li><strong>Unless = if ... not:</strong> Unless the weather turns bad, we will continue with our hiking trip.</li><li><strong>As long as:</strong> As long as you travel before this afternoon, you will reach the destination in time.</li><li><strong>Provided that:</strong> Provided that you learn how to read the map, you will find your way out of the woods.</li><li><strong>Providing that:</strong> Providing that the car doesn't break down, the passengers will safely cross the border.</li></ul>
<h3 class="red-heading">CÂU BỊ ĐỘNG (PASSIVE VOICE)</h3>
<p>Câu bị động nhấn mạnh hành động và đối tượng chịu tác động. Có thể lược bỏ tác nhân khi chưa xác định, không quan trọng hoặc quá hiển nhiên.</p>
<p><strong>Active:</strong> S + V + O &nbsp;→&nbsp; <strong>Passive:</strong> O + be + V3/V-ed + (by + S).</p>
<p><em>Example:</em> A thief stole our wallet on our trip. → Our wallet was stolen (by a thief) on our trip.</p>
<p>Chủ ngữ và tân ngữ đổi vị trí; <strong>be</strong> được chia theo chủ ngữ mới và thì của câu chủ động.</p>
<table><thead><tr><th>Tense</th><th>Active</th><th>Passive</th><th>Example</th></tr></thead><tbody>
<tr><td>Present simple</td><td>S + V(s/es) + O</td><td>S + am/is/are + V3 + O</td><td>Someone brings up the topic. → The topic is brought up.</td></tr>
<tr><td>Past simple</td><td>S + V-ed + O</td><td>S + was/were + V3 + O</td><td>Many people chose public transport. → Public transport was chosen.</td></tr>
<tr><td>Future simple</td><td>S + will + V + O</td><td>S + will be + V3 + O</td><td>She will write an itinerary. → An itinerary will be written.</td></tr>
<tr><td>Present continuous</td><td>S + am/is/are + V-ing + O</td><td>S + am/is/are being + V3 + O</td><td>Scientists are looking into this advance. → This advance is being looked into.</td></tr>
<tr><td>Past continuous</td><td>S + was/were + V-ing + O</td><td>S + was/were being + V3 + O</td><td>She was fixing her dryer. → Her dryer was being fixed.</td></tr>
<tr><td>Present perfect</td><td>S + have/has + V3 + O</td><td>S + have/has been + V3 + O</td><td>A police officer has stopped our car. → Our car has been stopped.</td></tr>
<tr><td>Past perfect</td><td>S + had + V3 + O</td><td>S + had been + V3 + O</td><td>A thief had broken into our house. → Our house had been broken into.</td></tr>
</tbody></table>
<p><strong>Modal verb:</strong> can/could/may/might/should + V → can/could/may/might/should + be + past participle.</p>
<p><em>Example:</em> You should write down important items before packing. → Important items should be written down before you pack.</p>
<h4>Notes</h4><ul><li>Có thể lược bỏ tác nhân là đại từ: He has brought me a first-aid kit. → I have been brought a first-aid kit.</li><li>Có thể lược bỏ <em>one/someone/people</em>: Someone sent me an email. → I was sent an email.</li><li>Lược bỏ tác nhân hiển nhiên: My mom gave birth to me in 1990. → I was born in 1990.</li><li>Nếu có nơi chốn và thời gian, sắp xếp cuối câu theo thứ tự <strong>Place – by – time</strong>.</li></ul>
'''

ex1 = [
field('1a','If a more efficient public transport system … (put into use)', 'is put into use'), field('1b','fewer people … (emigrate) to escape metropolitan congestion.', 'will emigrate'),
field('2a','Tourists … (take advantage of) the off-peak fares when traveling', 'will take advantage of|can take advantage of'), field('2b','if they … (not plan) to visit during rush hour.', "don't plan|do not plan"),
field('3a','If he … (study) the map more carefully before that trip,', 'had studied'), field('3b','he … (not get) lost in the unfamiliar city.', "wouldn't have got|would not have got|wouldn't have gotten|would not have gotten"),
field('4a','If cities … (accommodate) bicycles better,', 'accommodated'), field('4b','commuters … (get) to work quicker during rush hour.', 'would get'),
field('5a','I … (take a shortcut)', 'would have taken a shortcut|would have taken'), field('5b','if I … (know) I would get stuck in the traffic yesterday.', 'had known'),
field('6a','If cars … (be banned) from downtown areas during rush hours,', 'were banned'), field('6b','commuters … (experience) less congestion.', 'would experience'),
field('7a','Urban planners … (not set about) redesigning cities', "won't set about|will not set about"), field('7b','unless they … (foresee) an increase in rush-hour congestion.', 'foresee'),
field('8a','If I … (be) you,', 'were'), field('8b','I … (get itchy feet) in the summer!', 'would get itchy feet|would get'),
field('9a','If I … (know) about the road closure,', 'had known'), field('9b','I … (take) an alternate route.', 'would have taken'),
field('10a','When the topic of traveling … (bring up),', 'is brought up'), field('10b','my friend … (mention) the terrible memories of our last trip.', 'will mention|mentions')]

ex2 = [
field(1,'The smartphone is a great piece of technology. I use it every day.', 'The smartphone, which I use every day, is a great piece of technology.'),
field(2,'The tablet is state-of-the-art. I bought it last month.', 'The tablet, which I bought last month, is state-of-the-art.'),
field(3,'The laptop is multifunctional. My friend carries it with her everywhere.', 'The laptop, which my friend carries with her everywhere, is multifunctional.'),
field(4,'The smartwatch is cutting-edge. It has a 3-year guarantee.', 'The smartwatch, which has a 3-year guarantee, is cutting-edge.'),
field(5,'The gadget is eye-catching. It helps me keep up with the latest news.', 'The gadget, which helps me keep up with the latest news, is eye-catching.'),
field(6,'Many people are hooked on social media websites. They usually promote short-form content.', 'Many people are hooked on social media websites, which usually promote short-form content.'),
field(7,'She uses her smartphone on a daily basis. It helps her unwind after a long day at work.', 'She uses her smartphone on a daily basis, which helps her unwind after a long day at work.')]

ex3 = [
field(1,'Social media can foster a sense of community if people use it right.', 'A sense of community can be fostered by social media if it is used right.|A sense of community can be fostered by social media if people use it right.'),
field(2,'Many websites should accommodate disabled people with accessibility features.', 'Disabled people should be accommodated on many websites with accessibility features.'),
field(3,'Our parents pay for this trip, so we have such a blast!', 'This trip is paid for by our parents, so we have such a blast!'),
field(4,'If the government puts environmental protection laws into effect, we will be able to protect all of our natural tourist destinations.', 'If environmental protection laws are put into effect by the government, we will be able to protect all of our natural tourist destinations.'),
field(5,"If someone hadn't stolen my phone, I would have had a once-in-a-lifetime trip.", "If my phone hadn't been stolen, I would have had a once-in-a-lifetime trip."),
field(6,'Unless conservation efforts reduce habitat loss in this national park, the government will oversee the closure of the park.', 'Unless habitat loss is reduced in this national park by conservation efforts, the government will oversee the closure of the park.|Unless habitat loss is reduced by conservation efforts in this national park, the government will oversee the closure of the park.|Unless habitat loss is reduced in this national park, the government will oversee the closure of the park.'),
field(7,'We planned our trip beforehand, but the bad weather prevented us from enjoying ourselves.', 'Our trip was planned beforehand, but the bad weather prevented us from enjoying ourselves.|Our trip was planned beforehand by us, but the bad weather prevented us from enjoying ourselves.')]

work = '<div class="banner">Grammar Challenge</div>'
work += exercise('Exercise 1 — Conditional form','Fill in the blanks with the correct form of the verbs in brackets. You can use the negative form.',ex1)
work += exercise('Exercise 2 — Relative clauses','Combine the following sentences using relative clauses with the given words.',ex2)
work += exercise('Exercise 3 — Active to passive','Change the sentences from active voice to passive voice. If a sentence has two clauses, only the first clause needs to be changed.',ex3)
work += '''<details class="collapse answer-key-collapse"><summary>Đáp án đầy đủ</summary><div class="collapse-body"><p><strong>Exercise 1:</strong> 1 is put into use / will emigrate; 2 will (or can) take advantage of / don't plan; 3 had studied / wouldn't have got; 4 accommodated / would get; 5 would have taken a shortcut / had known; 6 were banned / would experience; 7 won't set about / foresee; 8 were / would get itchy feet; 9 had known / would have taken; 10 is brought up / will mention.</p><ol><li><strong>Exercise 2:</strong> The smartphone, which I use every day, is a great piece of technology.</li><li>The tablet, which I bought last month, is state-of-the-art.</li><li>The laptop, which my friend carries with her everywhere, is multifunctional.</li><li>The smartwatch, which has a 3-year guarantee, is cutting-edge.</li><li>The gadget, which helps me keep up with the latest news, is eye-catching.</li><li>Many people are hooked on social media websites, which usually promote short-form content.</li><li>She uses her smartphone on a daily basis, which helps her unwind after a long day at work.</li></ol><ol><li><strong>Exercise 3:</strong> A sense of community can be fostered by social media if it is used right.</li><li>Disabled people should be accommodated on many websites with accessibility features.</li><li>This trip is paid for by our parents, so we have such a blast!</li><li>If environmental protection laws are put into effect by the government, we will be able to protect all of our natural tourist destinations.</li><li>If my phone hadn't been stolen, I would have had a once-in-a-lifetime trip.</li><li>Unless habitat loss is reduced in this national park by conservation efforts, the government will oversee the closure of the park.</li><li>Our trip was planned beforehand, but the bad weather prevented us from enjoying ourselves.</li></ol></div></details>'''

work=work.replace('<div class="collapse-body"><p><strong>Exercise 1:', '<div class="collapse-body answer-key-content"><p><strong>Exercise 1:')
html = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>[FOUNDATION B] BREAK 2 - CHALLENGE</title><link rel="stylesheet" href="styles.css?v=13"></head><body class="lesson-page"><div class="shell"><header class="topbar compact-topbar"><a class="back" href="index.html">← Quay lại danh sách</a><div class="title-wrap"><div><div class="eyebrow">FOUNDATION B • GRAMMAR</div><h1 class="lesson-heading">[FOUNDATION B] BREAK 2 - CHALLENGE</h1></div><div class="original-top-actions"><button class="original-report-btn" type="button">Báo lỗi</button><a class="original-back-btn" href="index.html">← Quay lại</a></div><span class="lesson-badge">Bài số 21</span></div></header><main class="lesson-grid"><section class="panel"><h2>Đề bài</h2><div class="panel-body reading-source font-safe">{source}</div></section><section class="panel"><h2>Bài làm</h2><div class="panel-body reading-work font-safe">{work}</div></section></main><footer class="page-footer">Hai cột Đề bài / Bài làm cuộn độc lập trên máy tính.</footer></div><script src="app.js?v=12"></script></body></html>'''
(ROOT / 'break-2-challenge.html').write_text(unicodedata.normalize("NFC", html), encoding='utf-8')
