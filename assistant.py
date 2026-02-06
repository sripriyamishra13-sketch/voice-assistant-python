import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import requests

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen from microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except:
        speak("Sorry, I didn't understand")
        return ""

# Weather function
def get_weather(city="Bhubaneswar"):
    url = f"https://wttr.in/{city}?format=3"
    try:
        res = requests.get(url)
        speak(res.text)
    except:
        speak("Weather service unavailable")


# MAIN LOOP
speak("Voice assistant started")

while True:
    cmd = listen()

    if "time" in cmd:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "open google" in cmd:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "wikipedia" in cmd:
        topic = cmd.replace("wikipedia", "").strip()

        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        except wikipedia.exceptions.DisambiguationError as e:
            speak("Topic unclear. Showing first result.")
            result = wikipedia.summary(e.options[0], sentences=2)
            speak(result)

        except Exception:
            speak("Could not find information on Wikipedia.")

    elif "weather" in cmd:
        get_weather()

    elif "exit" in cmd:
        speak("Goodbye")
        break


