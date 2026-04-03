import speech_recognition as sr
import os
import webbrowser
from openai import OpenAI
from config import apikey
import datetime
import random
import pyttsx3

# Initialize TTS (Windows)
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

# OpenAI client (NEW API)
client = OpenAI(api_key=apikey)

chatStr = ""

def chat(query):
    global chatStr
    chatStr += f"User: {query}\nAssistant: "

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": chatStr}
            ]
        )

        reply = response.choices[0].message.content
        say(reply)
        chatStr += reply + "\n"
        return reply

    except Exception as e:
        print("Error:", e)
        return "Sorry, something went wrong"

def ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        text = response.choices[0].message.content

        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        filename = f"Openai/{random.randint(1,9999)}.txt"
        with open(filename, "w") as f:
            f.write(text)

    except Exception as e:
        print("Error:", e)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return ""

# ================= MAIN =================
if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A I")

    while True:
        query = takeCommand().lower()

        if not query:
            continue

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        # 🎵 Play music (Windows path)
        if "open music" in query:
            musicPath = "C:\\Users\\rohit\\Downloads\\song.mp3"   # CHANGE THIS
            os.startfile(musicPath)

        elif "time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Time is {hour} {minute}")

        elif "open notepad" in query:
            os.system("notepad")

        elif "open chrome" in query:
            os.system("start chrome")

        elif "using artificial intelligence" in query:
            ai(prompt=query)

        elif "jarvis quit" in query:
            say("Goodbye")
            break

        elif "reset chat" in query:
            chatStr = ""

        else:
            chat(query)