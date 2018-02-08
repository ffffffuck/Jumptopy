from gtts import gTTS

def speaker(a):
    tts = gTTS(text=a, lang='ko')
    tts.save("test.mp3")

    open("test.mp3")


speaker("안녕하세요")