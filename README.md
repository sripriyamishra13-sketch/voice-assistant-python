# Advanced Python Voice Assistant 🎙️

## Overview

This project is an advanced modular voice assistant built in Python that demonstrates speech recognition, task automation, and extensible command handling.
It is designed as a resume-level project showcasing architecture design, API usage, and user interaction through voice commands.

The assistant listens to spoken commands, interprets intent, and performs actions such as:

* Providing weather updates
* Answering general knowledge questions
* Opening web pages
* Simulating smart home device control
* Executing customizable user-defined commands

---

## Features

### Speech Recognition

* Uses microphone input to capture voice commands
* Converts speech to text using Google Speech Recognition API

### Natural Language Routing

* Lightweight intent detection system
* Routes commands to appropriate modules

### Modular Architecture

Clean separation of functionality:

* `speech.py` → Input/Output handling
* `weather.py` → Weather API interaction
* `knowledge.py` → Wikipedia query engine
* `smarthome.py` → Smart device simulation

### Custom Commands

Users can define their own assistant responses via:

```
data/custom_commands.json
```

### API Integration

* Weather data from wttr.in
* Knowledge responses from Wikipedia

### Error Handling

* Handles speech recognition failures
* Safe fallback responses for unknown queries

---

## Project Structure

```
voice-assistant/
│
├── assistant.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│   ├── speech.py
│   ├── weather.py
│   ├── knowledge.py
│   ├── smarthome.py
│
└── data/
    └── custom_commands.json
```

---

## Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/sripriyamishra13-sketch/voice-assistant-python.git
cd voice-assistant
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Install PyAudio (Windows)

```
pip install pipwin
pipwin install pyaudio
```

---

## Running the Assistant

```
python assistant.py
```

Speak commands such as:

* "time"
* "open google"
* "weather"
* "turn on light"
* "who is Elon Musk"
* "exit"

---

## Future Enhancements

* Email sending automation
* Reminder scheduling
* Advanced NLP with spaCy
* ChatGPT integration
* GUI interface
* Real IoT device control

---

## Author
 **Sripriya Mishra**

Built as part of a Python Internship Project demonstrating applied AI and automation skills.




