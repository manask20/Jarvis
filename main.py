from datetime import datetime
import time

import requests

from bot import wish_user, speak, takeCommand, BOT_NAME, USER_NAME, openProgram
from functions import online_ops, os_ops, offline_ops

if __name__ == '__main__':
    print("Hello World!")
    wish_user()
    while True:
        query = takeCommand().lower()
        print(query)

        if f"{BOT_NAME}" in query:
            query = query.replace(f"{BOT_NAME}", "")

        if "great me" in query or "wish me" in query:
            wish_user()

        elif "open" in query:
            openProgram(query)

        elif "search on google" in query:
            speak("what do you want to search on Google, Sir?")
            query = takeCommand().lower()
            online_ops.search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            online_ops.send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = takeCommand().capitalize()
            speak("What is the message sir?")
            message = takeCommand().capitalize()
            if online_ops.send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif "advice" in query:
            speak("Here's an advice for you, sir")
            advice = online_ops.get_random_advice()
            speak(advice)
            time.sleep(1)
            speak("For convenience, I am printing it on console")
            print(advice)

        elif "joke" in query:
            speak("Hope you like this one sir")
            joke = online_ops.get_random_joke()
            speak(joke)
            print(joke)

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            data = online_ops.wiki(query)
            if data == "None":
                speak("Sorry, but there is an Error printing it on Console")
            else:
                speak("According to wikipedia,")
                speak(data)

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(online_ops.get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*online_ops.get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = online_ops.find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = online_ops.get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")

        elif "screenshot" in query:
            if offline_ops.takeScreenShot():
                speak("Screenshot saved in image folder")
            else:
                speak("Sorry! printing the error on consol")

        elif "type here" in query:
            speak("What should I type here Sir?")
            data = takeCommand().capitalize()
            offline_ops.typeAnything(data)

        elif f"bye" in query or "good night" in query:
            hour = int(datetime.now().hour)
            if 6 < hour <= 19:
                speak("Bye Sir! Have a Good Day Sir.")
            else:
                speak("Good Night Sir!")
            break
