# Jarvis-ai-in-desktop
# 🤖 Jarvis AI Assistant (Windows Version)

A simple voice-controlled AI assistant built using Python.
It can listen to your voice, respond using AI, open websites, play music, and more.

---

## 🚀 Features

* 🎤 Voice recognition (Speech-to-Text)
* 🔊 Text-to-Speech (Jarvis speaks back)
* 🌐 Open websites like YouTube, Google, Wikipedia
* 🎵 Play music from your system
* 🧠 AI-powered chat using OpenAI
* ⏰ Tell current time
* 📂 Save AI responses to files

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* OpenAI API
* OS & Webbrowser modules

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pyttsx3 SpeechRecognition openai pyaudio
```

### 4. Fix PyAudio (if error occurs)

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 Setup API Key

Create a file named `config.py` in your project folder:

```python
apikey = "your_openai_api_key_here"
```

---

## ▶️ Run the Project

```bash
python main.py
```

## 🗣️ Voice Commands

Try saying:

* "Open YouTube"
* "Open Google"
* "Open music"
* "What is the time"
* "Using artificial intelligence ..."
* "Jarvis quit"

---

## 📁 Project Structure

```
jarvis-ai/
│── main.py
│── config.py
│── Openai/        # Saved AI responses
│── README.md
```

---

## ⚠️ Important Notes

* Change music path in code:

```python
musicPath = "C:\\Users\\YourName\\Downloads\\song.mp3"
```

* Ensure microphone is working
* Internet is required for AI responses

---

## 🔮 Future Improvements

* Wake word detection ("Hey Jarvis")
* Open apps like VS Code, Chrome
* Play songs by voice
* GUI interface
* Memory-based conversations

---

## 🙌 Author

Rohit Kumar

---


