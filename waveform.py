import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

audio_folder = 'audio_clips'

# Get a list of audio files
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]

# Visualize the first 3 audio files
for filename in audio_files[:3]:
    audio_path = os.path.join(audio_folder, filename)
    y, sr = librosa.load(audio_path, sr=None)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title(f'Waveform of {filename}')
    plt.tight_layout()
    plt.show()

