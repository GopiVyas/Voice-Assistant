from flask import Flask, render_template, request
import pyttsx3
import datetime
import webbrowser
import subprocess

app = Flask(__name__)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Common applications (update paths if needed)
apps = {
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "vs code": r"C:\Users\Gopi\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

def talk(text):
    """Speak out loud and return text"""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    return text

def execute_command(command):
    """Execute voice/text command"""
    command = command.lower()

    # --- Time ---
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return talk(f"The time is {now}")

    # --- Open applications ---
    if "open" in command:
        for name, path in apps.items():
            if name in command:
                talk(f"Opening {name}")
                subprocess.Popen(path, shell=True)
                return f"Opening {name}..."
        # If not an app, open website or perform a web search
        query = command.replace("open", "").strip()
        if "." in query or "com" in query:
            url = f"https://{query}"
        else:
            url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return talk(f"Searching {query} on the web")

    # --- Default search ---
    webbrowser.open(f"https://www.google.com/search?q={command}")
    return talk(f"Searching for {command} on Google")

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_command = request.form.get("command")
        if user_command:
            response = execute_command(user_command)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
