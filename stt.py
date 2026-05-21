import whisper
model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audio/03.mp3",
                          language='hi',
                          task='translate')

print(result["text"])