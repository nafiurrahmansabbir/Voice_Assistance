import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty('voice',voice[1].id)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

name = input("Enter name: ")
speak("Welcome back "+name)

