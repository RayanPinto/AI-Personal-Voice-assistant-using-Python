import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import requests

print('Loading your AI personal assistant - G One')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Jarvis")
wishMe()

if __name__ == '__main__':
    assistant_active = False  # Flag to control the assistant

    while True:
        if assistant_active:
            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            if statement == 0:
                continue

            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('Your personal assistant Jarvis is shutting down, Goodbye.')
                print('Your personal assistant Jarvis is shutting down, Goodbye.')
                assistant_active = False  # Deactivate assistant
                continue  # Wait for reactivation

            if 'start' in statement:
                assistant_active = True
                speak("Assistant is now active again.")
                print("Assistant is now active again.")
                continue

            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("YouTube is open now")
                time.sleep(5)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google Chrome is open now")
                time.sleep(5)
            elif 'open chat box' in statement:
                webbrowser.open_new_tab("window.location.href='index04.html'")
                
            elif 'open quiz' in statement:
                webbrowser.open_new_tab("window.location.href='index05.html'")
            elif 'speech' in statement:
                webbrowser.open_new_tab("window.location.href='index03.html'")
            elif 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif "who are you" in statement or "what can you do" in statement:
                speak("I am G-One version 1.0, your personal assistant. I can help with various tasks like opening websites, checking weather, and answering questions.")

            elif "camera" in statement or "take a photo" in statement:
                ec.capture(0, "robo camera", "img.jpg")

            elif 'ask' in statement:
                speak('What would you like to ask?')
                question = takeCommand()
                app_id = "R2K75H-7ELALHR35X"
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

        else:
            # Assistant is inactive
            speak("Your assistant is currently inactive. Say 'start' to activate it.")
            statement = takeCommand().lower()

            if "start" in statement:
                assistant_active = True
                speak("Assistant is now active.")
                print("Assistant is now active.")
                continue

            elif "stop" in statement:
                speak("Your assistant is already inactive.")
                print("Assistant is already inactive.")
                continue
            elif "close" in statement:
                speak("shutting down")
                break