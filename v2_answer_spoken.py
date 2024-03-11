from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import pygame
import os

load_dotenv('.env')

client = OpenAI() # defaults to getting the key using os.environ.get("OPENAI_API_KEY")

user_input = str(input("Prompt:"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You're a human, not a computer. Answer like in a human conversiation, not like an assistant."},
    {"role": "user", "content": user_input}
  ]
)

gpt_answer = str(completion.choices[0].message.content)

speech_file_path = Path(__file__).parent / "speech_output.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input=gpt_answer
)

response.write_to_file(speech_file_path)

pygame.init()
pygame.mixer.music.load("speech_output.mp3")
pygame.mixer.music.play()

while True:
    if not pygame.mixer.music.get_busy():
      os.remove("speech_output.mp3")
      exit()