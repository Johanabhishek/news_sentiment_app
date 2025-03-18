from tts import TTS

def text_to_speech(text, lang="hi"):
    tts = TTS("tts_models.hi.vits")  # Load Hindi TTS model
    tts.tts_to_file(text, "output.mp3")
    print("Speech saved as output.mp3")
