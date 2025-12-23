from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess
import os
import pyjokes

app = Flask(__name__)

def talk(text):
    """Speaks the text and returns it to be displayed on the UI."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop() # Ensures the engine loop is cleared
    return text

def execute_logic(command):
    """Processes the user command and returns the assistant's response."""
    command = command.lower()
    
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return talk(f"The time is {now}")

    elif "joke" in command:
        return talk(pyjokes.get_joke())

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return talk("Opening YouTube")
    
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return talk("Opening Google")

    elif "open" in command:
        apps = {
            "calculator": "calc.exe",
            "notepad": "notepad.exe",
            "paint": "mspaint.exe"
        }
        for name, path in apps.items():
            if name in command:
                subprocess.Popen(path, shell=True)
                return talk(f"Opening {name}")
        
        query = command.replace("open", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return talk(f"Searching for {query}")

    else:
        webbrowser.open(f"https://www.google.com/search?q={command}")
        return talk(f"Searching Google for {command}")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_command = request.form.get("command")
        if user_command:
            response_text = execute_logic(user_command)
    return render_template("index1.html", response=response_text)

@app.route("/listen", methods=["POST"])
def listen_via_mic():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            res = execute_logic(command) # Captured spoken text
            return jsonify({
                "status": "success", 
                "command": command, 
                "response": res # Sent back to JavaScript
            })
    except Exception as e:
        return jsonify({"status": "error", "message": "Could not hear you."})

if __name__ == "__main__":
    app.run(debug=False)
