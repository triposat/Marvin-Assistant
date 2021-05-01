import datetime
from plyer import notification
import requests
import json
import time
from difflib import get_close_matches
from datetime import date
import wikipedia
import smtplib
import webbrowser
import os
import pyautogui
import random
import pyjokes
import psutil
book = json.load(open("ebooks.json"))
# Name of your friend and email, so that you can access him/her by name.
dict = {"name": "email", "name": "email"}


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        print("\n\t\tGood Morning My Dear")
        speak("Good Morning My Dear")
    elif hour >= 12 and hour < 17:
        print("\n\t\tGood Afternoon My Dear")
        speak("Good Afternoon my Dear")
    else:
        print("\n\t\tGood Evening My Dear")
        speak("Good Evening my Dear")
    speak("This Assistant is Made by satyam Tripathi")
    speak("I am your Personal assistant please tell me how may i help you")


def gjb(ema):
    a = dict[ema]
    return a


def teller(word):
    if word.lower() in book:
        return book[word]
    elif word.title() in book:
        return book[word.title()]
    elif word.upper() in book:
        return book[word.upper()]
    elif len(get_close_matches(word, book.keys())) > 0:
        notification.notify(title=f"Showing results for {get_close_matches(word, book.keys())[0].capitalize()}",
                            message=f"Search instead for {word.capitalize()}",
                            app_icon="C:/Users"
                                     "/Dell/Downloads/sear.ico", timeout=5)
        speak(
            f"Showing results for {get_close_matches(word, book.keys())[0].capitalize()}")
        time.sleep(2)
        return book[get_close_matches(word, book.keys())[0]]
    else:
        notification.notify(title="Error!, Word not found in the Dictionary",
                            message="Please Try again",
                            app_icon="C:/Users"
                                     "/Dell/Downloads/err.ico", timeout=7)
        speak("Error!! Word not found in the Dictionary")
        speak("Please Try again")
        exit()


if __name__ == '__main__':
    wishme()
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.ehlo()
    conn.starttls()
    conn.login("your email", "your password")  # Enter Your email and password
    while 1:
        query = input("\nWhat do you want to do: ").lower()
        if query.isnumeric():
            raise Exception("Here Numbers are not allowed!")
        elif 'wiki' in query:  # Like search: Bill Gates wikipedia
            print("Searching...")
            speak("According to wikipedia")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'youtube' in query:  # say youtube
            search = input("What do you Want to Search: ")
            speak("Searching in Youtube")
            webbrowser.open(
                'https://www.youtube.com/results?search_query='+search)
        elif 'time' in query:
            a = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time is : {a}")
            speak(f"time is {a}")
        elif 'date' in query:
            today = date.today()
            a = today.strftime('%B %d ,%y')
            print(f"Date is: {a}")
            speak(f"Todays date is: {a}")
        elif 'song' in query:
            # Whole path your Music folder, where your all musics consists.
            mus = "D:\\Musics & Videos\\Mp3 Musics"
            song = os.listdir(mus)
            os.startfile(os.path.join(mus, song[random.randint(1, 247)]))
        elif 'dev' in query:
            # Whole path of Dev Cpp in your computer.
            url = "C:\\Program Files\\Dev-Cpp\\devcpp.exe"
            speak("Opening DEV CPP")
            os.startfile(url)
        elif 'whatsapp' in query:
            # If your PC have Whatsapp installed, then give the complete path
            path = "C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("opening whatsapp")
            os.startfile(path)
        elif 'github' in query:  # Search for github
            speak('opening github')
            url = 'https://github.com'
            webbrowser.open(url)
        elif 'lin' in query:  # Searching for Linked-in
            speak('opening linkdin')
            url = 'https://www.linkedin.com'
            webbrowser.open(url)
        elif 'thank' in query:
            speak("Thanks for using me  Good Luck ")
            exit()
        elif 'mail' in query:
            send = input("Please enter the Name of the Person: ")
            sub = input("Write a Message: ")
            conn.sendmail("your email", f"{gjb(send)}", f"Subject: {sub}")
            print("Successfully Sent...")
            conn.quit()
        elif 'google' in query:  # Google Search, type Google then serach your items...
            sea = input("What do you want to Search : ")
            speak("Searching in google")
            webbrowser.open("https://www.google.com/search?q="+sea)
        elif 'battery' in query:  # Know the Battery of your system
            battery = psutil.sensors_battery()
            speak(f"Your Laptop Battery Percent is {battery.percent} Percent")
            print(f"Battery Percentage: {battery.percent}%")
        elif "joke" in query:  # For funny jokes, type joke
            a = pyjokes.get_joke()
            print(a)
            speak(a)
        elif "quit" in query:
            speak("Ok Sir I am Quiting Now ")
            quit()
        elif "write a note" in query:
            speak("WhaT Should I Write in the Note")
            a = input("Enter a Note:")
            file = open("notews.txt", 'a')
            time = datetime.datetime.now().strftime("%H:%M:%S")
            d = date.today()
            c = d.strftime("%d-%m-%y")
            file.write(f"Time: {time}, Date: {c}")
            file.write(", Message: ")
            file.write(a)
            file.write("\n")
            file.close()
            speak("Done Sir")
        elif "show note" in query:
            speak("Showing Sir")
            file = open("notews.txt", 'r')
            print(file.read())
            speak(file.read())
            file.close()
        elif "shot" in query:  # Want to take Screenshot, type shot
            img = pyautogui.screenshot()
            img.save("C:\\Users\\Dell\\Desktop\\Shotss.jpg")
        elif "corona" in query:
            r = requests.get(
                'https://coronavirus-19-api.herokuapp.com/countries').text.lower()
            Data = json.loads(r)
            x = input("Name of the Country: ")
            Result = [sub for sub in Data if sub['country'] == x]
            country = Result[0]['country']
            cases = Data[0]['cases']
            deaths = Data[0]['deaths']
            recovered = Data[0]['recovered']
            case = Result[0]['cases']
            today_cases = Result[0]['todaycases']
            death = Result[0]['deaths']
            today_death = Result[0]['todaydeaths']
            recover = Result[0]['recovered']
            Today_date = datetime.datetime.now().strftime("%d-%m-%y")
            Today_time = datetime.datetime.now().strftime("%H : %M : %S")
            notification.notify(title=f"Covid-19 Live Updates\tDate : {Today_date}\tTime - {Today_time}", message=f"\n\t   WORLD "
                                f"\nConfirmed Cases: {cases}\nDeaths: {deaths}\nRecovered: {recovered}\n\n\t    {country.upper()}\nConfirmed Cases: "
                                f" {case}\nTotal Deaths: {death}\nTotal Recovered: {recover}\nToday Cases: {today_cases}\nToday Deaths: {today_death}", app_icon="D:\All IN ONE\Programming Notes\Icons/vir.ico", timeout=10)
        elif "news" in query:
            url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=0864a52124954666bb3e1fd0f7fbb1e6"
            a = requests.get(url).text
            b = json.loads(a)
            c = b['articles']
            for article in c:
                notification.notify(title="Today's News Headlines", message=article['title'],
                                    app_icon="C:/Users"
                                             "/Dell/Downloads/news.ico", timeout=7)
                speak(article['title'])
                time.sleep(1)
                speak("Next")
        elif "where is" in query:
            query = query.replace("where is", "")  # Search your Location
            location = query
            webbrowser.open_new_tab(
                "https://www.google.com/maps/place/"+location)
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("restart /r /t 1")
        elif "meaning of" in query:
            query = query.replace("meaning of", "")
            word = query.capitalize()
            tran = teller(word)
            a = type(tran)
            if a == list:
                for i in tran:
                    notification.notify(title=f"Meaning of {get_close_matches(word, book.keys())[0].capitalize()} : ",
                                        message=f"{i}",
                                        app_icon="C:/Users"
                                                 "/Dell/Downloads/sear.ico", timeout=8)
                    speak(
                        f"Meaning of {get_close_matches(word, book.keys())[0].capitalize()}")
                    speak(f"{i}")
                    time.sleep(2)
                    break
            else:
                speak(f"Meaning of {word.capitalize()}")
                speak(f"{tran}")
                notification.notify(title=f"Meaning of {word.capitalize()} : ",
                                    message=f"{tran}",
                                    app_icon="C:/Users"
                                             "/Dell/Downloads/sear.ico", timeout=8)
