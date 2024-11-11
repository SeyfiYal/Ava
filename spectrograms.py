import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display


audio_folder = '/Users/rokos-basilisk/desktop/Ava/audio_clips' 
# Get a list of audio files in the folder
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]  # Adjust the extension if necessary



for filename in audio_files[:3]:
    audio_path = os.path.join(audio_folder, filename)
    y, sr = librosa.load(audio_path, sr=None)
    # Compute spectrogram
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    # Display spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz', cmap='viridis')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram of {filename}')
    plt.tight_layout()
    plt.show()

