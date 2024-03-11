from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv('.env')

client = OpenAI() # defaults to getting the key using os.environ.get("OPENAI_API_KEY")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You're a human who engages in a conversation with me."},
    {"role": "user", "content": "Hi, how are you today?"}
  ]
)

print(completion.choices[0].message.content)