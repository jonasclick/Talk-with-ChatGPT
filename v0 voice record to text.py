# here I try to learn how to recognize my speech
from dotenv import load_dotenv
from pvrecorder import PvRecorder
import wave, struct 
from openai import OpenAI

load_dotenv('.env')


## Find out what index your deisred microphone has.
# for index, device in enumerate(PvRecorder.get_available_devices()):
#     print(f"[{index}] {device}")


## Record my prompt.
recorder = PvRecorder(device_index=0, frame_length=512) #(32 milliseconds of 16 kHz audio)
audio = []
path = 'promt_recording.wav'

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


## Send my prompt to OpenAI for transcription.
client = OpenAI()

audio_file= open("promt_recording.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcription.text)


## Yeah, this works.