import pyttsx3
text = input("Enter text: ")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
