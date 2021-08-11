from pushbullet import PushBullet  # pip install pushbullet.py==0.9.1
from pytube import YouTube  # pip install pytube
import cv2  # pip install opencv-python
import winshell  # pip install winshell
import pytube  # pip install pytube
from pathlib import Path
import sqlalchemy as db  # pip install SQLAlchemy
from spellchecker import SpellChecker  # pip install pyspellchecker
import wikipedia  # pip install wikipedia
import webbrowser  # pip install webbrowser
import pyjokes  # pip install pyjokes
import psutil  # pip install psutil
import yagmail  # pip install yagmail
from pywebio.input import *  # pip install pywebio
from pywebio.output import *
from pywebio.session import *
import requests
import re
import os
import datetime
from datetime import date
from difflib import get_close_matches
import time
import math
import urllib.request
import json

os.chdir(r"C:\Users\Dell\Desktop")

spell = SpellChecker()

yag = yagmail.SMTP("satyampsit244@gmail.com")  # Making email server using SMTP

# For checking the email in a text, or check whether the mail is correct or not
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# For checking the URL, whether it's right or not!
regex_1 = ("((http|https)://)(www.)?" +
           "[a-zA-Z0-9@:%._\\+~#?&//=]" +
           "{2,256}\\.[a-z]" +
           "{2,6}\\b([-a-zA-Z0-9@:%" +
           "._\\+~#?&//=]*)")

command_list = ["root", "%", "prod", 'add', 'sum', 'difference', 'subtract', 'product',
                'multiply', 'divide', 'sin', 'cos', 'tan', 'sqrt', 'square root', "sub", "diff", "mul", "div", "addition"]
commands = re.compile("|".join(command_list), re.IGNORECASE)

Pattern_1 = re.compile(regex_1)

# For extracting the current weather data
api_key = "88d279a5ff5fcd8e338ab42d94c819c3"

# URL for the weaher data
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# API key for sending push notification to the phone
access_token = "o.aJXLlYcxqUAyvZZLzGDdUQYWxwDNbhYw"

# JSON file for finding the meanings of the word
book = json.load(open(r"C:\Users\Dell\Desktop\ebooks.json"))

# Creating a database for storing our notes
'''Our database has three columns. They are,
        Time - Stores the time of the creation of the note (unique)
        Title - Stores the title of the note (unique)
        Note - Stores the note, that we have entered'''

engine = db.create_engine('sqlite:///notes.db')
metadata = db.MetaData()
notes = db.Table('notes', metadata, db.Column('Time', db.String(255), nullable=False, primary_key=True), db.Column(
    'Title', db.Text(), nullable=False, primary_key=True), db.Column('Note', db.Text(), default=''))
metadata.create_all(engine)

# Add two numbers


def addNumbers(list):
    sum = 0
    for i in list:
        sum += i
    return sum

# Subtract two numbers


def diffNumbers(a, b): return b-a

# Multiply two numbers


def multiplyNumbers(list):
    prod = 1
    for i in list:
        prod *= i
    return prod

# Divide two numbers


def divideNumbers(a, b):
    return a/b


def toRadians(degree):
    return math.radians(degree)


# For showing the weather image
def weathy():
    put_html("<p align=""left""><h4><img src=""https://icons.iconarchive.com/icons/pixelkit/flat-jewels/128/Weather-icon.png"" width=""28px""> Weather Forecast</h4></p>")

# Checking whether the name of the city exists or not


def Check_weath(City):
    complete_url = f"{base_url}appid={api_key}&q={City}"
    response = requests.get(complete_url)
    temp = response.json()
    if temp["cod"] == "404":
        return "City not found, Try searching..."
    return None

# For showing the loading bar


def circ():
    put_html("<p align=""center""><img src=""https://media.tenor.com/images/ed2c4fc16fcd23c5ad71cd8e802cd9a1/tenor.gif"" width=""90px""></p>")
    time.sleep(3)
# For showing the loading bar


def Bar():
    put_html("<p align=""center""><img src=""https://media.tenor.com/images/0d34378f630afe43f7ed93f8341d7d77/tenor.gif"" width=""120px""></p>")
    time.sleep(1)

# For showing the loading bar


def progress():
    put_html("<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
    time.sleep(2)
    clear()

# For showing the loading bar


def progresses():
    put_html("<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
    time.sleep(3)

# For showing the desktop assistant logo


def logo():
    put_html("<p align=""left""><h4><img src=""https://icons.iconarchive.com/icons/icons8/windows-8/128/Business-Assistant-icon.png"" width=""28px"">  Desktop <del>VOICE</del> Assistant</h4></p>")

# For showing the dictionary logo


def dicti():
    put_html("<p align=""left""><h4><img src=""https://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/accessories-dictionary-icon.png"" width=""32px""> ENGLISH DICTIONARY</h4></p>")

# Function to check whether the words spelling is correct or not!


def stac(data):
    words = data.split()
    misspelled = spell.unknown(words)
    if not misspelled:
        return None
    else:
        spel = [word for word in misspelled]
        if len(spel) > 1:
            spel = ", ".join(spel)
            return f"couldn't recognize words \"{spel}\""
        else:
            spel = ", ".join(spel)
            return f"couldn't recognize word \"{spel}\""
# Function for producing the voice


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


# Function to check whether the word is exists or not in the ebooks json file


def Check(word):
    if word.lower() in book:
        return book[word.lower()], None
    elif word.title() in book:
        return book[word.title()], None
    elif word.upper() in book:
        return book[word.upper()], None
    elif len(get_close_matches(word, book.keys())) > 0:
        return book[get_close_matches(word, book.keys())[0]], 1
    else:
        return None, 2


# When we enter any input at the very beginning, if it's a mail then we will move forwards, else, we will check whether the given input is correct or not1
def Spell(data):
    emails = re.findall(
        r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)  # This findall function provide all the email addresses i.e stored in data
    if not emails:      # If there is no email inside the data then it will spell the data
        if "?" in data:
            data = data.replace("?", "")
        if "," in data:
            data = data.replace(",", "")
        if "!" in data:
            data = data.replace("!", "")
        words = data.split()
        # Find the words having wrongly spelled(written) by the user
        misspelled = spell.unknown(words)
        if not misspelled:
            return None
        else:
            spel = [word for word in misspelled]
            if len(spel) > 1:
                # Joining all the misspelled or wrong words by ','
                spel = ", ".join(spel)
                return f"couldn't recognize words \"{spel}\""
            else:
                spel = ", ".join(spel)
                return f"couldn't recognize word \"{spel}\""

# When we want to send a mail, we need to enter many inputs, then this function will check for all the inputs


def check_for(data):
    if data['link']:
        if not re.search(Pattern_1, data['link']):
            return('link', "URL doesn't exists")
        else:
            try:
                response = requests.get(data['link'])
                return None
            except requests.ConnectionError as exception:
                return('link', "URL doesn't exists")
    if not data['content'] and not data['subject']:
        toast('Sending this message without a subject or text in the body?', position='center',
              color='#008080', duration=5, onclick=clear)
        time.sleep(5)
        return None
    if not data['content']:
        toast('Sending this message without a subject or text in the body?', position='center',
              color='#008080', duration=5, onclick=clear)
        time.sleep(5)
        return None
    if not data['subject']:
        toast('Sending this message without a subject or text in the body?', position='center',
              color='#008080', duration=5, onclick=clear)
        time.sleep(5)
        return None

# In the case where we need to download the youtube videos, so there we provide the link, then this function would check whether the URL is correct or not!


def check_url(data):
    if not re.search(Pattern_1, data):
        return("URL doesn't exists")

# Checking all the mail data which we wanna send


def check_form(data):
    if not (re.search(regex, data['To'])):
        add = data['To']
        return ('To', f'The address "{add}" in the "To" field was not recognised.\n\nPlease make sure that all addresses are properly formed.')
    if data['link']:
        if not re.search(Pattern_1, data['link']):
            return('link', "URL doesn't exists")
        else:
            try:
                response = requests.get(data['link'])
                return None
            except requests.ConnectionError as exception:
                return('link', "URL doesn't exists")
    if not data['content'] and not data['subject']:
        toast('Sending this message without a subject or text in the body?', position='center',
              color='#008080', duration=5, onclick=clear)
        time.sleep(5)
        return None
    if not data['content']:
        toast('Sending this message without a subject or text in the body?', position='center',
              color='#008080', duration=5, onclick=clear)
        time.sleep(5)
        return None
    if not data['subject']:
        toast('Sending this message without a subject or text in the body?', position='center',
              color='#008080', duration=5, onclick=clear)
        time.sleep(5)
        return None

# Function to enter a new note


def enterNote(title, note):
    current_dateTime = str(datetime.datetime.today().strftime("%I:%M %p"))
    try:
        connection = engine.connect()
        query = db.insert(notes).values(
            Time=current_dateTime, Title=title, Note=note)
        result = connection.execute(query)
        connection.close()
    except Exception as e:
        put_warning(e)
        time.sleep(3)

# Function to display a note


def displayNote(title):
    try:
        connection = engine.connect()
        s = notes.select().where(notes.columns.Title == title)
        result = connection.execute(s)
        for row in result:
            style(put_text(row[2]),
                  'color:green; font-size: 20px')
            exists = True
            time.sleep(3)
        connection.close()
        if exists is not True:
            style(put_text(f'The note with a title "{title}" is not present'),
                  'color:green; font-size: 20px')
            time.sleep(3)
    except Exception as e:
        put_warning("Note doesn't exists")
        time.sleep(3)

# Function to update an existing note


def updateNote(title, note):
    current_dateTime = str(datetime.now())
    try:
        connection = engine.connect()
        query = db.update(notes).values(Time=current_dateTime, Note=note)
        query = query.where(notes.columns.Title == title)
        results = connection.execute(query)
        connection.close()
    except Exception as e:
        put_warning(e)
        time.sleep(3)

# Function to list all the available notes


def listAllNotes():
    try:
        connection = engine.connect()
        s = notes.select()
        result = connection.execute(s)
        for row in result:
            style(put_text(row[1]),
                  'color:blue; font-size: 20px')
            style(put_text(row[2]),
                  'color:green; font-size: 15px')
            put_html("<hr>")
            time.sleep(2)
        connection.close()
    except Exception as e:
        put_warning(e)
        time.sleep(3)

# Function to delete a specific note


def deleteNote(title):
    try:
        connection = engine.connect()
        query = db.delete(notes).where(notes.columns.Title == title)
        results = connection.execute(query)
        connection.close()
    except Exception as e:
        put_warning(e)
        time.sleep(3)

# When we enter any song name, the we need to generate the url pof the song, this function will help on that


def generateURL(songName):
    circ()
    search_keyword = str(songName)
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    playSong(url)

# Download the song from the url generated by the above function, then play the song


def playSong(url):
    yt = YouTube(str(url))
    audio = yt.streams.filter(only_audio=True).first()
    song = yt.title
    song = song.replace("|", "")
    if not os.path.exists(song+".mp3"):
        out_file = audio.download()
        clear()
        logo()
        base, _ = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        clear()
        logo()
        style(put_text("Playing: "+yt.title),
              'color:green; font-size: 25px')
        os.startfile(new_file)
        time.sleep(5)
    else:
        clear()
        logo()
        style(put_text("Playing: "+song+".mp3"),
              'color:green; font-size: 25px')
        os.startfile(song+".mp3")
# Function for the wishes


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        toast('Good Morning!', position='center',
              color='#469F70', duration=3, onclick=clear)
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        toast('Good Afternoon!', position='center',
              color='#469F70', duration=3, onclick=clear)
        speak("Good Afternoon")
    else:
        toast('Good Evening!', position='center',
              color='#469F70', duration=3, onclick=clear)
        speak("Good Evening")


def main(_):
    while 1:
        clear()
        logo()
        Query = input(placeholder="Try Searching something...",
                      required=True, validate=Spell)
        Query = Query.lower().strip()

        if ('wikipedia' in Query and "open" in Query) or 'wikipedia' in Query:
            while 1:
                clear()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Google-Earth-icon.png"" width=""120px""></p>")
                Test_string = input(
                    placeholder="Wikipedia Search", required=True)
                if "wikipedia" in Test_string:
                    Test_string = Test_string.replace("wikipedia", "")
                whats = Test_string
                try:
                    progress()
                    clear()
                    logo()
                    put_success("Almost done!")
                    Result = wikipedia.summary(
                        Test_string, sentences=2, auto_suggest=False, redirect=True)
                    time.sleep(3)
                    clear()
                    logo()
                    popup(f"{Test_string.title()} Wikipedia", [put_html("<ol>"f"{Result}""</ol>"), put_buttons(
                        ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)
                except:
                    Test_string = wikipedia.suggest(Test_string)
                    try:
                        Result = wikipedia.summary(
                            Test_string, sentences=2, auto_suggest=False, redirect=True)
                        clear()
                        logo()
                        time.sleep(2)
                        popup(f"{Test_string.title()} Wikipedia", [put_html("<ol>"f"{Result}""</ol>"), put_buttons(
                            ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)
                    except:
                        clear()
                        logo()
                        put_warning(
                            f"Aw, Snap!\nSomething went wrong while displaying result for \"{whats.strip()}\"")
                        time.sleep(4)
                a = radio("Do you want to search more queries?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif ('youtube' in Query and "open" in Query) or 'youtube' in Query:
            while 1:
                clear()
                logo()
                Query = Query.replace("youtube", "")
                Query = Query.lower().strip()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/dakirby309/simply-styled/256/YouTube-icon.png"" width=""120px""></p>")
                Test_string = input(
                    placeholder="YouTube Search", required=True)
                if 'youtube' in Test_string.lower().strip():
                    Test_string = Test_string.replace("youtube", "")
                progress()
                clear()
                logo()
                put_success("Almost done!")
                time.sleep(3)
                clear()
                logo()
                Test_string = Test_string.title().strip()
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={Test_string}")
                a = radio("Do you want to search more queries?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif ('google' in Query and "open" in Query) or 'google' in Query:
            while 1:
                clear()
                logo()
                Query = Query.replace("google", "")
                Query = Query.lower().strip()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://media.tenor.com/images/c130571f5e239c834e52f75d4d06d4d8/tenor.gif"" width=""120px""></p>")
                Test_string = input(
                    placeholder="Google Search", required=True)
                if 'google' in Test_string.lower().strip():
                    Test_string = Test_string.replace("google", "")
                progress()
                clear()
                logo()
                put_success("Almost done!")
                time.sleep(3)
                clear()
                logo()
                Test_string = Test_string.title().strip()
                webbrowser.open(
                    f"https://www.google.com/search?q={Test_string}")
                a = radio("Do you want to search more queries?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "send email" in Query or "send mail" in Query or "sendemail" in Query or "mail" in Query or "email" in Query or "gmail" in Query or "send gmail" in Query or 'sendgmail' in Query:
            while 1:
                clear()
                logo()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Communication-gmail-icon.png"" width=""120px""></p>")
                data = input_group("New Message", [input('', name='To', type=TEXT, required=True, PlaceHolder="Recipients"), input(
                    '', name='subject', type=TEXT, PlaceHolder="Subject"), input('', name='content', type=TEXT, PlaceHolder="Content"), input('Attach file', name='path', type=TEXT, PlaceHolder="File path"), input('Insert link', name='link', type=TEXT, PlaceHolder="Link here")], validate=check_form, cancelable=True)
                to = data['To']
                subject = data['subject']
                body = data['content']
                if data['link'] or data['path']:
                    Link = data['link']
                    html = f'<a href={Link}>Click here!</a>'
                    file = data['path']
                    content = [body, file, html]
                    progresses()
                    yag.send(f'{to}', f'{subject}', content)
                else:
                    content = [body]
                    progresses()
                    yag.send(f'{to}', f'{subject}', content)
                clear()
                logo()
                put_success("Message sent successfully")
                time.sleep(3)
                a = radio("Do you want to send more mails?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "send mail to " in Query or "mail to" in Query or "email to" in Query or "gmail to" in Query or "send email to" in Query or "send gmail to" in Query:
            while 1:
                clear()
                logo()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Communication-gmail-icon.png"" width=""120px""></p>")
                emails = re.findall(
                    r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", Query)
                if emails:
                    put_html(
                        "<ol align=""left"">To: <b>"f"{emails[0]}""</b></ol>")
                    data = input_group(f"New Message", [input('', name='subject', type=TEXT, PlaceHolder="Subject"), input('', name='content', type=TEXT, PlaceHolder="Content"), input(
                        'Attach file', name='path', type=TEXT, PlaceHolder="File path"), input('Insert link', name='link', type=TEXT, PlaceHolder="Link here")], validate=check_for, cancelable=True)
                    clear()
                    logo()
                    to = emails[0]
                    subject = data['subject']
                    body = data['content']
                    if data['link'] or data['path']:
                        Link = data['link']
                        html = f'<a href={Link}>Click here!</a>'
                        file = data['path']
                        content = [body, file, html]
                        progresses()
                        yag.send(f'{to}', f'{subject}', content)
                    else:
                        content = [body]
                        progresses()
                        yag.send(f'{to}', f'{subject}', content)
                    clear()
                    logo()
                    put_success("Message sent successfully")
                    time.sleep(3)
                a = radio("Do you want to send more mails?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "send mail" in Query or "send email" in Query or "send gmail" in Query or "email" in Query or "gmail" in Query or "mail" in Query:
            while 1:
                clear()
                logo()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Communication-gmail-icon.png"" width=""120px""></p>")
                data = input_group("New Message", [input('', name='To', type=TEXT, required=True, PlaceHolder="Recipients"), input(
                    '', name='subject', type=TEXT, PlaceHolder="Subject"), input('', name='content', type=TEXT, PlaceHolder="Content"), input('Attach file', name='path', type=TEXT, PlaceHolder="File path"), input('Insert link', name='link', type=TEXT, PlaceHolder="Link here")], validate=check_form, cancelable=True)
                to = data['To']
                subject = data['subject']
                body = data['content']
                if data['link'] or data['path']:
                    Link = data['link']
                    html = f'<a href={Link}>Click here!</a>'
                    file = data['path']
                    content = [body, file, html]
                    yag.send(f'{to}', f'{subject}', content)
                else:
                    content = [body]
                    progresses()
                    yag.send(f'{to}', f'{subject}', content)
                    progresses()
                clear()
                logo()
                put_success("Message sent successfully")
                time.sleep(3)
                a = radio("Do you want to send more mails?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "keep note" in Query or "keep notes" in Query or "notes" in Query or "note" in Query or "keep" in Query or "keep notes" in Query or "store data" in Query:
            while 1:
                clear()
                logo()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/custom-icon-design/flatastic-6/256/Note-icon.png"" width=""10%""></p>")
                choice = radio("What do you want to do?", options=[
                    'Insert a new note', 'View a note', 'Update a note', 'List all the notes', 'Delete a note'], required=True)
                if choice == 'Insert a new note':
                    data = input_group("", [
                        input('Title', name='ttle', type=TEXT,
                              required=True, PlaceHolder="Enter Title"),

                        input('Note', name='Nte', type=TEXT,
                              required=True, PlaceHolder="Note...")], cancelable=True)
                    title = data['ttle']
                    note = data['Nte']
                    enterNote(title, note)
                    put_success("Note inserted successfully")
                    time.sleep(3)

                elif choice == 'View a note':
                    title = input(
                        '', placeholder="Enter title of note to view", required=True)
                    displayNote(title)

                elif choice == 'Update a note':
                    data = input_group("", [
                        input('Title', name='ttle', type=TEXT,
                              required=True, PlaceHolder="'Enter the title of the note to be updated"),

                        input('Note', name='Nte', type=TEXT,
                              required=True, PlaceHolder="Enter new-note")], cancelable=True)
                    title = data['ttle']
                    note = data['Nte']
                    updateNote(title, note)
                    put_success("Note updated successfully")
                    time.sleep(3)

                elif choice == 'List all the notes':
                    clear()
                    style(put_text("Available Notes: "),
                          'color:red; font-size: 25px')
                    time.sleep(3)
                    listAllNotes()

                elif choice == 'Delete a note':
                    title = input(
                        '', placeholder="Enter title of note to be deleted", required=True)
                    again = radio(
                        "Are you sure you want to delete this data?", ["Yes", "No"])
                    if again == "Yes":
                        deleteNote(title)
                        put_error("Note deleted successfully")
                        time.sleep(3)
                a = radio("Do you want to keep more notes?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "video" in Query or "download" in Query or "download video" in Query or "download videos" in Query:
            while 1:
                clear()
                logo()
                Bar()
                clear()
                logo()
                put_html(
                    "<p align=""center""><img src=""https://icons.iconarchive.com/icons/custom-icon-design/mono-general-2/256/download-icon.png"" width=""120px""></p>")
                url = input("URL", type=TEXT, placeholder="https:/xyz.com",
                            required=True, validate=check_url)
                try:
                    # Creating a youtube object
                    youtube = pytube.YouTube(url)
                    # Getting the video stream of highest quality with both video and audio codec
                    style(put_text("Downloading..."),
                          'color:red; font-size: 25px')
                    video = youtube.streams.filter(
                        progressive=True, file_extension='mp4').desc().first()
                    # Getting the path of the 'Downloads' folder of the user's computer
                    path = str(os.path.join(Path.home(), 'Downloads'))
                    # Downloading the video to the 'Downloads' folder
                    video.download(output_path=path)
                    clear()
                    logo()
                    put_success(video.title+' downloaded successfully!')
                    time.sleep(3)

                # If there is any exception, print it
                except Exception as e:
                    put_error("Error occured - "+e)
                    time.sleep(3)
                a = radio("Do you want to download more videos?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "bin" in Query or "recycle" in Query or "empty" in Query or 'recycle bin' in Query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                style(put_text("Deleting items..."),
                      'color:red; font-size: 25px')
                time.sleep(2)
                clear()
                logo()
                style(put_text("Wait for a sec..."),
                      'color:red; font-size: 25px')
                time.sleep(2)
                clear()
                logo()
                put_success("Recycle bin empty successfully...")
                time.sleep(3)
            except:
                put_error("Recycle bin is already empty!")
                time.sleep(4)
        elif "photo" in Query or "take photo" in Query or "image" in Query or "capture image" in Query or "camera" in Query or "pic image" in Query:
            while 1:
                clear()
                logo()
                try:
                    style(put_text("Wait for a sec..."),
                          'color:red; font-size: 18px')
                    camera = cv2.VideoCapture(0)
                    _, image = camera.read()
                    clear()
                    logo()
                    name = input(
                        "", placeholder="With what name do you want to save the image?", required=True)
                    cv2.imwrite(name+".png", image)
                    del(camera)
                    put_success("Image capture successfully!")
                    time.sleep(3)
                except Exception as e:
                    put_warning("Unable to access camera!")
                    time.sleep(3)
                a = radio("Do you want to capture more images",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "play music" in Query or "play song" in Query or "play" in Query or "song" in Query or "music" in Query:
            while 1:
                clear()
                logo()
                songName = input("", placeholder="Song name", required=True)
                songName = songName.replace(" ", "")
                generateURL(songName)
                a = radio("Do you want to play more songs?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "time" in Query:
            style(put_text(datetime.datetime.today().strftime("%I:%M %p")),
                  'color:red; font-size: 25px')
            time.sleep(4)
        elif "date" in Query:
            current_time = datetime.datetime.now()
            datetime_object = datetime.datetime.strptime(
                str(current_time.month), "%m")
            month_name = datetime_object.strftime("%b")
            style(put_text(month_name+" "+str(current_time.day) +
                  ", "+str(current_time.year)),
                  'color:red; font-size: 25px')
            time.sleep(4)
        elif "day" in Query:
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            day, month, year = d1.split('/')
            day_name = datetime.date(int(year), int(month), int(day))
            style(put_text(day_name.strftime("%A")),
                  'color:red; font-size: 25px')
            time.sleep(3)
        elif "month" in Query:
            current_time = datetime.datetime.now()
            datetime_object = datetime.datetime.strptime(
                str(current_time.month), "%m")
            month_name = datetime_object.strftime("%B")
            style(put_text(month_name),
                  'color:red; font-size: 25px')
            time.sleep(4)
        elif "restart" in Query:
            again = radio(
                "Are you sure you want to reSTART your PC?", ["Yes", "No"])
            if again == "Yes":
                os.system("shutdown /r /t  1")
        elif "jokes" in Query or "joke" in Query or "fun" in Query:
            while 1:
                clear()
                logo()
                My_joke = pyjokes.get_joke(
                    language="en", category="neutral")
                popup("Jokes", [put_html("<ol>"f"{My_joke}""</ol>"), put_buttons(
                    ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)
                a = radio("Do you want to have more jokes?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "location" in Query or "locate" in Query or "map" in Query:
            while 1:
                clear()
                logo()
                what = input("", placeholder="Location?", required=True)
                circ()
                webbrowser.open_new_tab(
                    "https://www.google.com/maps/place/"+what)
                clear()
                logo()
                a = radio("Do you want to search again?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "shutdown" in Query or "shut" in Query:
            again = radio(
                "Are you sure you want to shutDOWN your PC?", ["Yes", "No"])
            if again == "Yes":
                os.system("shutdown /s /t  1")
        elif "battery" in Query:
            battery = psutil.sensors_battery()
            percent = battery.percent  # Give you the battery percent

            if percent >= 90:
                pluged = battery.power_plugged  # Check whether the plugged in or not
                plug = "Plugged In" if pluged else "Plugged Not In"

                if plug == "Plugged In":
                    # Producing a notification with the Battery percentage and a Icon
                    popup(f"Battery Percentage Reaches to: {percent}%", [put_html("<ol>""Please Remove the Plug!""</ol>"), put_buttons(
                        ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)

            else:
                pluged = battery.power_plugged
                plug = "Plugged In" if pluged else "Plugged Not In"
                if plug == "Plugged In":
                    popup(f"Battery Percentage Reaches to: {percent}%", [put_html("<ol>""Please Don't Remove the Plug!""</ol>"), put_buttons(
                        ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)

                else:
                    popup(f"Battery Percentage Reaches to: {percent}%", [put_html("<ol>""Please Connect to the the Plug!""</ol>"), put_buttons(
                        ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)
        elif "dictionary" in Query:
            while 1:
                clear()
                logo()
                clear()
                dicti()
                word = input("", placeholder="What word do you want to look up?",
                             required=True, validate=stac)
                put_html(
                    "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                time.sleep(3)
                tran, res = Check(word)
                Res = type(tran)
                clear()
                dicti()
                if Res == list:
                    if res == 1:
                        put_warning("Error! word not found", closable=True)
                        time.sleep(3)
                        clear()
                        dicti()
                        for i in tran:
                            popup(f"Showing result for {get_close_matches(word, book.keys())[0].capitalize()}",
                                  [put_html("<ol>"f"{i}""</ol>"), put_buttons(
                                      ['Close'], onclick=lambda _: close_popup())])
                            break
                    elif res == 2:
                        put_error(
                            "No definitions found for this word, Try searching...")
                        time.sleep(3)
                        clear()
                        dicti()
                        break
                    elif res == None:
                        put_success("Wow, word found")
                        time.sleep(3)
                        clear()
                        dicti()
                        for i in tran:
                            popup(f"{word.capitalize()}", [put_html("<ol>"f"{i}""</ol>"), put_buttons(
                                ['Close'], onclick=lambda _: close_popup())])
                            break

                else:
                    put_error(
                        "No definitions found for this word, Try searching...")
                    time.sleep(3)
                    clear()
                    dicti()

                a = radio("Do you want to search again?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "meaning of" in Query:
            Query = Query.replace("meaning of", "")
            Query = Query.strip()
            put_html(
                "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
            time.sleep(3)
            word = Query
            word = stac(word)
            if word == None:
                word = Query
            tran, res = Check(word)
            Res = type(tran)
            clear()
            dicti()
            if Res == list:
                if res == 1:
                    put_warning("Error! word not found", closable=True)
                    time.sleep(3)
                    clear()
                    dicti()
                    for i in tran:
                        popup(f"Showing result for {get_close_matches(word, book.keys())[0].capitalize()}",
                              [put_html("<ol>"f"{i}""</ol>"), put_buttons(
                                  ['Close'], onclick=lambda _: close_popup())])
                        break
                elif res == 2:
                    put_error(
                        "No definitions found for this word, Try searching...")
                    time.sleep(3)
                    clear()
                    dicti()
                    break
                elif res == None:
                    put_success("Wow, word found")
                    time.sleep(3)
                    clear()
                    dicti()
                    for i in tran:
                        popup(f"{word.capitalize()}", [put_html("<ol>"f"{i}""</ol>"), put_buttons(
                            ['Close'], onclick=lambda _: close_popup())])
                        break

            else:
                put_error(
                    "No definitions found for this word, Try searching...")
                time.sleep(3)
                clear()
                dicti()
        elif "weather" in Query:
            while 1:
                clear()
                put_image(
                    "https://icons.iconarchive.com/icons/pixelkit/flat-jewels/128/Weather-icon.png")
                City = input("", placeholder="City name",
                             required=True, validate=Check_weath)
                clear()
                weathy()
                circ()
                clear()
                complete_url = f"{base_url}appid={api_key}&q={City}"
                response = requests.get(complete_url)
                temp = response.json()
                Res = temp["main"]
                current_temperature = Res["temp"]
                curr = current_temperature-273.15
                current_pressure = Res["pressure"]
                current_humidiy = Res["humidity"]
                Descrip = temp["weather"]
                weather_description = Descrip[0]["description"]
                popup(f"{City.title()} Weather", [put_html("<h4>"f"Temperature: {math.ceil(curr)}{chr(176)}C</br>Atmospheric Pressure: {current_pressure} hpa</br>Humidity: {current_humidiy}%</br>Description: {weather_description.title()}""</h4>"), put_buttons(
                    ['Close'], onclick=lambda _: close_popup())], implicit_close=True)
                clear()
                a = radio("Do you want to search again?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "send message" in Query or "notify" in Query or "notification" in Query or "send notification" in Query:
            data = input('', placeholder="Title", required=True)
            text = textarea("Text", rows=3,
                            placeholder="Write something...", required=True)
            pb = PushBullet(access_token)
            push = pb.push_note(data, text)
            put_success("Message sent successfullly...")
            time.sleep(3)
        elif "maths" in Query or "calculation" in Query or "maths calculation" in Query or "maths calculations" in Query or "math calculation" in Query or "maths calculations" in Query:
            while 1:
                clear()
                logo()
                inputCommand = input(
                    "", placeholder="What do you want to do?", required=True)
                match = commands.search(inputCommand)
                if match:
                    command = match.group().lower()
                    numbers = re.findall(r'\d+', inputCommand)
                    numbers = list(map(int, numbers))

                    if command == 'add' or command == 'sum' or command == "+" or command == "addition":
                        style(put_text(addNumbers(numbers)),
                              'color:red; font-size: 20px')
                    elif command == 'subtract' or command == 'difference' or command == "-" or command == "sub":
                        style(put_text(diffNumbers(
                            numbers[0], numbers[1])), 'color:red; font-size: 20px')
                    elif command == 'multiply' or command == 'product' or command == "mul" or command == "prod":
                        style(put_text(multiplyNumbers(numbers)),
                              'color:red; font-size: 20px')
                    elif command == 'divide' or command == "/" or command == "%" or command == "div":
                        after = "{:.2f}".format(
                            divideNumbers(numbers[0], numbers[1]))
                        style(put_text(after), 'color:red; font-size: 20px')
                    elif command == 'sin':
                        radians = toRadians(numbers[0])
                        after = round(math.sin(radians), 2)
                        style(put_text(after),
                              'color:red; font-size: 20px')
                    elif command == 'cos':
                        radians = toRadians(numbers[0])
                        after = round(math.cos(radians))
                        style(put_text(after),
                              'color:red; font-size: 20px')
                    elif command == 'tan':
                        radians = toRadians(numbers[0])
                        after = round(math.tan(radians), 2)
                        style(put_text(after),
                              'color:red; font-size: 20px')
                    elif command == 'sqrt' or command == 'square root' or command == "root":
                        style(
                            put_text(math.sqrt(numbers[0])), 'color:red; font-size: 20px')
                else:
                    put_warning("Alert!, given command is not recognised")
                a = radio("Do you want to calculate again?",
                          options=['Yes', 'No'], required=True)
                if a == 'Yes':
                    continue
                else:
                    break
        elif "who are you?" in Query or "who are you" in Query or "what is your name" in Query:
            speak("I am a DevIncept Assistant built by Satyam, Rahul, and Shruti")
        elif "hey, who are you?" in Query or "hey who are you" in Query or "hey who are you?" in Query or "hey, who are you" in Query:
            speak("Hello, I am a DevIncept Assistant built by Satyam, Rahul, and Shruti")
        elif "how are you?" in Query or "how are you" in Query:
            speak("Hello, I am fine, Thank you for asking and what about you")
        elif "hey, how are you?" in Query or "hey how are you" in Query or "hey how are you?" in Query or "hey, how are you" in Query:
            speak("Hello, I am fine, Thank you for asking and what about you")


if __name__ == '__main__':
    wishme()
    time.sleep(3)
    put_html("<p align=""center""><h1><img src=""https://icons.iconarchive.com/icons/icons8/windows-8/128/Business-Assistant-icon.png"">  Desktop <del>VOICE</del> Assistant</h1></p>")
    put_html("<h3>What can Assistant do?</h3>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Google-Earth-icon.png"" width=""32px""> WikiPedia &emsp;&emsp;&nbsp;&emsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/dtafalonso/android-l/256/Youtube-icon.png"" width=""32px""> YouTube &emsp;&emsp;&emsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/google-icon.png"" width=""32px""> Google &emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Gmail-icon.png"" width=""32px""> Send Email &emsp;&emsp;&emsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/fasticon/hand-draw-iphone/256/Notes-icon.png"" width=""32px""> Keep Notes</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/designbolts/seo/256/Time-Management-icon.png"" width=""32px""> Time &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Google-Calendar-icon.png"" width=""32px""> Date &emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;&nbsp;  <img src=""https://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Media-play-music-icon.png"" width=""32px""> Play Music &emsp;&ensp; <img src=""https://icons.iconarchive.com/icons/mkho/christmas/256/Bell-icon.png"" width=""32px""> Send Notification &nbsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/wineass/ios7-redesign/256/Calculator-icon.png"" width=""30px""> Maths Calculation</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/xenatt/minimalism/256/App-dictionary-icon.png"" width=""32px""> Words Meaning &ensp;&ensp; <img src=""https://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/weather-icon.png"" width=""32px""> Weather &ensp;&emsp;&emsp;&ensp;&nbsp; <img src=""https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Status-battery-080-icon.png"" width=""32px""> Battery &emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/hopstarter/soft-scraps/256/Button-Log-Off-icon.png"" width=""30px""> ShutDown &emsp;&emsp;&nbsp;&nbsp;&ensp;&ensp;&nbsp; <img src=""https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/map-marker-icon.png"" width=""32px""> Search Locations</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/256/Downloads-icon.png"" width=""32px""> Download Video &ensp; <img src=""https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Emotes-face-smile-icon.png"" width=""32px""> Jokes &nbsp;&ensp;&emsp;&emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/icons8/windows-8/256/Computer-Hardware-Restart-icon.png"" width=""30px""> reSTART &emsp;&emsp;&nbsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/dapino/summer-holiday/256/camera-icon.png"" width=""32px""> Take a Photo &emsp;&nbsp;&nbsp;&nbsp;&emsp; <img src=""https://icons.iconarchive.com/icons/itzikgur/my-seven/256/Recycle-Bin-full-icon.png"" width=""32px""> Empty Recycle Bin</p>")
    put_html("<hr>")
    put_buttons(
        [dict(label='Next', value='outline-success', color='outline-success')], onclick=main)
hold()
