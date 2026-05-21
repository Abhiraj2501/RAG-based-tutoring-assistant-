import whisper
model = whisper.load_model("large-v2")

result = model.transcribe("audio = "audio/1.mp3")