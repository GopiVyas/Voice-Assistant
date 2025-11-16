# 🗣️ Voice Assistant Web App (Flask + Python) -
This project is a simple Voice/Text Command Assistant built using Flask, Python, and pyttsx3 for text-to-speech.
The assistant can perform tasks like telling the time, opening Windows applications, launching websites, and performing Google searches.

# 🚀 Features -
✔️ Time Announcement

Asks the system time and speaks it out loud.
Example:
What is the time?

✔️ Open Installed Applications

Supports common Windows apps such as:

Calculator

Notepad

Paint

Command Prompt

Visual Studio Code

Google Chrome

Example:
Open notepad
Open chrome

✔️ Open Websites / Google Search

If the text is a website → opens directly
If not → performs a Google search

Example:

Open google.com

Open Facebook (performs search)

python flask tutorial (searches on Google)

✔️ Text-to-Speech Response

Every reply is spoken using pyttsx3.

# 📁 Project Structure -
project/
│── app.py
│── templates/
│     └── index.html
│── static/
│     └── (CSS/JS if needed)

# 🧠 How It Works -
🔹 execute_command(command)

Reads the user’s command and decides what action to perform:

Checks for time

Checks for open app

Checks for open website

Otherwise → performs Google search

🔹 talk(text)

Uses pyttsx3 to speak the response aloud.
