import os
import time
from datetime import datetime
import speech_recognition as sr
from functions import online_ops, os_ops
import utils
import random
import pyautogui as pg

import pyttsx3
from dotenv import load_dotenv

load_dotenv()  # loading .env file

# Extracting the variables from .env file
USER_NAME = os.getenv('USER')
BOT_NAME = os.getenv('BOT_NAME')

engine = pyttsx3.init('sapi5')  # Sapi5 is a Microsoft API
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set Male Voice
engine.setProperty("rate", 178)  # Slow the rate of speech
engine.setProperty('volume', 1.0)  # Set Volume


def speak(audio):
    """Used to speak whatever text (audio) is passed to it"""
    engine.say(audio)
    engine.runAndWait()


def wish_user():
    """
    Wish the user (Good Morning, Good evening...) according to time.
    Returns:
    """
    speak(online_ops.greetHelloInRandomLang())
    hour = int(datetime.now().hour)
    if 6 <= hour < 12:
        speak(f"Good Morning {USER_NAME}")

    elif 12 <= hour < 16:
        speak(f"Good afternoon {USER_NAME}")

    elif 16 <= hour < 19:
        speak(f"Good Evening {USER_NAME}")

    speak(f"I am {BOT_NAME} Sir. Please tell me how may I help you?")
    return


def echoMode():    # speak what he listens
    speak("Echo Mode On!")
    query = takeCommand()
    while not "echo mode off" in query:
        speak(query)
        query = takeCommand()

    speak("Echo Mode Off!")
    return


def takeCommand():
    """
    It takes microphone input from the User, recognizes it using Speech Recognition module
    Returns:
        string: convert speech to text and return text as string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # Use Google speech recognition API
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        # print(e) # You Can print the error
        print("Say that again please...")
        return "None"


def openProgram(query):
    text = utils.opening_text[random.randrange(0,len(utils.opening_text))]
    speak(text)
    if "open youtube" in query:
        speak('What do you want to play on Youtube, sir?')
        data = takeCommand().lower()
        online_ops.play_on_youtube(data)

    elif "open command prompt" in query or "open cmd" in query :
        os_ops.open_cmd()

    elif "open camera" in query:
        os_ops.open_camera()

    elif os_ops.open_path(query.replace("open ", "")):
        pass

    else:
        pg.press('win')
        time.sleep(0.2)
        pg.write(query.replace('open ', ""))
        time.sleep(0.2)
        pg.press('enter')

