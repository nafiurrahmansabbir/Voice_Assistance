import random
import pyttsx3
import wikipedia
import pyjokes

# Initialize the text-to-speech engine with female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choosing a female voice

# Function to greet the user
def greet():
    responses = ["Hello! How can I assist you today?",
                 "Hi there! What can I do for you?",
                 "Hey! How can I help you today?"]
    response = random.choice(responses)
    print(response)
    speak(response)

# Function to say the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle user commands
def handle_command(command):
    if "hello" in command:
        response = "Hello! Nice to see you."
        print(response)
        speak(response)
    elif "bye" in command:
        response = "Goodbye! Have a great day!"
        print(response)
        speak(response)
        return True  # Exiting the program
    elif "tell me about" in command:
        topic = command.replace("tell me about", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            print(summary)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            response = "There are multiple results for this query. Please be more specific."
            print(response)
            speak(response)
        except wikipedia.exceptions.PageError as e:
            response = "Sorry, I couldn't find any information about that."
            print(response)
            speak(response)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    else:
        response = "Sorry, I didn't understand that command. Can you please try again?"
        print(response)
        speak(response)

# Main function
def main():
    greet()
    while True:
        user_input = input("Your command: ").lower()
        if handle_command(user_input):
            break

if __name__ == "__main__":
    main()
