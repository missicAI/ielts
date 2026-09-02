from html import escape
from pathlib import Path
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "lesson-10-challenge-1.html"
LINK = "https://drive.google.com/file/d/1zjsALHIKI67jjQ2MMQNOD0OlOyiAmOqh/view?usp=drive_link"


def e(value):
    return escape(str(value), quote=True)


def input_box(answers, label, main=False):
    main_attr = ' data-main-answer="true"' if main else ""
    return (
        f'<input class="source-answer-input" type="text" data-answer="{e(answers)}" '
        f'aria-label="{e(label)}" autocomplete="off"{main_attr}>'
    )


def controls():
    return '''<div class="action-row"><button class="btn green" type="button" data-check-text>Kiểm tra</button><button class="btn ghost" type="reset" data-reset-text>Làm lại</button><span class="result" data-text-result></span></div>'''


def solution(number, answer, question_type, translation, analysis, evidence, paraphrase, detail):
    return f'''<article class="solution-card">
      <h4>Question {e(number)} / Answer: <span>{e(answer)}</span></h4>
      <dl>
        <dt>Loại câu hỏi</dt><dd>{e(question_type)}</dd>
        <dt>Dịch nghĩa</dt><dd>{e(translation)}</dd>
        <dt>Phân tích</dt><dd>{e(analysis)}</dd>
        <dt>Đoạn chứa thông tin</dt><dd><mark>{e(evidence)}</mark></dd>
        <dt>Từ khóa paraphrase</dt><dd>{e(paraphrase)}</dd>
        <dt>Giải thích chi tiết</dt><dd>{e(detail)}</dd>
      </dl>
    </article>'''


SOURCE = '''
<div class="original-reading-heading"><span class="reading-word">READING</span> <span class="reading-pass-label">READING PASSAGE 1</span></div>
<article class="reading-passage-card" id="passage-1">
  <h3>DAYLIGHT SAVING TIME</h3>
  <p>Each year in many countries around the world, clocks are set forward in spring and then back again in autumn in an effort to 'save' daylight hours. Like many modern practices, Daylight Savings Time (DST) dates back to ancient civilisations. The Romans would adjust their routines to the sun's schedule by using different scales in their water clocks for different months of the year.</p>
  <p>This practice fell out of favour, however, and the concept was renewed only when, in 1784, the American inventor Benjamin Franklin wrote a jocular article for <em>The Journal of Paris</em> exhorting the city's residents to make more use of daylight hours in order to reduce candle use. In 1895, in a more serious effort, New Zealand entomologist George Vernon Hudson proposed a biannual two-hour shift closely resembling current forms of DST. His cause was not taken up, however, until Germany first pushed their clocks forward in April 1916 as part of a drive to save fuel in World War I.</p>
  <p>Over the next several decades, global use of DST was sporadic and inconsistent. Countries such as the UK and USA adopted DST in World Wars I and II, but reverted to standard time after the wars ended. In the USA, the decision to use DST was determined by states and municipalities between 1945 and 1966, causing widespread confusion for transport and broadcasting schedules until Congress implemented the Uniform Time Act in 1966.</p>
  <p>Today, DST is used in some form by over 70 countries worldwide, affecting around one sixth of the world's population. There is still no uniform standard, however. Countries such as Egypt and Russia have adjusted their policies on multiple occasions in recent years, in some instances leading to considerable turmoil. Muslim countries often suspend DST for the month of Ramadan. The European Union finally standardised DST in 2000, while the USA's most recent adjustments were introduced with the Energy Policy Act of 2005.</p>
  <p>In general, the benefits of DST are considerable and well documented. Perhaps the most significant factor in terms of popular support is the chance to make better use of daylight in the evening. With extended daylight hours, office workers coming off a 9 to 5 shift can often take part in outdoor recreational activities for an hour or two. This has other positive effects, such as reducing domestic electricity consumption as more opportunities become available to use sunlight instead of artificial lighting. A further benefit is a reduction in the overall rate of automobile accidents, as DST ensures that streets are well lit at peak hours.</p>
  <p>Many industries are supportive of DST due to the opportunities it provides for increased revenue. Extended daylight hours mean people are more likely to stay out later in the evening and spend more money in bars and restaurants, for example, so tourism and hospitality are two sectors that stand to gain a lot from more daylight. In Queensland, Australia, which elected not to implement DST due to complaints from dairy farmers over disruption to milking schedules, the annual drain on the state's economy is estimated to be as high as $4 billion.</p>
  <p>Some research casts doubt on the advantages of DST, however. Although the overall incidence of traffic accidents is lower, for pedestrians, the risk of being hit by a car in the evening increases by as much as 186 per cent in the weeks after clocks are set back in autumn, possibly because drivers have not yet adjusted to earlier sunsets. Although this shift does in turn make streets safer in early mornings, the risk to pedestrians is not offset simply because fewer pedestrians use the streets at that time.</p>
  <p>A further health concern involves the disruption of our body clock. Setting clocks one hour forward at night can cause many people to lose sleep, resulting in tiredness and all its well-documented effects, such as mood swings, reduced productivity and problems with overall physical well-being. In 2008, a Swedish study found that heart attack rates spike in the few days following the switch to DST for summer. Tiredness may also be a factor behind the increase in road accidents in the week after DST begins.</p>
  <p>Finally, safety issues have arisen in parts of Latin America relating to a suspected relationship between DST and higher incidences of street crime. In 2008, Guatemala chose not to use DST because it forced office workers to leave their homes while it was still dark outside in the morning. This natural cover for criminals was thought to increase incidents of crime at this hour.</p>
</article>
<div class="original-reading-heading"><span class="reading-pass-label">READING PASSAGE 2</span></div>
<article class="reading-passage-card" id="passage-2">
  <h3>THE LIFE OF SIR ISAAC NEWTON</h3>
  <p><strong>A</strong> Isaac Newton was born on January 4, 1643, in Lincolnshire, England. The son of a farmer, who died three months before he was born, Newton spent most of his early years with his maternal grandmother after his mother remarried. Following an education interrupted by a failed attempt to turn him into a farmer, he attended the King's School in Grantham before enrolling at the University of Cambridge's Trinity College in 1661, where he soon became fascinated by the works of modern philosophers such as René Descartes. When the Great Plague shut Cambridge off from the rest of England in 1665, Newton returned home and began formulating his theories on calculus, light and color, his farm the setting for the supposed falling apple that inspired his work on gravity.</p>
  <p><strong>B</strong> Newton returned to Cambridge in 1667. He constructed the first reflecting telescope in 1668, and the following year he received his Master of Arts degree and took over as Cambridge's Professor of Mathematics. In 1671 he was asked to give a demonstration of his telescope to the Royal Society of London, the same year he was elected to the prestigious Society. The following year, fascinated with the study of light, he published his notes on optics for his peers. Through his experiments, Newton determined that white light was a composite of all the colors on the spectrum, and he asserted that light was composed of particles instead of waves. His methods were heavily criticized by established Society member Robert Hooke, who was also unwilling to compromise again with Newton's follow-up paper in 1675. Known for his temperamental defense of his work, Newton engaged in heated correspondence with Hooke before suffering a nervous breakdown and withdrawing from the public eye in 1678. In the following years, he returned to his earlier studies on the forces governing gravity.</p>
  <p><strong>C</strong> In 1684, English astronomer Edmund Halley paid a visit to the reclusive Newton. Upon learning that Newton had mathematically worked out the elliptical paths of celestial bodies, such as the movement of the planets around the sun, Halley urged him to organize his notes. The result was the 1687 publication of “Philosophiae Naturalis Principia Mathematica” (Mathematical Principles of Natural Philosophy), which established the three laws of motion and the law of universal gravity. Principia made Newton a star in intellectual circles, eventually earning him widespread acclaim as one of the most important figures in modern science.</p>
  <p><strong>D</strong> As a now influential figure, Newton opposed King James II's attempts to reinstate Catholic teachings at English Universities, and was elected to represent Cambridge in Parliament in 1689. He moved to London permanently after being named warden of the Royal Mint in 1696, earning a promotion to master of the Mint three years later. Determined to prove his position wasn't merely symbolic, Newton moved the pound sterling from the silver to the gold standard and sought to punish forgers.</p>
  <p><strong>E</strong> The death of Hooke in 1703 allowed Newton to take over as president of the Royal Society, and the following year he published his second major work, “Opticks.” Composed largely from his earlier notes on the subject, the book detailed Newton's experiments with refraction and the color spectrum, and also contained his conclusions on such matters as energy and electricity. In 1705, he was knighted by Queen Anne of England.</p>
  <p><strong>F</strong> Around this time, the debate over Newton's claims to originating the field of calculus, the mathematical study of change, exploded into a nasty dispute. Newton had developed his mathematical concept of “fluxions” (differentials) in the mid-1660s to account for celestial orbits, though there was no public record of his work. In the meantime, German mathematician Gottfried Leibniz formulated his own theories and published them in 1684. As president of the Royal Society, Newton oversaw an investigation that ruled his work to be the founding basis of the field, but the debate continued even after Leibniz's death in 1716. Researchers later concluded that both men likely arrived at their conclusions independent of one another.</p>
  <p><strong>G</strong> Newton was also obsessed with history and religious doctrines, and his writings on those subjects were collected into multiple books that were published after his death. Having never married, Newton spent his later years living with his niece at Cranbury Park, near Winchester, England. He died on March 31, 1727, and was buried in Westminster Abbey. A giant even among the brilliant minds that drove the Scientific Revolution, Newton is remembered as an extraordinary scholar, inventor and writer. His theories about the movement of bodies in the solar system transformed our understanding of the universe and his precise methodology helped to give birth to what is known as the scientific method. Although his theories of space-time and gravity were eventually superseded by those of Einstein, his work remains the foundation stone on which modern physics was built.</p>
</article>
'''


DST_QUESTIONS = [
    (1, "More opportunities for", "after work.", "(outdoor) recreational activities|outdoor recreational activities|recreational activities"),
    (2, "Better lighting during", "leads to fewer car crashes following the spring change to DST.", "peak hours"),
    (3, "Some industries, such as", ", earn more money with DST.", "tourism and hospitality|hospitality and tourism"),
    (4, "Dairy farmers find that DST upsets their", ".", "milking schedules"),
    (5, "More dangerous for", "following re-setting of clocks in autumn.", "pedestrians"),
    (6, "Loss of sleep can lead to", ", inferior performance at work and poorer general health because of fatigue.", "mood swings"),
    (7, "Darker mornings may lead to more", ".", "crime|street crime|incidents of crime"),
]


HEADINGS = [
    ("i", "Continued breakthroughs in research"),
    ("ii", "Competing claims of originality"),
    ("iii", "The early years of Sir Isaac Newton"),
    ("iv", "The legacy of an exceptional mind"),
    ("v", "Routine life at a 17th-century university"),
    ("vi", "Heated academic disputes"),
    ("vii", "A new venture"),
    ("viii", "His crowning achievement"),
    ("ix", "A controversial theory about planets"),
]


KEYWORDS = [
    ("PASSAGE 1", "1. after work", "office workers coming off a 9 to 5 shift / coming off a 9 to 5 shift", "office workers coming off a 9 to 5 shift|coming off a 9 to 5 shift"),
    ("PASSAGE 1", "1. use less power in their homes", "reducing domestic electricity consumption", "reducing domestic electricity consumption"),
    ("PASSAGE 1", "2. better lighting", "streets are well lit / well lit / streets are well-lit / well-lit", "streets are well lit|well lit|streets are well-lit|well-lit"),
    ("PASSAGE 1", "2. fewer", "a reduction in / reduction", "a reduction in|reduction"),
    ("PASSAGE 1", "2. car crashes", "automobile accidents", "automobile accidents"),
    ("PASSAGE 1", "3. industries", "sectors", "sectors"),
    ("PASSAGE 1", "3. earn more money", "increased revenue / gain a lot / increased revenue, gain a lot", "increased revenue|gain a lot|increased revenue, gain a lot"),
    ("PASSAGE 1", "4. upsets", "disruption to / disruption", "disruption to|disruption"),
    ("PASSAGE 1", "5. dangerous", "risk / the risk of / the risk of being hit by a car / the risk of being hit by a car in the evening", "risk|the risk of|the risk of being hit by a car|the risk of being hit by a car in the evening"),
    ("PASSAGE 1", "5. re-setting", "set back", "set back"),
    ("PASSAGE 1", "6. loss of sleep", "lose sleep", "lose sleep"),
    ("PASSAGE 1", "6. inferior performance at work", "reduced productivity", "reduced productivity"),
    ("PASSAGE 1", "6. poorer general health", "problems with overall physical well-being", "problems with overall physical well-being"),
    ("PASSAGE 1", "6. fatigue", "tiredness", "tiredness"),
    ("PASSAGE 2", "8. Heated academic disputes", "heavily criticized", "heavily criticized"),
    ("PASSAGE 2", "9. crowning achievement", "one of the most important figures in modern science", "one of the most important figures in modern science"),
    ("PASSAGE 2", "11. Continued breakthroughs in research", "second major work", "second major work"),
    ("PASSAGE 2", "12. originality", "independent of one another", "independent of one another"),
    ("PASSAGE 2", "13. an exceptional mind", "brilliant minds", "brilliant minds"),
    ("PASSAGE 2", "16. created", "constructed", "constructed"),
    ("PASSAGE 2", "18. constitute", "was composed of", "was composed of"),
    ("PASSAGE 2", "20. Joint founder", "originating the field of", "originating the field of"),
]


VOCABULARY = [
    ("READING PASSAGE 1", "This practice fell out of favour, however, ...", "fall out of favour", "phrase / idiom", "không còn được ưa chuộng"),
    ("READING PASSAGE 1", "Over the next several decades, global use of DST was sporadic and inconsistent.", "global use of", "noun phrase", "việc sử dụng trên toàn cầu"),
    ("READING PASSAGE 1", "In general, the benefits of DST are considerable and well-documented.", "well-documented", "adjective", "được ghi chép và chứng minh đầy đủ"),
    ("READING PASSAGE 1", "With extended daylight hours, office workers coming off a 9 to 5 shift can often take part in outdoor recreational activities for an hour or two.", "extended", "adjective", "được kéo dài"),
    ("READING PASSAGE 1", "With extended daylight hours, office workers coming off a 9 to 5 shift can often take part in outdoor recreational activities for an hour or two.", "outdoor recreational activities", "noun phrase", "các hoạt động giải trí ngoài trời"),
    ("READING PASSAGE 1", "This has other positive effects, such as reducing domestic electricity consumption as more opportunities become available to use sunlight instead of artificial lighting.", "domestic electricity consumption", "noun phrase", "mức tiêu thụ điện trong gia đình"),
    ("READING PASSAGE 1", "This has other positive effects, such as reducing domestic electricity consumption as more opportunities become available to use sunlight instead of artificial lighting.", "artificial lighting", "noun phrase", "ánh sáng nhân tạo"),
    ("READING PASSAGE 1", "A further benefit is a reduction in the overall rate of automobile accidents, as DST ensures that streets are well-lit at peak hours.", "automobile accidents", "noun phrase", "tai nạn ô tô"),
    ("READING PASSAGE 1", "A further benefit is a reduction in the overall rate of automobile accidents, as DST ensures that streets are well-lit at peak hours.", "well-lit", "adjective", "được chiếu sáng tốt"),
    ("READING PASSAGE 1", "Some research casts doubt on the advantages of DST", "cast doubt on", "verb phrase", "đặt nghi vấn về"),
    ("READING PASSAGE 1", "Although this shift does in turn make streets safer in early mornings, the risk to pedestrians is not offset simply because fewer pedestrians use the streets at that time", "offset", "verb", "bù đắp"),
    ("READING PASSAGE 1", "In 2008, a Swedish study found that heart attack rates spike in the few days following the switch to DST for summer.", "spike", "verb", "tăng vọt"),
    ("READING PASSAGE 1", "Tiredness may also be a factor behind the increase in road accidents in the week after DST begins.", "be a factor behind", "verb phrase", "là một nguyên nhân đằng sau"),
    ("READING PASSAGE 2", "Following an education interrupted by a failed attempt to turn him into a farmer, he attended the King's School in Grantham.", "interrupt", "verb", "làm gián đoạn"),
    ("READING PASSAGE 2", "Newton returned home and began formulating his theories on calculus, light and color.", "formulate his theories", "verb phrase", "hình thành các học thuyết của ông"),
    ("READING PASSAGE 2", "Newton returned to Cambridge in 1667. He constructed the first reflecting telescope in 1668.", "telescope", "noun", "kính thiên văn"),
    ("READING PASSAGE 2", "The same year he was elected to the prestigious Society.", "prestigious", "adjective", "danh giá, có uy tín"),
    ("READING PASSAGE 2", "Through his experiments, Newton determined that white light was a composite of all the colors on the spectrum.", "composite", "noun", "hỗn hợp"),
    ("READING PASSAGE 2", "Known for his temperamental defense of his work, Newton engaged in heated correspondence with Hooke ...", "temperamental", "adjective", "thất thường, nóng nảy"),
    ("READING PASSAGE 2", "Principia made Newton a star in intellectual circles, eventually earning him widespread acclaim as one of the most important figures in modern science.", "intellectual circles", "noun phrase", "giới trí thức"),
    ("READING PASSAGE 2", "Principia made Newton a star in intellectual circles, eventually earning him widespread acclaim as one of the most important figures in modern science.", "earn someone widespread acclaim as", "verb phrase", "mang lại cho ai sự công nhận rộng rãi với tư cách là"),
    ("READING PASSAGE 2", "As a now influential figure, Newton opposed King James II's attempts to reinstate Catholic teachings at English Universities.", "an influential figure", "noun phrase", "một nhân vật có ảnh hưởng"),
    ("READING PASSAGE 2", "Around this time, the debate over Newton's claims to originating the field of calculus, the mathematical study of change, exploded into a nasty dispute.", "a nasty dispute", "noun phrase", "một cuộc tranh chấp gay gắt"),
    ("READING PASSAGE 2", "A giant even among the brilliant minds that drove the Scientific Revolution, Newton is remembered as an extraordinary scholar, inventor and writer.", "a brilliant mind", "noun phrase", "một trí tuệ xuất chúng"),
    ("READING PASSAGE 2", "A giant even among the brilliant minds that drove the Scientific Revolution, Newton is remembered as an extraordinary scholar, inventor and writer.", "an extraordinary scholar", "noun phrase", "một học giả phi thường"),
]


def highlight(sentence, phrase):
    start = sentence.lower().find(phrase.lower())
    if start < 0:
        if phrase == "interrupt":
            start = sentence.lower().find("interrupted")
            end = start + len("interrupted")
        elif phrase == "formulate his theories":
            start = sentence.lower().find("formulating his theories")
            end = start + len("formulating his theories")
        elif phrase == "a brilliant mind":
            start = sentence.lower().find("brilliant minds")
            end = start + len("brilliant minds")
        else:
            return e(sentence)
    else:
        end = start + len(phrase)
    return e(sentence[:start]) + '<mark class="vocab-highlight">' + e(sentence[start:end]) + "</mark>" + e(sentence[end:])


def main_questions():
    left = []
    right = []
    for number, before, after, answers in DST_QUESTIONS:
        row = f'''<div class="dst-question-row"><strong>{number}.</strong><span>{e(before)} {input_box(answers, f"Question {number}", True)} {e(after)}</span></div>'''
        (left if number in (1, 2, 3) else right).append(row)
    table = f'''<section class="task-card"><div class="source-task-banner">Questions 1–7</div><h3>Complete the table below.</h3><p><strong>Choose NO MORE THAN THREE WORDS from the passage for each answer.</strong></p><p>Write your answers in boxes 1–7 on your answer sheet.</p><h3 class="table-caption">Advantages and disadvantages of Daylight Saving Time</h3><form data-text-form><div class="dst-comparison"><section><h4>Advantages</h4>{''.join(left[:1])}<p>People use less power in their homes because they don't need as much lighting.</p>{''.join(left[1:])}</section><section><h4>Disadvantages</h4>{''.join(right)}</section></div>{controls()}</form></section>'''

    heading_list = ''.join(f'<li><strong>{roman}</strong> {e(title)}</li>' for roman, title in HEADINGS)
    heading_rows = []
    for number, paragraph, answers in ((8, "B", "vi|6"), (9, "C", "viii|8"), (10, "D", "vii|7"), (11, "E", "i|1"), (12, "F", "ii|2"), (13, "G", "iv|4")):
        heading_rows.append(f'<label class="question-row"><strong>{number}.</strong><span>Paragraph {paragraph}</span>{input_box(answers, f"Question {number}", True)}</label>')
    headings = f'''<section class="task-card"><div class="source-task-banner">Questions 8–13</div><h3>Reading Passage 2 has seven paragraphs, A–G.</h3><p><strong>Choose the correct heading for paragraphs B–G from the list of headings below.</strong></p><p>Write the correct number, i–ix, in boxes 8–13 on your answer sheet.</p><div class="headings-box"><h4>List of Headings</h4><ol>{heading_list}</ol><p><strong>Example — Paragraph A: iii</strong></p></div><form data-text-form>{''.join(heading_rows)}{controls()}</form></section>'''

    short_rows = [
        (14, "With which scientific organisation was Newton associated for much of his career?", "Royal Society"),
        (15, "With whom did Newton live as he got older?", "niece|his niece"),
    ]
    short = ''.join(f'<label class="question-row"><strong>{n}.</strong><span>{e(q)}</span>{input_box(a, f"Question {n}", True)}</label>' for n, q, a in short_rows)
    questions_14_15 = f'''<section class="task-card"><div class="source-task-banner">Questions 14–15</div><p><strong>Answer the questions below.</strong></p><p>Choose NO MORE THAN TWO WORDS from the passage for each answer.</p><form data-text-form>{short}{controls()}</form></section>'''

    note_rows = [
        (16, "He created the first reflecting", ".", "telescope"),
        (17, "He published his notes on", ".", "optics"),
        (18, "He claimed that light was made of", "rather than waves.", "particles"),
        (19, "Principia established the three laws of", ".", "motion"),
        (20, "Newton was joint founder of the field of", ".", "calculus"),
    ]
    notes = ''.join(f'<div class="note-completion-row"><strong>{n}.</strong><span>{e(before)} {input_box(a, f"Question {n}", True)} {e(after)}</span></div>' for n, before, after, a in note_rows)
    questions_16_20 = f'''<section class="task-card"><div class="source-task-banner">Questions 16–20</div><h3>Complete the notes below.</h3><p><strong>Choose ONE WORD ONLY from the passage for each answer.</strong></p><form data-text-form><div class="notes-source-box">{notes}</div>{controls()}</form></section>'''
    return table + headings + questions_14_15 + questions_16_20


SOLUTION_DATA = [
    (1, "(OUTDOOR) RECREATIONAL ACTIVITIES", "Table completion", "Nhiều cơ hội hơn cho ___ sau giờ làm việc.", "Cần một cụm danh từ chỉ hoạt động mà người lao động có thể tham gia sau giờ làm.", "With extended daylight hours, office workers coming off a 9 to 5 shift can often take part in outdoor recreational activities for an hour or two.", "after work = office workers coming off a 9 to 5 shift; opportunities = can take part in", "Câu chứa thông tin nói rõ nhân viên văn phòng sau ca 9–5 có thể tham gia các hoạt động giải trí ngoài trời. Vì vậy đáp án là recreational activities hoặc outdoor recreational activities."),
    (2, "PEAK HOURS", "Table completion", "Ánh sáng tốt hơn trong ___ dẫn đến ít tai nạn ô tô hơn sau khi chuyển sang DST vào mùa xuân.", "Sau giới từ during cần một cụm danh từ chỉ thời gian.", "A further benefit is a reduction in the overall rate of automobile accidents, as DST ensures that streets are well lit at peak hours.", "better lighting = streets are well lit; fewer = a reduction in; car crashes = automobile accidents; during = at", "Đường phố được chiếu sáng tốt vào giờ cao điểm làm giảm tai nạn ô tô, nên cụm thời gian cần điền là peak hours."),
    (3, "TOURISM AND HOSPITALITY / HOSPITALITY AND TOURISM", "Table completion", "Một số ngành, chẳng hạn như ___, kiếm được nhiều tiền hơn nhờ DST.", "Cần cụm danh từ chỉ các ngành hưởng lợi về doanh thu.", "Tourism and hospitality are two sectors that stand to gain a lot from more daylight.", "industries = sectors; earn more money = increased revenue / gain a lot", "Đoạn văn nêu trực tiếp hai lĩnh vực hưởng lợi là tourism và hospitality; có thể viết theo cả hai thứ tự."),
    (4, "MILKING SCHEDULES", "Table completion", "Nông dân chăn nuôi bò sữa thấy rằng DST làm xáo trộn ___.", "Cần cụm danh từ chỉ hoạt động trong nghề chăn nuôi bò sữa.", "Queensland ... elected not to implement DST due to complaints from dairy farmers over disruption to milking schedules.", "upsets = disruption to; dairy farmers = dairy farmers", "Lời phàn nàn của nông dân liên quan trực tiếp đến việc lịch vắt sữa bị xáo trộn, nên đáp án là milking schedules."),
    (5, "PEDESTRIANS", "Table completion", "Nguy hiểm hơn đối với ___ sau khi chỉnh lại đồng hồ vào mùa thu.", "Cần danh từ số nhiều chỉ nhóm người gặp rủi ro.", "For pedestrians, the risk of being hit by a car in the evening increases ... after clocks are set back in autumn.", "more dangerous = risk increases; re-setting = set back", "Nhóm có nguy cơ bị ô tô đâm tăng lên là người đi bộ; pedestrians là từ dùng nguyên văn trong passage."),
    (6, "MOOD SWINGS", "Table completion", "Mất ngủ có thể dẫn đến ___, hiệu suất làm việc kém và sức khỏe tổng thể giảm sút do mệt mỏi.", "Cần một cụm danh từ chỉ tác động của mệt mỏi, đứng song song với reduced productivity và physical well-being problems.", "Setting clocks one hour forward ... can cause many people to lose sleep, resulting in tiredness and ... mood swings, reduced productivity and problems with overall physical well-being.", "loss of sleep = lose sleep; inferior performance = reduced productivity; fatigue = tiredness", "Danh sách hậu quả gồm mood swings, reduced productivity và problems with overall physical well-being. Ô trống đầu tiên vì vậy là mood swings."),
    (7, "CRIME / STREET CRIME / INCIDENTS OF CRIME", "Table completion", "Buổi sáng tối hơn có thể dẫn đến nhiều ___ hơn.", "Cần danh từ chỉ vấn đề an toàn tăng lên vào buổi sáng tối trời.", "This natural cover for criminals was thought to increase incidents of crime at this hour.", "darker mornings = still dark outside in the morning; lead to more = increase", "Bóng tối tạo sự che chắn cho tội phạm và được cho là làm tăng các vụ phạm tội. Các đáp án crime, street crime hoặc incidents of crime đều nằm trong giới hạn ba từ."),
    (8, "vi — Heated academic disputes", "Matching headings", "Đoạn B phù hợp với tiêu đề nào?", "Tìm ý chính bao trùm toàn đoạn thay vì chỉ một chi tiết.", "His methods were heavily criticized ... Newton engaged in heated correspondence with Hooke.", "heated academic disputes = heavily criticized / heated correspondence", "Đoạn B tập trung vào sự chỉ trích và tranh luận gay gắt giữa Newton và Hooke, nên tiêu đề vi là phù hợp."),
    (9, "viii — His crowning achievement", "Matching headings", "Đoạn C phù hợp với tiêu đề nào?", "Xác định thành tựu nổi bật nhất được mô tả trong đoạn.", "The result was the 1687 publication of ... Principia ... earning him widespread acclaim as one of the most important figures in modern science.", "crowning achievement = Principia / widespread acclaim", "Đoạn C trình bày việc xuất bản Principia và danh tiếng lớn mà tác phẩm mang lại, đây là thành tựu đỉnh cao của Newton."),
    (10, "vii — A new venture", "Matching headings", "Đoạn D phù hợp với tiêu đề nào?", "Theo dõi sự chuyển hướng nghề nghiệp của Newton.", "He moved to London permanently after being named warden of the Royal Mint.", "new venture = warden/master of the Royal Mint", "Newton chuyển tới London để đảm nhiệm công việc tại Royal Mint, một hướng hoạt động mới ngoài nghiên cứu học thuật."),
    (11, "i — Continued breakthroughs in research", "Matching headings", "Đoạn E phù hợp với tiêu đề nào?", "Tìm dấu hiệu về các công trình nghiên cứu tiếp theo.", "The following year he published his second major work, “Opticks.”", "continued breakthroughs = second major work", "Việc xuất bản công trình lớn thứ hai, Opticks, cho thấy Newton tiếp tục tạo ra đột phá nghiên cứu."),
    (12, "ii — Competing claims of originality", "Matching headings", "Đoạn F phù hợp với tiêu đề nào?", "Đoạn nói về tranh chấp ai là người khai sinh một lĩnh vực.", "The debate over Newton's claims to originating the field of calculus ... Gottfried Leibniz formulated his own theories.", "claims of originality = claims to originating; competing = Newton and Leibniz", "Newton và Leibniz cùng có tuyên bố về nguồn gốc của calculus; nghiên cứu sau này cho rằng họ đi đến kết luận độc lập."),
    (13, "iv — The legacy of an exceptional mind", "Matching headings", "Đoạn G phù hợp với tiêu đề nào?", "Xác định phần tổng kết về đóng góp và ảnh hưởng lâu dài.", "Newton is remembered as an extraordinary scholar ... his work remains the foundation stone on which modern physics was built.", "exceptional mind = brilliant minds / extraordinary scholar; legacy = remains the foundation stone", "Đoạn cuối tổng kết tài năng và di sản khoa học lâu dài của Newton, nên chọn iv."),
    (14, "ROYAL SOCIETY", "Short-answer question", "Newton gắn bó với tổ chức khoa học nào trong phần lớn sự nghiệp?", "Cần tên riêng của một tổ chức khoa học, không quá hai từ.", "He was asked to give a demonstration of his telescope to the Royal Society ... elected to the prestigious Society.", "scientific organisation = Society; associated = elected / president", "Newton là thành viên rồi trở thành chủ tịch Royal Society; đáp án đủ hai từ theo giới hạn."),
    (15, "NIECE / HIS NIECE", "Short-answer question", "Newton sống cùng ai khi ông lớn tuổi hơn?", "Cần danh từ chỉ người, không quá hai từ.", "Newton spent his later years living with his niece at Cranbury Park.", "as he got older = later years; lived with = living with", "Cụm his niece xuất hiện nguyên văn và trả lời trực tiếp câu hỏi."),
    (16, "TELESCOPE", "Note completion", "Ông tạo ra chiếc ___ phản xạ đầu tiên.", "Cần danh từ số ít sau reflecting; chỉ được dùng một từ.", "He constructed the first reflecting telescope in 1668.", "created = constructed", "Vật Newton chế tạo là reflecting telescope; từ cần điền duy nhất là telescope."),
    (17, "OPTICS", "Note completion", "Ông công bố các ghi chép về ___.", "Cần danh từ chỉ lĩnh vực nghiên cứu; một từ.", "Fascinated with the study of light, he published his notes on optics for his peers.", "published his notes = published work; study of light = optics", "Passage dùng trực tiếp notes on optics, nên đáp án là optics."),
    (18, "PARTICLES", "Note completion", "Ông cho rằng ánh sáng được cấu thành từ ___ thay vì sóng.", "Cần danh từ số nhiều đối lập với waves.", "He asserted that light was composed of particles instead of waves.", "constitute = was composed of; rather than = instead of", "Cấu trúc đối lập particles với waves xác định rõ từ cần điền."),
    (19, "MOTION", "Note completion", "Principia thiết lập ba định luật về ___.", "Cần một danh từ sau laws of.", "Principia ... established the three laws of motion and the law of universal gravity.", "established = established; three laws = three laws", "Cụm cố định trong passage là three laws of motion, vì vậy đáp án một từ là motion."),
    (20, "CALCULUS", "Note completion", "Newton là người đồng sáng lập lĩnh vực ___.", "Cần tên một lĩnh vực toán học; một từ.", "The debate over Newton's claims to originating the field of calculus ... Gottfried Leibniz formulated his own theories.", "joint founder = Newton and Leibniz / originating the field of", "Hai nhà toán học được xem là đã phát triển calculus độc lập, nên lĩnh vực cần điền là calculus."),
]


def keyword_task():
    rows = []
    answer_rows = []
    current = None
    for group, keyword, answer, accepted in KEYWORDS:
        if group != current:
            rows.append(f'<tr class="source-group-row"><th colspan="2">{e(group)}</th></tr>')
            answer_rows.append(f'<tr class="source-group-row"><th colspan="2">{e(group)}</th></tr>')
            current = group
        rows.append(f'<tr><td>{e(keyword)}</td><td>{input_box(accepted, keyword)}</td></tr>')
        answer_rows.append(f'<tr><td>{e(keyword)}</td><td class="answer-reference">{e(answer)}</td></tr>')
    return f'''<section class="reference-task"><div class="source-table-title">Keyword table</div><form data-text-form><div class="source-table-wrap"><table class="source-entry-table keyword-source-table"><thead><tr><th>Keywords in the questions</th><th>Similar words in the passage</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>{controls()}</form><details class="answer-key-collapse collapse" data-section="keyword-answer-key"><summary>Xem đáp án Keyword table</summary><div class="collapse-body source-table-wrap"><table class="source-entry-table"><thead><tr><th>Keywords in the questions</th><th>Similar words in the passage</th></tr></thead><tbody>{''.join(answer_rows)}</tbody></table></div></details></section>'''


def vocabulary_task():
    rows = []
    answer_rows = []
    current = None
    for group, sentence, phrase, word_type, meaning in VOCABULARY:
        if group != current:
            rows.append(f'<tr class="source-group-row"><th colspan="4">{e(group)}</th></tr>')
            answer_rows.append(f'<tr class="source-group-row"><th colspan="4">{e(group)}</th></tr>')
            current = group
        sentence_html = highlight(sentence, phrase)
        rows.append(f'<tr><td>{sentence_html}</td><td>{e(phrase)}</td><td>{input_box(word_type, phrase + " word type")}</td><td>{input_box(meaning, phrase + " meaning")}</td></tr>')
        answer_rows.append(f'<tr><td>{sentence_html}</td><td>{e(phrase)}</td><td class="answer-reference">{e(word_type)}</td><td class="answer-reference">{e(meaning)}</td></tr>')
    return f'''<section class="reference-task"><div class="source-table-title">New vocabulary</div><form data-text-form><div class="source-table-wrap"><table class="source-entry-table vocabulary-source-table"><thead><tr><th>Sentences</th><th>Useful words/phrases</th><th>Type of word<br>(n/ v/ adj/ adv...)</th><th>Meaning<br>(in English/ in Vietnamese)</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>{controls()}</form><details class="answer-key-collapse collapse" data-section="vocabulary-answer-key"><summary>Xem đáp án New vocabulary</summary><div class="collapse-body source-table-wrap"><table class="source-entry-table vocabulary-source-table"><thead><tr><th>Sentences</th><th>Useful words/phrases</th><th>Type of word</th><th>Meaning</th></tr></thead><tbody>{''.join(answer_rows)}</tbody></table></div></details></section>'''


def build():
    solutions = ''.join(solution(*row) for row in SOLUTION_DATA)
    work = main_questions()
    work += f'<details class="collapse solutions-collapse"><summary>Giải thích chi tiết đáp án</summary><div class="collapse-body">{solutions}</div></details>'
    work += keyword_task()
    work += vocabulary_task()
    work += f'''<section class="external-reading"><p>Read the passage in the following <a class="inline-link" href="{e(LINK)}" target="_blank" rel="noopener">LINK</a> carefully, remember the meaning of the vocabulary in yellow and note down at least 10 new/useful words/phrases.</p><label for="lesson19-notes"><strong>Note down at least 10 new/useful words/phrases from the reading passages.</strong></label><textarea id="lesson19-notes" class="notes-area"></textarea></section>'''
    html = f'''<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>[FOUNDATION B] LESSON 10 - CHALLENGE 1</title>
  <link rel="stylesheet" href="styles.css?v=13">
</head>
<body class="lesson-page">
  <div class="shell">
    <header class="topbar compact-topbar">
      <a class="back" href="index.html">← Quay lại danh sách</a>
      <div class="title-wrap">
        <div><div class="eyebrow">FOUNDATION B • IELTS READING</div><h1 class="lesson-heading">[FOUNDATION B] LESSON 10 - CHALLENGE 1</h1></div>
        <div class="original-top-actions"><button class="original-report-btn" type="button">Báo lỗi</button><a class="original-back-btn" href="index.html">← Quay lại</a></div>
        <span class="lesson-badge">Bài số 19</span>
      </div>
    </header>
    <main class="lesson-grid">
      <section class="panel"><h2>Đề bài</h2><div class="panel-body reading-source font-safe">{SOURCE}<p class="external-reading">Read the passage in the following <a class="inline-link" href="{e(LINK)}" target="_blank" rel="noopener">LINK</a> carefully.</p></div></section>
      <section class="panel"><h2>Bài làm</h2><div class="panel-body reading-work font-safe">{work}</div></section>
    </main>
  </div>
  <script src="app.js?v=12"></script>
</body>
</html>'''
    OUTPUT.write_text(unicodedata.normalize("NFC", html), encoding="utf-8")


if __name__ == "__main__":
    build()
