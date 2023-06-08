import os
import json
import openai
openai.api_key=json.loads(open("keys.json").read())['openaikey']
messages=[{"role":"system","content":"intelligent system"}]
while(True):
    question=input("user: ").strip()
    if messages:
        messages.append({"role":"user","content":question})
        chat=openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=messages)
    answer=chat.choices[0].message.content
    print("AI: " + answer)
messages=[{"role":"system","content":answer}]




