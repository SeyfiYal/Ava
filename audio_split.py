import os
import whisper
from pydub import AudioSegment

# Specify the path to your audio file
audio_file = "/Users/rokos-basilisk/desktop/AVA-Audio-Filesa/Ava-Data.m4a" 

# Load the Whisper model -- Tiny,Small,Large-- Depends I fast you wanna go
model = whisper.load_model("base")

# Transcribe the audio file with timestamps
result = model.transcribe(audio_file)

# Get the list of segments from the transcription
segments = result['segments']

# Load the audio file using pydub
audio = AudioSegment.from_file(audio_file)

# Create an output directory for the audio clips
output_folder = "audio_clips"
os.makedirs(output_folder, exist_ok=True)

# Iterate over each segment and export the corresponding audio clip
for i, segment in enumerate(segments):
    # Extract the start and end times in milliseconds
    start_time = int(segment['start'] * 1000)
    end_time = int(segment['end'] * 1000)

    # Extract the audio segment
    audio_segment = audio[start_time:end_time]

    # Generate a filename for the audio clip
    clip_filename = f"clip_{i+1:04d}.wav"
    clip_path = os.path.join(output_folder, clip_filename)

    # Export the audio clip
    audio_segment.export(clip_path, format="wav")

    # Optionally, print the transcription text
    print(f"Saved {clip_filename}: {segment['text'].strip()}")

