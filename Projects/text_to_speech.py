s = '''young boy named Liam. Liam was known throughout the village for his adventurous spirit and insatiable curiosity. He had explored every corner of the village, from the dense forests to the tranquil meadows. Yet, one place had always remained a mystery to him: the ancient, abandoned house at the edge of the village.

The house had a mysterious history. It was said to belong to an eccentric inventor who had vanished without a trace, leaving behind a wealth of strange contraptions and inventions. The villagers believed the house was haunted, and they avoided it at all costs.'''

import gtts,playsound

tts = gtts.gTTS(s, lang='en')
tts.save('story.mp3')

playsound.playsound('story.mp3')
