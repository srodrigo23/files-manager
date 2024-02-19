from pydub import AudioSegment

# Load audio files
audio1 = AudioSegment.from_file("scripts/audio/PTT-20200102-WA0002.opus")
audio2 = AudioSegment.from_file("scripts/audio/PTT-20200102-WA0004.opus")

# Join audio files
combined_audio = audio1 + audio2

# Export the combined audio as a new file
combined_audio.export("scripts/audio/combined.mp3", format="mp3")