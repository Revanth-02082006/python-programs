import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

command = recognizer.recognize_google(audio)
print(f"You said: {command}")
