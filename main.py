import os
import json
import openai
openai.my_api_key=json.loads(open("keys.json").read())['openaikey']
messages=[{"role":"system","content":"intelligent system"}]


