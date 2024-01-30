s = 'अरे, यह तो पाइथॉन का एक बुनियादी कोड है'
import gtts,playsound
tts = gtts.gTTS(s, lang='en')
tts.save('story.mp3')
playsound.playsound('story.mp3')
