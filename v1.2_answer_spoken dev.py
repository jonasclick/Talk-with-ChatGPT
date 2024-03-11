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

print("Request sent.")

print(completion.choices[0].message.content)

print("Answer received.")

gpt_answer = str(completion.choices[0].message.content)

speech_file_path = Path(__file__).parent / "speech_output.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input=gpt_answer
)

response.write_to_file(speech_file_path)

print("Audio file created.")

pygame.init()
pygame.mixer.music.load("/Users/jonas/JONAS VETSCH/2_PRIVAT/5_Projekte/Coding Projects 2024/GPT Coding Interface/speech_output.mp3")
pygame.mixer.music.play()

print("Playback started.")

while True:
    if not pygame.mixer.music.get_busy():
      print("Playback ended. Shutting down.")
      os.remove("speech_output.mp3")
      exit()