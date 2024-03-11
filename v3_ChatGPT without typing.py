from dotenv import load_dotenv
from pvrecorder import PvRecorder
from openai import OpenAI
from pathlib import Path
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import wave, struct

load_dotenv('.env')

## Record my spoken prompt.
recorder = PvRecorder(device_index=0, frame_length=512) #(32 milliseconds of 16 kHz audio)
audio = []
path = 'audio_prompt.wav'

try:
    recorder.start()


    while True:
        frame = recorder.read()
        audio.extend(frame)
except KeyboardInterrupt:
    recorder.stop()
    with wave.open(path, 'w') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))
finally:
    recorder.delete()


## Send my audio_prompt to OpenAI for transcription.
client = OpenAI() # defaults to getting the key using os.environ.get("OPENAI_API_KEY")

audio_file= open("audio_prompt.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

transcribed_prompt = transcription.text

## Send my transcribed_prompt to OpenAI for a GPT_answer.  
client = OpenAI() # do I need this a second time????

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You're a human, not a computer. Answer like in a human conversiation, not like an assistant."},
    {"role": "user", "content": transcribed_prompt}
  ]
)

gpt_answer = str(completion.choices[0].message.content)


## Send the gpt_answer back to OpenAI for speech_output
speech_file_path = Path(__file__).parent / "speech_output.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input=gpt_answer
)

response.write_to_file(speech_file_path)


## Read out the answer and delete the audio files.
pygame.init()
pygame.mixer.music.load("speech_output.mp3")
pygame.mixer.music.play()

while True:
    if not pygame.mixer.music.get_busy():
      os.remove("audio_prompt.wav")
      os.remove("speech_output.mp3")
      exit()