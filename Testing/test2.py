import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime

# Initialize the speech recognizer
listener = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index to change voices

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = None  # Initialize command variable with None
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            command = command.replace('alexa', '')
            print(command)
            # if 'alexa' in command:
            #     command = command.replace('alexa', '')
            #     print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')
    else:
        print("Didn't catch that. Please say the command again.")

while True:
    run_alexa()
