import random
import pyttsx3
import wikipedia
import pyjokes
import tkinter as tk

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
    add_response(response)
    speak(response)

# Function to say the text
def speak(text):
    
    engine.say(text)
    engine.runAndWait()
    

# Function to add a response to the text widget
def add_response(response):
    response_text.config(state=tk.NORMAL)
    response_text.insert(tk.END, response + '\n\n')
    response_text.config(state=tk.DISABLED)
    response_text.see(tk.END)  # Scroll to the end

# Function to handle user commands
def handle_command(command):
    if "hello" in command:
        response = "Hello! Nice to see you."
    elif "bye" in command:
        response = "Goodbye! Have a great day!"
        root.destroy()  # Exiting the program
    elif "tell me about" in command:
        topic = command.replace("tell me about", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            response = summary
        except wikipedia.exceptions.DisambiguationError as e:
            response = "There are multiple results for this query. Please be more specific."
        except wikipedia.exceptions.PageError as e:
            response = "Sorry, I couldn't find any information about that."
    elif "joke" in command:
        joke = pyjokes.get_joke()
        response = joke
    else:
        response = "Sorry, I didn't understand that command. Can you please try again?"
    
    add_response(response)
    speak(response)

# Function to handle button click event
def on_button_click():
    user_input = command_entry.get().lower()
    command_entry.delete(0, tk.END)
    handle_command(user_input)

# Main function
def main():
    greet()

# Create the main window
root = tk.Tk()
root.title("Text Assistant")

# Create and configure widgets
response_text = tk.Text(root, width=50, height=20, wrap=tk.WORD, state=tk.DISABLED)
response_text.pack(pady=10)

command_entry = tk.Entry(root, width=40)
command_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_button_click)
submit_button.pack(pady=5)

# Call the main function
main()

# Start the Tkinter event loop
root.mainloop()
