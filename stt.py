import whisper
#load the model - large-v2
model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/03_MySQL or Mongo dB.mp3",
                          language='hi',
                          task='translate')
#check the translate
print(result["text"])