# here I try to learn how to recognize my speech

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')

client = OpenAI()

audio_file= open("./speech_output_1.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcription.text)