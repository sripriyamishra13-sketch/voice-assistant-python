import json
import datetime
import webbrowser

from modules.speech import speak, listen
from modules.weather import get_weather
from modules.knowledge import search
from modules.smarthome import control

# Load custom commands
with open("data/custom_commands.json") as f:
    custom = json.load(f)

def detect_intent(cmd):

    if cmd in custom:
        return "custom"

    if "time" in cmd:
        return "time"

    if "google" in cmd:
        return "browser"

    if "weather" in cmd:
        return "weather"

    if "turn" in cmd:
        return "device"

    if "exit" in cmd:
        return "exit"

    return "knowledge"


speak("Advanced assistant started")

while True:
    cmd = listen()

    intent = detect_intent(cmd)

    if intent == "custom":
        speak(custom[cmd])

    elif intent == "time":
        now = datetime.datetime.now().strftime("%H:%M")
        speak(now)

    elif intent == "browser":
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif intent == "weather":
        speak(get_weather())

    elif intent == "device":
        speak(control(cmd))

    elif intent == "knowledge":
        speak(search(cmd))

    elif intent == "exit":
        speak("Goodbye")
        break


