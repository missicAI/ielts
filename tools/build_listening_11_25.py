from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def transcript(text):
    paras = ''.join(f'<p>{escape(p.strip())}</p>' for p in text.strip().split('\n\n') if p.strip())
    return f'<details class="collapse transcript-collapse"><summary>◉ Xem transcript</summary><div class="collapse-body transcript-text">{paras}</div></details>'


def track(n, src, text):
    return f'<div class="audio-card"><h3>Exercise {n}</h3><audio controls preload="metadata" src="{src}"></audio>{transcript(text)}</div>'


def field(q, answer, prompt):
    return f'<label class="question-row"><strong>{q}.</strong> <span>{prompt}</span><input type="text" data-answer="{escape(answer, quote=True)}" autocomplete="off"></label>'


def form(ex, instruction, fields):
    return f'''<section class="exercise-block"><h3>Exercise {ex}</h3><p><strong>{instruction}</strong></p><form data-text-form>{''.join(fields)}<div class="actions"><button class="btn green" type="button" data-check-text>Kiểm tra</button><button class="btn" type="reset" data-reset-text>Làm lại</button></div><div class="result" data-text-result></div></form></section>'''


def shell(number, title, source, work, filename):
    work=work.replace('<details class="collapse answer-key-collapse"><summary>', '<details class="collapse answer-key-collapse"><summary>').replace('<div class="collapse-body"><p><strong>Ex', '<div class="collapse-body answer-key-content"><p><strong>Ex')
    (ROOT / filename).write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><link rel="stylesheet" href="styles.css?v=13"></head><body class="lesson-page"><div class="shell"><header class="topbar compact-topbar"><a class="back" href="index.html">← Quay lại danh sách</a><div class="title-wrap"><div><div class="eyebrow">FOUNDATION B • IELTS LISTENING</div><h1 class="lesson-heading">{escape(title)}</h1></div><span class="lesson-badge">Bài số {number}</span></div></header><main class="lesson-grid"><section class="panel"><h2>Đề bài</h2><div class="panel-body reading-source font-safe"><div class="section-label">LISTENING</div>{source}</div></section><section class="panel"><h2>Bài làm</h2><div class="panel-body reading-work font-safe"><div class="banner">Listening</div>{work}</div></section></main><footer class="page-footer">Audio và transcript được đặt theo từng Exercise; hai cột cuộn độc lập.</footer></div><script src="app.js?v=12"></script></body></html>''', encoding="utf-8")


t13_1 = '''Hello, everyone, and welcome aboard the Sunshine Express on our journey from London to Naples. I'm Jane Sharpe, the train manager, and I hope you'll all enjoy the trip.

Before we depart, I'd like to tell you a bit about the train and its facilities. Now, we're here on the observation deck, which is where you'll probably spend most of your trip, as it offers the best views, and directly below us is a, well, we call it our leisure centre. There are some games machines, a television, a small library and so on. If you've brought a laptop or computer with you, you can also get onto the Internet here, as it has full Wi-Fi capability. There's also a small bar where you can get tea, coffee and light meals. For lunch and dinner, you'll use the restaurant car, which is at the front of the train. You'll have breakfast in your cabins, by the way, which will be brought to you by your steward.

The two cars behind the restaurant are where you'll find the second-class cabins. Each cabin has seats which are changed into beds at night. You'll also find a simple basin for washing, and a small fold-down table. First-class passengers, your cabins are at the back of the train. To get to them, you'll need to pass through the lounge. This can be used by everyone during the day, but is exclusive to first-class passengers after 6 p.m.

Right at the back of the train, basically as far as you can go, is my office. If anyone needs to see me, though, please use the phone in your cabin rather than coming to the office. Just press one and you'll get me. If I'm not there, tell your steward you need to see the manager, and he or she will look for me.'''
t13_2 = '''Right, let me give you a bit more information about the trip. The first part of our journey is from London to Paris, going through the Channel Tunnel. It will take us just over an hour to get to the Tunnel, including a short stop before we get there to pick up some more passengers. From there, it'll be another three hours to Paris, so we're looking at four hours altogether, give or take a few minutes.

A quick bit of advice about passports. You won't need these until we get to the Italian border, so I suggest you keep them in the safe which you'll find in your cabin. Ask your steward — that's the person in charge of your carriage — for a key. That way, you won't need to carry them with you all the time.

Now, meals. As I said earlier, breakfast tomorrow morning will be in your cabins, and this will be served at about 7.30, 7.45, so you'll be able to enjoy it as we travel along the southern French coast. Lunch is at 1 o'clock in the restaurant car, and dinner is at 8 o'clock, although we'd like you all to be at your table about fifteen minutes earlier, at a quarter to, if you could.

When we get to the Italian border tomorrow morning, our train will change engines, and we'll also be getting a new crew. We'll be taking advantage of the stop to have a look around. I've arranged a visit to the local market, a museum and a castle. This will take about four hours, with a break for coffee in a local café, and we'll be back on the train in time for lunch.

A few quick rules. Some of you might have brought your own food or drink on board. That's fine, but could we ask that you consume it in your cabins and not in the restaurant or lounge? Could we also ask you to make sure your cabin windows are closed when you're not in your cabin? And whatever you do, don't get off the train until we reach the Italian border. Apart from the border and one or two other places, which I'll tell you about, any stops we make will only be for a few minutes. I'd hate to leave anyone behind.'''
t13_3 = '''Welcome to Manham Port, where a thousand years of history are brought to life. All the family can enjoy a day out at Manham: visit our copper mine, see models of the machinery it used, have your photo taken in a nineteenth-century costume, experience at first hand how people lived at different stages throughout history, and especially how children studied, worked and played.

The port of Manham is located in beautiful and peaceful countryside, on a bend in the great River Avon, and developed here because it's the highest navigable point of the Avon — boats can go no higher up this river — and proved a handy place to load and unload cargo to and from the sea, which is over 23 miles away. A small port was already established here when, about 900 years ago, tin was discovered nearby, though it wasn't until the Industrial Revolution, when a tremendous need for metals of all kinds developed, that Manham expanded to become one of the busiest ports in the country. And because it was already so busy, prospectors began to look for other minerals, and by the end of the nineteenth century, lead, copper, manganese and arsenic were added to the cargoes leaving Manham.

In the early days, the ores had been smelted — or processed — in the same area they were mined. But, as demand grew, the smelting process required huge factory furnaces or fires to melt the metal from the rock and there was not enough coal in the local area, so the rocks containing minerals had to be shipped long distances.

Sadly, in the twentieth century, the great port of Manham declined, and thousands of workers were forced to emigrate out of the area. The buildings at the port fell into disrepair, and the place became almost forgotten. But then, the Manham Trust was formed to conserve the historical resources of the area. It organised scores of local volunteers to remove undergrowth to find the original outlines of the installations. It then brought in paid professionals to match installations with maps of the original port complex and to set about reconstructing it. Today you can see the results of this ambitious programme of restoration. The intention, and we believe this will be realised before the end of the year, is to return Manham Port to the condition it reached at its peak as “the greatest copper port in the country”.'''
t13_4 = '''Longfield Park has a programme of activities throughout the year, and to give you a sample, this is what's happening in the next few days. On Monday you can learn about herbs, and how they've been used over the centuries. You'll start with four of our herb gardens, practise the technique of using them as colour dyes for cloth, and listen to an illustrated talk about their use in cooking and medicine.

Then on Wednesday you can join local experts to discover the variety of insects and birds that appear in the evening. We keep to a small number of people in the group, so if you want to go you'll need to phone the park ranger a few days ahead. There's a small charge, which you should pay when you turn up.

I'm sure you're all keen to help with the practical task of looking after the park, so on Saturday you can join a working party. You'll have a choice of all sorts of activities, from planting hedges to picking up litter, so you'll be able to change from one to another when you feel like it. The rangers will be hard at work all day, but do come and join in, even for just a short while. One thing, though, is to make sure you're wearing something that you don't mind getting dirty or torn.'''

source13 = track(1, "assets/bai-13/ex1.mp3", t13_1) + track(2, "assets/bai-13/ex2.mp3", t13_2) + track(3, "assets/bai-13/ex3.mp3", t13_3) + track(4, "assets/bai-13/ex4.mp3", t13_4)
work13 = form(1, "Label the Sunshine Express diagram. Write ONE WORD ONLY.", [field(1,"Internet","Leisure centre: access to …"),field(2,"restaurant","Car at the front used for lunch and dinner"),field(3,"washing","Second-class cabins have a basin for …"),field(4,"lounge","Pass through the … to reach first class"),field(5,"manager","Contact the train … through your steward")])
work13 += form(2, "Choose A, B or C.", [field(1,"C","How long to Paris? A about one hour / B about three hours / C about four hours"),field(2,"B","Passports: A leave with steward / B lock away / C carry at all times"),field(3,"A","Restaurant for dinner: A 7.45 / B 8.00 / C 8.15"),field(4,"B","Italian border: A change trains / B go on a tour / C lunch in a café"),field(5,"C","Passengers must not: A eat own food / B open cabin window / C leave train before Italy")])
work13 += form(3, "MANHAM PORT — Choose A, B or C.", [field(1,"B","Why did the port develop? A safe from attack / B convenient river transport / C sea-coast position"),field(2,"B","Cause of expansion? A mining techniques / B demand for metals / C discovery of tin"),field(3,"A","Why send rocks away? A fuel shortage / B transport / C skills"),field(4,"A","When the port declined: A workers went away / B tourism grew / C fishing increased"),field(5,"C","The Trust hoped to: A close mines / B move harbour / C rebuild the port complex")])
work13 += form(4, "LONGFIELD PARK — Choose A, B or C.", [field(1,"C","Monday: A prepare food / B meet herbalist / C dye cloth with herbs"),field(2,"B","Wednesday: A groups only / B book in advance / C free"),field(3,"A","Saturday: A suitable clothing / B stay all day / C tell rangers activity beforehand")])
work13 += '''<details class="collapse answer-key-collapse"><summary>Đáp án, keyword table và vocabulary</summary><div class="collapse-body"><p><strong>Ex 1:</strong> Internet; restaurant; washing; lounge; manager.</p><p><strong>Ex 2:</strong> C, B, A, B, C. <strong>Ex 3:</strong> B, B, A, A, C. <strong>Ex 4:</strong> C, B, A.</p><h4>Task 1: Keyword table</h4><table><thead><tr><th>Part</th><th>Keywords in the questions</th><th>Similar words in the transcript</th></tr></thead><tbody><tr><td>1</td><td>has access to Internet</td><td>get onto the Internet</td></tr><tr><td>1</td><td>for first-class passengers only</td><td>is exclusive to first-class passengers</td></tr><tr><td>2</td><td>lock them away</td><td>keep them in the safe</td></tr><tr><td>2</td><td>go on a tour</td><td>have a look around</td></tr><tr><td>2</td><td>must not leave before Italy</td><td>don't get off until we reach the Italian border</td></tr><tr><td>3</td><td>convenient</td><td>handy</td></tr><tr><td>3</td><td>expansion</td><td>expanded</td></tr><tr><td>3</td><td>increase in demand for metals</td><td>a tremendous need for metals</td></tr><tr><td>3</td><td>sent away</td><td>shipped long distances</td></tr><tr><td>3</td><td>shortage of fuel</td><td>not enough coal</td></tr><tr><td>3</td><td>went away</td><td>emigrate out of the area</td></tr><tr><td>3</td><td>rebuild</td><td>reconstructing</td></tr><tr><td>4</td><td>dye cloth with herbs</td><td>using them as colour dyes for cloth</td></tr><tr><td>4</td><td>book in advance</td><td>phone the park ranger a few days ahead</td></tr><tr><td>4</td><td>come in suitable clothing</td><td>wear something you don't mind getting dirty or torn</td></tr></tbody></table><h4>Task 2: Vocabulary table</h4><table><thead><tr><th>Useful word / phrase</th><th>Type</th><th>Meaning</th><th>Sentence from the transcript</th></tr></thead><tbody><tr><td>exclusive</td><td>adjective</td><td>limited to a particular person or group; dành riêng</td><td>The lounge is exclusive to first-class passengers after 6 p.m.</td></tr><tr><td>safe</td><td>noun</td><td>a locked container for valuables; két an toàn</td><td>Keep passports in the safe in your cabin.</td></tr><tr><td>take advantage of</td><td>phrase</td><td>make good use of an opportunity; tận dụng</td><td>We will take advantage of the stop.</td></tr><tr><td>have a look around</td><td>phrase</td><td>visit and explore a place; tham quan</td><td>We have arranged time to have a look around.</td></tr><tr><td>emigrate</td><td>verb</td><td>leave one's country or area to live elsewhere; di cư</td><td>Thousands of workers were forced to emigrate.</td></tr><tr><td>fall into disrepair</td><td>phrase</td><td>become damaged through neglect; xuống cấp</td><td>The port buildings fell into disrepair.</td></tr><tr><td>set about V-ing</td><td>phrase</td><td>begin doing something with purpose; bắt tay vào</td><td>Professionals set about reconstructing it.</td></tr><tr><td>restoration</td><td>noun</td><td>returning something to an earlier condition; sự phục dựng</td><td>The results of this ambitious programme of restoration.</td></tr><tr><td>colour dye</td><td>noun</td><td>a substance used to colour material; thuốc nhuộm</td><td>Use herbs as colour dyes for cloth.</td></tr><tr><td>park ranger</td><td>noun</td><td>a person who protects and manages a park; kiểm lâm</td><td>Phone the park ranger a few days ahead.</td></tr></tbody></table></div></details>'''
shell(13, "[FOUNDATION B] LESSON 7 - CHALLENGE 1", source13, work13, "lesson-7-challenge-1.html")


t17_2 = '''Researcher: Hello, Joe, good to see you again.

Joe: Hi, you too.

R: So how did you get on with the devices we asked you to test for us?

J: Oh, fine. Well, mostly.

R: OK, well, we'll come back to those in a minute. First of all, I was wondering if I could ask you a few questions about your attitude to new electrical products. This will help us with future marketing. Is that OK?

J: Sure.

R: OK. First of all, how much do you spend on electronic items a month?

J: Hmm, let me see. I don't earn a lot, so I don't have much left after I've paid for things like rent, bills, food and so on. Anything else is a luxury. So, I'd guess about 5%, maybe 10% of my monthly salary.

R: All right, and what influences you in your choice of product? Say you wanted a new mobile phone, how would you decide which one to buy?

J: Well, first I look at reviews on the Internet, you know, what other customers think about them. Then I'll ask my friends what they think. In fact, their opinions are probably more important than anything.

R: How much does advertising help you choose a product?

J: I think that depends on how the product is advertised, and who is advertising it.

R: For example?

J: Well, if it's someone I respect, you know, like a famous sportsman or actor, that can certainly make a difference. I know it shouldn't really, but it does.

R: And where do you buy most of these products? The High Street? The Internet?

J: Most people seem to avoid shops these days, don't they, for things like that? They think they can get things cheaper on the Internet.

R: Right.

J: But I find that if you say to a shop assistant that you can get a new, er, camera for example, for £100 on the Internet, they'll often match the price. So, that's where I go.

R: Any other advantages?

J: Well, you get personal service and you don't have to wait for the product to be delivered. Ordering online means you have to wait, sometimes for ages, to get the things you've just bought. I hate that. I guess I'm just very impatient.

R: OK, one final question. Do you ever see a product and think, “I've absolutely got to get one of those”?

J: Oh, all the time, especially if I'm walking past a shop and I see a new electronic item in the window, especially if it's unusual, you know, something I've never seen before. It takes a lot of willpower.'''
t17_3 = '''Researcher: Right, Joe, let's move on. Now, we gave you three items to test for us. Let's start with the mobile phone.

Joe: OK, well, it has its good points and its bad points. The purple and silver make it quite eye-catching, you know, modern, exciting.

R: Right. Anything else?

J: Well, it's very small, isn't it? I know people say small is good, but in this case I think you might have gone too far.

R: In what way?

J: It can be a bit difficult to use, especially if you've got big hands like mine. You press one key, and you end up pressing another at the same time. On the other hand, thanks to the oval design, it does fit comfortably in your hand. Mobiles are usually sort of rectangular, aren't they? I think this is much better.

R: OK.

J: What else? When I was sending text messages, I had real problems seeing what I was writing. It's not that the screen was too small, just that it was a bit dark. If you're outside, you can hardly see anything on it.

R: We added a few things that you don't get on other mobiles. What did you think about those?

J: Ah, right, well, that noise it makes if you move away from it? That's really annoying. It's basically a good idea, but I think that after a while it would drive me mad.

R: So, probably wouldn't buy it?

J: Probably not. When I buy a mobile phone, I don't want one that's going to be difficult to operate. There's no point having a phone that looks good if you have to spend ages trying to make a call or send a text message. It's funny, but I find that more expensive mobile phones are more difficult to use than cheaper ones. It should be the other way round.

R: So keep it simple, right?

J: Right. And I want a phone that doesn't have problems picking up a signal, or doesn't cut you off halfway through a call. And all those games and other things you get on a mobile? I really can't see the point in those.

R: Fair point. Next, the digital radio. What did you think?

J: The audio quality was crisp and clear, even if you turned it up really loud. Some sound systems can sound a bit distorted at higher volumes, but not on this one. So 10 out of 10 for that.

R: Great.

J: The thing is, I'm not sure if it's the area I live in, but the choice of radio stations seemed very limited. It didn't make any difference what I did with the aerial or where I put the radio, high up on a shelf, low down on the floor. And there seemed to be a delay when you turned up the volume.

R: What do you mean?

J: Well, when you press the volume control, for example, nothing seems to happen for a few seconds. And the same thing happens when you want to change radio stations.

R: OK, the third item was the laptop computer. What's your opinion on that?

J: Oh, I really liked it. It's so small, so compact, but easy to use, I don't think you could make it smaller if you tried. But at £900, I'm not sure you'd get many customers. That's a lot of money for a laptop. Bring that down to, say, £400 and things might be different.

R: Any other changes you'd make? Like adding more memory, for example?

J: I think that's fine as it is. Three hundred gigabytes of memory is probably more than enough for most people. Oh, and incidentally, the way the keyboard folds out so that it's like a full-size one? That's really clever. But the computer doesn't have anywhere you can play CD-ROMs. And I'd include a light in the keyboard so you can use it when it's dark.

R: Well, thanks, Joe, for your comments. I think we ...'''
t17_4 = '''Hello, and thank you for asking me to your teachers' meeting to talk about the Dinosaur Museum and to tell you about your students there.

Well, let me give you some of the basic information first. In regard to opening hours, we're open every day of the week from 9.00 a.m. to 8.00 p.m. except on Mondays when we close at 1.30 p.m. And, in fact, the only day in the year when we're closed is on the 25th of December. You can book a guided tour for your school group any time that we're open.

If you bring a school group to the museum, when you arrive we ask you to remain with your group in the car park. One or more of the tour guides will welcome you there and brief you about what the tour will be about. We do this there because our entrance is quite small and we really haven't got much room for briefing groups in the exhibition area.

As far as the amount of time you'll need goes, if you bring a school group you should plan on allowing a minimum of 90 minutes for the visit. This allows 15 minutes to get on and off the coach, 45 minutes for the guided tour and 30 minutes for after-tour activities.

If you're going to have lunch at the museum you will, of course, have to allow more time. There are two cafés in the museum, with seating for 80 people. If you want to eat there you'll need to reserve some seating, as they can get quite crowded at lunchtime. Then outside the museum at the back there are tables, and students can bring their own lunch and eat it there in the open air.'''
t17_5 = '''When the students come into the museum foyer we ask them to check in their backpacks with their books, lunch boxes, etc., at the cloakroom before they enter the museum proper. I'm afraid in the past we have had a few things gone missing after school visits so this is a strict rule. Also, some of the exhibits are fragile and we don't want them to be accidentally knocked.

But we do provide school students with handouts with questions and quizzes on them. There's so much that students can learn in the museum and it's fun for them to have something to do. Of course they'll need to bring something to write with for these. We do allow students to take photographs. For students who are doing projects it's useful to make some kind of visual record of what they see that they can add to their reports. And finally, they should not bring anything to eat into the museum, or drinks of any kind.'''
t17_6 = '''There are also a few things the students can do after the tour. In the theatrette on the ground floor there are continuous screenings of short documentaries about dinosaurs which they can see at any time.

We used to have an activity room with more interactive things like making models of dinosaurs and drawing and painting pictures, even hunting for dinosaur eggs, but unfortunately the room was damaged in a bad storm recently when water came in the roof, so that's closed at the moment.

But we do have an IT centre where students have access to CD-ROMs with a range of dinosaur games. These games are a lot of fun, but they also teach the students about the lives of dinosaurs, how they found food, protected their habitat, survived threats, that kind of thing.

And I think that's all I have to tell you. Please feel free to ask any questions if you would like to know anything else.'''
source17 = '''<div class="audio-card"><h3>Exercise 1 (Pre-listening)</h3><p>Look at the sentences in Exercise 2 and decide whether each missing word is a noun, verb or adjective.</p></div>''' + track(2,"assets/bai-17/ex2.mp3",t17_2)+track(3,"assets/bai-17/ex3.mp3",t17_3)+track(4,"assets/bai-17/ex4.mp3",t17_4)+track(5,"assets/bai-17/ex5.mp3",t17_5)+track(6,"assets/bai-17/ex6.mp3",t17_6)
work17 = form(1,"Identify the missing word type.",[field(1,"noun","low …"),field(2,"noun","influenced by his …"),field(3,"adjective","somebody …"),field(4,"noun","from …"),field(5,"verb","doesn't like …"),field(6,"adjective","new and …")])
work17 += form(2,"Complete Questions 1–6. Write ONE WORD for each answer.",[field(1,"salary","Joe's low … does not allow many electronic goods."),field(2,"friends","He is often influenced by his …"),field(3,"famous","Advertisements featuring somebody …"),field(4,"shops","Joe prefers to get new products from …"),field(5,"waiting","He doesn't like … for a long time."),field(6,"unusual","He cannot resist products that are new and …")])
work17 += form(3,"Choose TWO letters for each question; enter both letters, e.g. AC.",[field(1,"AC|CA","Liked about phone: A colour, B size, C shape, D screen, E features"),field(2,"AD|DA","Looks for: A easy, B looks, C cheap, D reliable, E games"),field(3,"CE|EC","Radio problems: A sound, B volume, C stations, D position, E controls"),field(4,"BE|EB","Improve computer: A smaller, B price, C memory, D keyboard size, E features")])
work17 += form(4,"Complete the Dinosaur Museum sentences.",[field(1,"1.30 p.m.|1:30 p.m.","Museum closes at … on Mondays."),field(2,"25th December|25 December","Not open on …"),field(3,"car park","School groups are met in the …"),field(4,"90 minutes","Whole visit takes …"),field(5,"tables","There are … behind the museum for lunch.")])
work17 += form(5,"Choose THREE letters A–G; enter three letters.",[field(1,"CFG|CGF|FCG|FGC|GCF|GFC","What can students have? A food, B water, C cameras, D books, E bags, F pens, G worksheets")])
work17 += form(6,"Choose TWO letters A–E; enter both letters.",[field(1,"BE|EB","Activities available now: A models, B films, C drawing, D dinosaur eggs, E computer games")])
work17 += '''<details class="collapse answer-key-collapse"><summary>Đáp án, keyword table và vocabulary</summary><div class="collapse-body"><p><strong>Ex 1:</strong> noun, noun, adjective, noun, verb, adjective. <strong>Ex 2:</strong> salary, friends, famous, shops, waiting, unusual. <strong>Ex 3:</strong> AC, AD, CE, BE. <strong>Ex 4:</strong> 1.30 p.m.; 25th December; car park; 90 minutes; tables. <strong>Ex 5:</strong> C, F, G. <strong>Ex 6:</strong> B, E.</p><h4>Task 1: Keyword table</h4><table><thead><tr><th>Exercise</th><th>Keyword in question</th><th>Transcript expression</th></tr></thead><tbody><tr><td>2</td><td>low salary</td><td>I don't earn a lot; monthly salary</td></tr><tr><td>2</td><td>influenced by friends</td><td>their opinions are probably more important than anything</td></tr><tr><td>2</td><td>advertisements featuring somebody famous</td><td>a famous sportsman or actor advertising it</td></tr><tr><td>2</td><td>prefers shops</td><td>they will often match the price; that is where I go</td></tr><tr><td>2</td><td>doesn't like waiting</td><td>I am very impatient; wait for ages</td></tr><tr><td>2</td><td>new and unusual</td><td>something I have never seen before</td></tr><tr><td>3</td><td>liked colour</td><td>purple and silver make it eye-catching</td></tr><tr><td>3</td><td>liked shape</td><td>thanks to the oval design it fits comfortably</td></tr><tr><td>3</td><td>easy to use</td><td>not difficult to operate</td></tr><tr><td>3</td><td>reliable</td><td>doesn't cut you off halfway through a call</td></tr><tr><td>3</td><td>few radio stations</td><td>the choice of stations seemed very limited</td></tr><tr><td>3</td><td>controls did not work properly</td><td>there seemed to be a delay</td></tr><tr><td>3</td><td>reduce the price</td><td>bring that down to about £400</td></tr><tr><td>3</td><td>add more features</td><td>include a keyboard light and a CD-ROM drive</td></tr><tr><td>5</td><td>cameras</td><td>take photographs; make a visual record</td></tr><tr><td>5</td><td>pens</td><td>something to write with</td></tr><tr><td>5</td><td>worksheets</td><td>handouts with questions and quizzes</td></tr><tr><td>6</td><td>watch films</td><td>continuous screenings of short documentaries</td></tr><tr><td>6</td><td>play computer games</td><td>access to CD-ROMs with dinosaur games</td></tr></tbody></table><h4>Task 2: Vocabulary table</h4><table><thead><tr><th>Useful word / phrase</th><th>Type</th><th>Meaning</th><th>Transcript context</th></tr></thead><tbody><tr><td>wonder</td><td>verb</td><td>ask oneself; tự hỏi</td><td>I was wondering if I could ask a few questions.</td></tr><tr><td>match the price</td><td>phrase</td><td>offer the same price; bán bằng giá</td><td>The shop will often match the Internet price.</td></tr><tr><td>eye-catching</td><td>adjective</td><td>attracting attention; bắt mắt</td><td>Purple and silver make it eye-catching.</td></tr><tr><td>cut somebody off</td><td>phrasal verb</td><td>disconnect a call; làm gián đoạn cuộc gọi</td><td>A reliable phone does not cut you off.</td></tr><tr><td>see the point</td><td>phrase</td><td>understand the purpose; thấy được ích lợi</td><td>I cannot see the point in those games.</td></tr><tr><td>distorted</td><td>adjective</td><td>changed so it is unclear; bị méo</td><td>Some systems sound distorted at high volume.</td></tr><tr><td>compact</td><td>adjective</td><td>small and efficiently designed; nhỏ gọn</td><td>The laptop is compact but easy to use.</td></tr><tr><td>fold out</td><td>phrasal verb</td><td>open from a folded position; mở ra</td><td>The keyboard folds out to full size.</td></tr><tr><td>have access to</td><td>phrase</td><td>be able to use; có quyền truy cập</td><td>Students have access to CD-ROM games.</td></tr><tr><td>protect a habitat</td><td>phrase</td><td>keep an animal's environment safe; bảo vệ môi trường sống</td><td>The games teach how dinosaurs protected their habitat.</td></tr></tbody></table></div></details>'''
shell(17,"[FOUNDATION B] LESSON 9 - CHALLENGE 1",source17,work17,"lesson-9-challenge-1.html")


t24_1='''Hello, everyone, and welcome to our college Natural History Day. You've all got your programme for the day, but let me just give you a bit of information about your options for this morning's sessions, which begin at half past nine. Remember, you need to attend one of these sessions.

All right, your first choice is called “Dogs Might Fly”, which will take place in Room 27. Professor Keenan, who you may remember ran a workshop last year on how dinosaurs became extinct, will be giving a lecture on the evolution of animals. In particular, she'll be looking at how they may evolve in the future, and this will be followed by a group discussion where you'll get a chance to ask her questions and offer your own thoughts and opinions on this. So, if the evolution of animals is something you're interested in, head for Room 27.

We all know that animals communicate with each other, but what about flowers? Your second choice is a video presentation called “Flowers Talk”. This considers the possibility that plants and flowers do actually communicate with each other. The video is presented by Patrick Bell, who has just written a book on how plants adapt to their natural environment, so it should be very interesting. That will take place in the lecture room, no sorry, correct that, here in the main hall. We've had to move it because the lecture room is being renovated.

The third choice is ideal for those of you who want to get a bit of fresh air. We've called it “A World in Your Garden”, which we thought was appropriate as it looks at the sort of things you can find just by stepping out of your front door. Anyway, for those of you interested in getting away from the classroom, Doctor Watkins will be taking you on a nature walk through the local park, and will be telling you about some of the fascinating animals and plants that live and grow nearby. And it's a lovely day for a walk!

The final option, well you might want to avoid this one if you're frightened of things like snakes, as this is a hands-on workshop where you'll actually get a chance to handle these exotic creatures. It won't just be snakes, however. I believe Tom Howard, our resident reptile expert, has brought some other reptiles along for you to meet, including his pet tortoise, Reggie, who is over 100 years old, and a pet lizard he calls Arthur. So, if you want to meet Reggie and his other reptile friends, head on over to the Biology lab at 9.30. I'm sure you'll have a lot of fun. For those of you who don't usually use the Biology lab, could I remind you that you need to put on one of the white coats by the door before you go in.

OK, now, we've got some students here from Bardwell College who ...'''
t24_3='''OK, now, we've got some students here from Bardwell College who have joined us for today's events. Hello to you all, and welcome.

Now, before our day begins, you'll need to get a guest badge, which you'll have to wear while you're on the college premises. You can get these from the Administration Office. To get there from the Main Hall, leave the hall by the door opposite reception, turn left, and just follow the corridor to the end. The Administration Office is on your right. Don't go any further, or you'll be in the sports hall.

If you show your guest badge in the café, by the way, you'll get a 20% discount on drinks and sandwiches. To get there, from the Main Hall, walk along the corridor between the Main Hall and reception and turn right. The café is through the first door on your left. Directly opposite the café, on the same corridor, is the student common room, where you can go to relax and perhaps meet some of our own students.

If you have any valuables that you don't want to carry around with you, I suggest you put these in a locker. These are next to the sports hall, opposite the Administration Office. You can get a key for a locker when you get your guest badge from the Administration Office. And if you want to use our library, leave the common room and continue along the corridor; it is the large room marked on the plan.'''
t24_4='''Hello, I'm delighted to welcome you to our Wildlife Club, and very pleased that you're interested in the countryside and the plants and creatures of this area. I think you'll be surprised at the variety we have here, even though we're not far from London. I'll start by telling you about some of the parks and open spaces nearby.

One very pleasant place is Halland Common. This has been public land for hundreds of years, and what you'll find interesting is that the River Ouse, which flows into the sea eighty kilometres away, has its source in the common. There's an information board about the plants and animals you can see here, and by the way, the common is accessible 24 hours a day.

Then there's Holt Island, which is noted for its great range of trees. In the past willows were grown here commercially for basket-making, and this ancient craft has recently been reintroduced. The island is only open to the public from Friday to Sunday, because it's quite small, and if there were people around every day, much of the wildlife would be kept away.

From there it's just a short walk across the bridge to Longfield Country Park. Longfield has a modern replica of a farm from over two thousand years ago. Children's activities are often arranged there, like bread-making and face-painting. The park is only open during daylight hours, so bear that in mind if you decide to go there.'''
t24_5='''And finally I'd like to tell you about our new wildlife area, Hinchingbrooke Park, which will be opened to the public next month. This slide doesn't really indicate how big it is, but anyway, you can see the two gates into the park, and the main paths.

As you can see, there's a lake in the north-west of the park, with a bird hide to the west of it, at the end of a path. So it'll be a nice quiet place for watching the birds on the lake.

Fairly close to where refreshments are available, there's a dog-walking area in the southern part of the park, leading off from the path. And if you just want to sit and relax, you can go to the flower garden: that's the circular area on the map surrounded by paths.

And finally, there's a wooded area in the western section of the park, between two paths. Okay, that's enough from me, so let's go on to ...'''
source24 = track(1,"assets/bai-24/ex1.mp3",t24_1)+'''<div class="audio-card"><h3>Exercise 2</h3><p>Complete the route from the Main Hall to Room F before Exercise 3. Use the supplied campus plan below.</p><img class="content-graphic" src="assets/bai-24/college-plan.png" alt="Campus plan labelled A to K"></div>'''+track(3,"assets/bai-24/ex3.mp3",t24_3)+f'''<div class="audio-card"><h3>Exercise 4</h3><p class="audio-note">Bộ file được gửi không có MP3 riêng cho Exercise 4; transcript gốc vẫn được giữ đầy đủ bên dưới.</p>{transcript(t24_4)}</div><div class="audio-card"><h3>Exercise 5</h3><img class="content-graphic" src="assets/bai-24/park-map.png" alt="Hinchingbrooke Park map labelled A to I"><p class="audio-note">Bộ file được gửi không có MP3 riêng cho Exercise 5; transcript gốc vẫn được giữ đầy đủ bên dưới.</p>{transcript(t24_5)}</div>'''
work24 = form(1,"Complete the Natural History Day programme. Write NO MORE THAN TWO WORDS OR A NUMBER for each answer.",[field(1,"evolution","Dogs Might Fly — Animal …"),field(2,"group discussion","Type of event after the lecture"),field(3,"talk","Flowers might …"),field(4,"Main hall","Location of the video presentation"),field(5,"garden","A World in Your …"),field(6,"nature walk","Type of event in the local park"),field(7,"other reptiles","Snakes and …"),field(8,"Biology","Location of the hands-on workshop: … lab")])
work24 += form(2,"Complete the directions using: end, first, follow, leave, left, opposite, pass, right, second, turn.",[field(1,"leave","… the Main Hall by the door"),field(2,"opposite","… reception"),field(3,"turn","… left"),field(4,"follow","… the corridor"),field(5,"pass","… Room J"),field(6,"right","turn …"),field(7,"end","at the … of the corridor"),field(8,"left","turn …"),field(9,"first","through the … door"),field(10,"right","on the …")])
work24 += '''<figure class="content-figure"><img class="content-graphic" src="assets/bai-24/college-plan.png" alt="Campus plan labelled A to K"><figcaption>Use this plan for Exercise 3.</figcaption></figure>'''+form(3,"Label the plan. Choose the correct letter A–K for Questions 1–5.",[field(1,"D","Administration Office"),field(2,"E","Café"),field(3,"K","Student common room"),field(4,"C","Lockers"),field(5,"B","Library")])
work24 += form(4,"Complete the table.",[field(1,"trees","Holt Island: many different …"),field(2,"Friday","Open between … and Sunday"),field(3,"farm","Longfield: reconstruction of a 2,000-year-old …")])
work24 += '''<figure class="content-figure"><img class="content-graphic" src="assets/bai-24/park-map.png" alt="Hinchingbrooke Park map labelled A to I"><figcaption>Use this park map for Exercise 5.</figcaption></figure>'''+form(5,"Choose the correct answer from the list A–I.",[field(1,"A","Bird hide"),field(2,"I","Dog-walking area"),field(3,"F","Flower garden"),field(4,"E","Wooded area")])
work24 += '''<details class="collapse answer-key-collapse"><summary>Đáp án và vocabulary</summary><div class="collapse-body"><p><strong>Ex 1:</strong> evolution; group discussion; talk; Main Hall; garden; nature walk; other reptiles; Biology.</p><p><strong>Ex 2:</strong> leave, opposite, turn, follow, pass, right, end, left, first, right. <strong>Ex 3:</strong> D, E, K, C, B. <strong>Ex 4:</strong> trees, Friday, farm. <strong>Ex 5:</strong> A, I, F, E.</p><h4>Vocabulary table</h4><table><thead><tr><th>Useful word / phrase</th><th>Type</th><th>Meaning</th><th>Sentence from the transcript</th></tr></thead><tbody><tr><td>evolve</td><td>verb</td><td>develop gradually; tiến hóa</td><td>She will look at how animals may evolve in the future.</td></tr><tr><td>possibility</td><td>noun</td><td>something that may happen; khả năng</td><td>The video considers the possibility that plants communicate.</td></tr><tr><td>adapt to</td><td>verb phrase</td><td>change to suit new conditions; thích nghi</td><td>Plants adapt to their natural environment.</td></tr><tr><td>renovate</td><td>verb</td><td>repair and improve a building; cải tạo</td><td>The lecture room is being renovated.</td></tr><tr><td>sort</td><td>noun</td><td>a type or kind; loại</td><td>The sort of things found outside your front door.</td></tr><tr><td>exotic</td><td>adjective</td><td>unusual and from a distant place; kỳ lạ, ngoại lai</td><td>Students get a chance to handle exotic creatures.</td></tr><tr><td>hands-on</td><td>adjective</td><td>involving practical participation; thực hành</td><td>It is a hands-on workshop.</td></tr><tr><td>on the premises</td><td>phrase</td><td>within a building and its grounds; trong khuôn viên</td><td>Wear your guest badge on the college premises.</td></tr><tr><td>valuables</td><td>plural noun</td><td>valuable personal possessions; đồ có giá trị</td><td>Put valuables in a locker.</td></tr><tr><td>open space</td><td>noun phrase</td><td>an undeveloped outdoor area; không gian mở</td><td>Nearby parks and open spaces.</td></tr><tr><td>be noted for</td><td>phrase</td><td>be well known for; nổi tiếng về</td><td>Holt Island is noted for its range of trees.</td></tr><tr><td>replica</td><td>noun</td><td>an exact copy; bản sao mô phỏng</td><td>Longfield has a modern replica of a farm.</td></tr><tr><td>bear in mind</td><td>phrase</td><td>remember and consider; ghi nhớ</td><td>Bear the daylight opening hours in mind.</td></tr><tr><td>indicate</td><td>verb</td><td>show or point out; chỉ ra</td><td>The slide does not indicate how big the park is.</td></tr><tr><td>refreshments</td><td>plural noun</td><td>light food and drinks; đồ ăn nhẹ</td><td>The dog-walking area is close to refreshments.</td></tr></tbody></table></div></details>'''
shell(24,"[FOUNDATION B] LESSON 12 - CHALLENGE 1",source24,work24,"lesson-12-challenge-1.html")
