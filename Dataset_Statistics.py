import os
import librosa
import numpy as np

audio_folder = '/Users/rokos-basilisk/desktop/Ava/audio_clips'

# Get a list of audio files in the folder
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]  # Adjust the extension if needed

# Initialize lists to store durations and sample rates
durations = []
sample_rates = []

# Iterate over each audio file
for filename in audio_files:
    audio_path = os.path.join(audio_folder, filename)
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    durations.append(duration)
    sample_rates.append(sr)

# Print out statistics
print(f"Total audio files: {len(audio_files)}")
print(f"Average duration: {np.mean(durations):.2f} seconds")
print(f"Duration range: {np.min(durations):.2f} - {np.max(durations):.2f} seconds")
print(f"Sample rates: {set(sample_rates)}")

