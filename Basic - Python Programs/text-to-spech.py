from gtts import gTTS    

def talkToMe(audio):
    tts = gTTS(text = audio)
    a = tts.save('audio.mp3')
    return a

audio = 'Hey, how are you?'
talkToMe(audio)