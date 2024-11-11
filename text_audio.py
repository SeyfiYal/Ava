import speech_recognition as sr
import os

recognizer = sr.Recognizer()
audio_folder = '/Users/rokos-basilisk/desktop/Ava/audio_clips'
transcripts = []

for filename in os.listdir(audio_folder):
    if filename.endswith('.wav'):
        audio_path = os.path.join(audio_folder, filename)
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            transcripts.append(f"{filename}|{text}")
            print(f"Transcribed {filename}: {text}")
        except sr.UnknownValueError:
            print(f"Could not understand audio {filename}")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Save transcripts to file
with open('transcripts.txt', 'w') as f:
    for line in transcripts:
        f.write(line + '\n')

