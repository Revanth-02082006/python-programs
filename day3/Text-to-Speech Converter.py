from gtts import gTTS
import os

text = "Hello, Revanth! Keep learning and coding."
speech = gTTS(text)
speech.save("speech.mp3")
os.system("start speech.mp3")
