import os
import librosa
import soundfile as sf


## Inconsistent Sample Rates ##

audio_folder = '/Users/rokos-basilisk/desktop/Ava/audio_clips'

#Get a list of audio files in the folder
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]

# Target sampling rate
target_sr = 22050

# Iterate over each audio file
for filename in audio_files:
    audio_path = os.path.join(audio_folder, filename)
    y, sr = librosa.load(audio_path, sr=None)
    if sr != target_sr:
        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        sf.write(audio_path, y_resampled, target_sr)
        print(f"Resampled {filename} to {target_sr} Hz")

