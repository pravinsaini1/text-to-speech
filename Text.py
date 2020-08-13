from gtts import gTTS
import os
mytext = 'Convert this Text to Speech in Python'
language = 'en'
output = gTTS(text=mytext, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")