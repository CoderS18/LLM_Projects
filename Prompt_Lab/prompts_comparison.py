import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_API_KEY"),
)

def ask(prompt,temperature=0.3):
    #call through API to check different responses based on different prompting styles.
    r = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        max_tokens=200,
        temperature=temperature,
        messages=[{"role":"user","content":prompt}]
    )

    return r.choices[0].message.content

#Zero shot
zero_shot= '''
Classify sentiment: Positive, Negative, or Neutral.
Text: "{text}"
Sentiment:'''

#print("Check zero shot:", ask(zero_shot))

#Few shot 
few_shot = '''
Classify sentiment: Positive, Negative, or Neutral.

Text: "I love it!"       -> Positive
Text: "Worst ever."      -> Negative
Text: "It arrived."      -> Neutral

Text: "{text}" -> '''

#print("Check few shot:",ask(few_shot))

#Chain of Thought
cot = '''
Classify the sentiment of this text. Think step by step.

Text: "{text}"

Steps:
1. What emotion is expressed?
2. Is it positive, negative, or neutral?
3. Final answer: '''


#Compare all side by side
tasks = [
    "The service was slow but the food was amazing.",
    "Meh, nothing special.",
    "I cannot believe how bad this was!"
]

for task in tasks:
    print(f"\nText: {task}")
    print(f"  Zero-shot: {ask(f'Classify: {task} -> ')}")
    print(f"  Few-shot:  {ask(few_shot.format(text=task))}")
    print(f"  Chain of Out: {ask(cot.format(text=task))}")

