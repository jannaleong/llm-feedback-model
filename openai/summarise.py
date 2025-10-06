import os, re, datetime
from openai import OpenAI
import pandas as pd


client = OpenAI(
  api_key="API-KEY"
)

# data
feedback_1 = "Course difficulty will vary among professors. I took it with Sara Humphreys. I did not have much to take home from the lectures, and the assigned work felt made the course feel like a very upper year / graduate studies course. Dropped and retook it online with Randy Harris and not only was the course assignment less painful, I also learned more and had a very enjoyable time."
feedback_2 = "Not a hard course if you go to class and listen to the prof( Bill Bishop). Too many slides to cram, but they are a strong resource, especially if you annotate them during lectures. Plenty of past midterms and exams but don't expect a really high mark just from those. A lot of content that can be dry at times, but overall an enjoyable course. Labs are very long and can go wrong just about anywhere if not set up properly so get help from the TA's while you can."
feedback_3 = "Like state previously, he is a bad teacher but a nice person. He means well, but his lectures make no sense at all. I took him for both acct classes and did not learn a single thing. His lectures relate to nothing to accounting and they are a waste of time to go to. Everything is online and open book, open notes and easy grading."
feedback_4 = "ULTRA BORING! dont even register unless you know you want to be bored out of your mind. The class does not seem that hard, but the readings are dumb hard to understand and he sounds so uninterested in the class. oh and he says right at the end of each sentence. so annoying"
feedback_5 = "Professor Lawton explains things well and shows why they matter in real life. He did a great job making complicated concepts seem simple. He assigns a lot of homework, but not more than any other college-level calculus class."
feedback_6 = "Professor Marney is great! She gave me a lot of help on my papers and was willing to work with me when I had to miss class because of a long illness. She is nice and her class is really interesting. If you can take her class, you should."
feedback_7 = "The most useless course I've ever taken. The standards for the assignments are ridiculously low. You'd think in a design class, you'd learn how to design / plan / implement projects were economically or, at very least, physically feasible, but that really wasn't the case. Many of the groups that retrieved high marks had issues with hindering their entire designs on technologies that did not yet exist, were clearly economically unfeasible, or didn't really solve the problem they were tasked to solve. The first two out of three major projects were designing a poster and re-design of a room/ space. The course really wasn't challenging, didn't introduce any novel material about design or design strategies, and no real concern seemed to go towards the viability of designs / solutions."
feedback_8 = "If you've done AP or IB physics in high school, this shouldn't be too bad. Understanding the concepts is absolutely essential: if you just try to memorize problems or equations, you will fail."
feedback_9 = "Great Professor! Content is really interesting and he is very enthusiastic about what he teaches! Gives plenty of opportunities for participation!"
feedback_10 = "Arrogant , inconsiderate , and unreasonable. For a professor teaching argumentation, Zunic employs textbook fallacies against his own students. Assignment expectations are vague and understated, marks aggressively like he has a personal vendetta with his students, and will not , under any circumstance , yield to alternative justified reasoning. Everything besides his opinions is wrong and irrelevant in his eyes. For any student taking this course outside of their major as an elective, your intelligence will be shamed and disregarded in favor of the subjective flavor of common sense the professor employs. A near unwavering offline class consensus was reached on the disapproval of this professor. However, the course itself is somewhat useful in all real-life forms of communication, so I recommend it but stay away from this prof."
feedback_11 = "The lecutres were alright"
feedback_12 = "I think the course was okay"
feedback_13 = "The prof was interesting I guess"
feedback_14 = "The prof was interesting I guess"
feedback_15 = "I think the course was okay"
feedback_16 = "I think professor Sam was a great teacher. He was able to teach us the materials in a clear and concise way. I would say one feedback I have is increase the security of graded quizzes as there is a loophole that makes it easy to cheat."

feedbacks = [
    feedback_1, feedback_2, feedback_3, feedback_4,
    feedback_5, feedback_6, feedback_7, feedback_8,
    feedback_9, feedback_10, feedback_11, feedback_12,
    feedback_13, feedback_14, feedback_15, feedback_16,
]

# prompt types
prompt_5feedback = (
    f"Summarise the feedback given by 5 students about a university course. "
    f"Feedback 1: {feedback_1}\n"
    f"Feedback 2: {feedback_2}\n"
    f"Feedback 3: {feedback_3}\n"
    f"Feedback 4: {feedback_4}\n"
    f"Feedback 5: {feedback_5}\n"
)
prompt_100feedback = "Summarise the feedback given by 100 students about a university course.\n"
for i in range(1, 101):
    if i == 64:
        text = feedbacks[15]   
    else:
        text = feedbacks[(i - 1) % len(feedbacks)]  
    prompt_100feedback += f"Feedback {i}: {text}\n"
prompt_to_send = prompt_5feedback  

# connect to gpt api
resp = client.responses.create(
    model="gpt-5",
    input=prompt_to_send,
    store=True,
)

# save response to excel
response_text = getattr(resp, "output_text", None)
if not response_text:
    response_text = resp.output[0].content[0].text

row = {
    "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
    "prompt": prompt_to_send,
    "response": response_text,
}
xlsx_path = "runs.xlsx"

if os.path.exists(xlsx_path):
    existing = pd.read_excel(xlsx_path)
    df = pd.concat([existing, pd.DataFrame([row])], ignore_index=True)
else:
    df = pd.DataFrame([row])

df.to_excel(xlsx_path, index=False) 
print(f"Saved to {xlsx_path}")