import os
import urllib.request
import re
import webbrowser

import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

load_dotenv()

# Extract all environmental functions
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_ID = os.getenv("WEATHER_APP_ID")


# Online functions using API
def find_my_ip():
    ipaddress = requests.get("https://api64.ipify.org?format=json").json()
    return ipaddress["ip"]


def wiki(query, no_of_sentences=3):
    """
        search the query on wikipedia and tell out the summary in given (no_of_sentences) no of lines.
    """
    try:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, no_of_sentences)
        # speak("According to Wikipedia")
        # speak(results)
        return results
    except Exception as e:
        print(e)
    return "None"


def find_link_youtube_video(data):
    d = data.split(" ")
    data = "+".join(d)

    search = "https://www.youtube.com/results?search_query=" + data
    html = urllib.request.urlopen(search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    final_link = "https://www.youtube.com/watch?v="
    final_link += video_ids[0]
    return final_link


def play_on_youtube(data):
    """
    This function will play music on YouTube using WebBrowser module.
    Args:
        data: name of music or the video name which you want to search on YouTube

    Returns:

    """
    final_link = find_link_youtube_video(data)
    webbrowser.open(final_link)


def search_on_google(query):
    kit.search(query)


def greetHelloInRandomLang():
    """
    Returns a string having random greeting message.
    Returns:
        string: greet message
    """
    try:
        response = requests.get("https://www.greetingsapi.com/random",timeout=5)
        json_data = response.json()
    # print(json_data)
        return json_data['greeting'] + "! That's hello in " + json_data["language"]
    except Exception as e:
        return "Namaste!, That's hello in Hindi"


def send_whatsapp_message(number, message):
    # make sure you logged in into your Whatsapp account on WhatsApp for Web
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(EMAIL,EMAIL_PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_latest_news():
    headlines = []
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = response["articles"]
    for article in articles:
        headlines.append(article["title"])

    return headlines[:5]


def get_weather_report(city):
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_ID}&units=metric").json()
    weather = response["weather"][0]["main"]
    temperature = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_joke():
    headers = {'Accept': 'application/json'}
    response = requests.get("https://icanhazdadjoke.com/",headers=headers).json()
    return response["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

