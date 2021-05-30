import datetime
import requests
import speech_recognition as sr
import json
import time
from difflib import get_close_matches
from datetime import date
import wikipedia
import webbrowser
import os
import pyautogui
import random
import pyjokes
import psutil
import re
import yagmail
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from spellchecker import SpellChecker

spell = SpellChecker()

yag = yagmail.SMTP("satyampsit244@gmail.com")

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

Pattern = re.compile("(0/91)?[6-9][0-9]{9}")

regex_1 = ("((http|https)://)(www.)?" +
           "[a-zA-Z0-9@:%._\\+~#?&//=]" +
           "{2,256}\\.[a-z]" +
           "{2,6}\\b([-a-zA-Z0-9@:%" +
           "._\\+~#?&//=]*)")

Pattern_1 = re.compile(regex_1)


def Spell(data):
    emails = re.findall(
                r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)
    if not emails: 
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


def progress():
    put_html("<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
    time.sleep(3)
    clear()


def progresses(Query):
    put_processbar("Hello", label=f"Searching on {Query}", auto_close=True)
    for i in range(1, 11):
        set_processbar('Hello', i / 10, label=f"Searching on {Query}")
        time.sleep(0.3)


def logo():
    put_html("<p align=""left""><h4><img src=""https://icons.iconarchive.com/icons/icons8/windows-8/128/Business-Assistant-icon.png"" width=""28px"">  Desktop <del>VOICE</del> Assistant</h4></p>")


def main(some):
    while 1:
        clear()
        logo()
        Query = input(placeholder="Try Searching something...",
                      required=True, validate=Spell)
        Query = Query.lower().strip()
        if ('wikipedia' in Query and "open" in Query) or 'wikipedia' in Query:
            Query = Query.replace("wikipedia", "")
            Que = Query
            put_html(
                "<p align=""center""><img src=""https://media.tenor.com/images/0d34378f630afe43f7ed93f8341d7d77/tenor.gif"" width=""120px""></p>")
            time.sleep(5)
            clear()
            logo()
            put_html(
                "<p align=""center""><img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Google-Earth-icon.png"" width=""120px""></p>")
            what = input(
                placeholder="Wikipedia Search", required=True)
            if "wikipedia" in what:
                what = what.replace("wikipedia", "")
            whats = what
            try:
                progress()
                clear()
                logo()
                put_success("Almost done!")
                Result = wikipedia.summary(
                    what, sentences=2, auto_suggest=False, redirect=True)
                time.sleep(3)
                clear()
                logo()
                popup(f"{what.title()} Wikipedia", [put_html("<ol>"f"{Result}""</ol>"), put_buttons(
                    ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)
            except:
                what = wikipedia.suggest(what)
                try:
                    progress()
                    logo()
                    put_success("Almost done!")
                    Result = wikipedia.summary(
                        what, sentences=2, auto_suggest=False, redirect=True)
                    time.sleep(2)
                    clear()
                    logo()
                    popup(f"{what.title()} Wikipedia", [put_html("<ol>"f"{Result}""</ol>"), put_buttons(
                        ['Close'], onclick=lambda _: close_popup())], size=PopupSize.NORMAL)
                except:
                    progress()
                    logo()
                    put_warning(
                        f"Aw, Snap!\nSomething went wrong while displaying result for \"{whats.strip()}\"")
                    time.sleep(6)
        elif ('youtube' in Query and "open" in Query) or 'youtube' in Query:
            Query = Query.replace("youtube", "")
            Query = Query.lower().strip()
            put_html(
                "<p align=""center""><img src=""https://media.tenor.com/images/0d34378f630afe43f7ed93f8341d7d77/tenor.gif"" width=""120px""></p>")
            time.sleep(5)
            clear()
            logo()
            put_html(
                "<p align=""center""><img src=""https://icons.iconarchive.com/icons/dakirby309/simply-styled/256/YouTube-icon.png"" width=""120px""></p>")
            what = input(
                placeholder="YouTube Search", required=True)
            progress()
            clear()
            logo()
            put_success("Almost done!")
            time.sleep(3)
            clear()
            logo()
            what = what.title().strip()
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={what}")
        elif ('google' in Query and "open" in Query) or 'google' in Query:
            Query = Query.replace("google", "")
            Query = Query.lower().strip()
            put_html(
                "<p align=""center""><img src=""https://media.tenor.com/images/0d34378f630afe43f7ed93f8341d7d77/tenor.gif"" width=""120px""></p>")
            time.sleep(5)
            clear()
            logo()
            put_html(
                "<p align=""center""><img src=""https://media.tenor.com/images/c130571f5e239c834e52f75d4d06d4d8/tenor.gif"" width=""120px""></p>")
            what = input(
                placeholder="Google Search", required=True)
            progress()
            clear()
            logo()
            put_success("Almost done!")
            time.sleep(3)
            clear()
            logo()
            what = what.title().strip()
            webbrowser.open(f"https://www.google.com/search?q={what}")
        elif Query == "send email" or Query == "send mail" or Query == "sendemail" or Query == "mail" or Query == "email" or Query == "gmail" or Query == "send gmail" or Query == 'sendgmail':
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
                put_html(
                    "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                time.sleep(3)
                yag.send(f'{to}', f'{subject}', content)
            else:
                content = [body]
                put_html(
                    "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                time.sleep(3)
                yag.send(f'{to}', f'{subject}', content)
            clear()
            logo()
            put_success("Message sent successfully")
            time.sleep(3)
        elif "send mail to " in Query or "mail to" in Query or "email to" in Query or "gmail to" in Query or "send email to" in Query or "send gmail to" in Query:
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
                    put_html(
                        "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                    time.sleep(3)
                    yag.send(f'{to}', f'{subject}', content)
                else:
                    content = [body]
                    put_html(
                        "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                    time.sleep(3)
                    yag.send(f'{to}', f'{subject}', content)
                clear()
                logo()
                put_success("Message sent successfully")
                time.sleep(3)
        elif "send mail" in Query or "send email" in Query or "send gmail" in Query or "email" in Query or "gmail" in Query or "mail" in Query:
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
                put_html(
                    "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                time.sleep(3)
                yag.send(f'{to}', f'{subject}', content)
            else:
                content = [body]
                put_html(
                    "<p align=""center""><img src=""https://media.tenor.com/images/6399c69d68f8e6351e599e0db88f665e/tenor.gif"" width=""120px""></p>")
                time.sleep(3)
                yag.send(f'{to}', f'{subject}', content)
            clear()
            logo()
            put_success("Message sent successfully")
            time.sleep(3)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        toast('Good Morning!', position='center',
              color='#469F70', duration=4, onclick=clear)
    elif hour >= 12 and hour < 17:
        toast('Good Afternoon!', position='center',
              color='#469F70', duration=4, onclick=clear)
    else:
        toast('Good Evening!', position='center',
              color='#469F70', duration=4, onclick=clear)


if __name__ == '__main__':
    wishme()
    time.sleep(4)
    put_html("<p align=""center""><h1><img src=""https://icons.iconarchive.com/icons/icons8/windows-8/128/Business-Assistant-icon.png"">  Desktop <del>VOICE</del> Assistant</h1></p>")
    put_html("<h3>What can Assistant do?</h3>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Google-Earth-icon.png"" width=""32px""> WikiPedia &emsp;&emsp;&nbsp;&emsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/dtafalonso/android-l/256/Youtube-icon.png"" width=""32px""> YouTube &emsp;&emsp;&emsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/google-icon.png"" width=""32px""> Google &emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Gmail-icon.png"" width=""32px""> Send Email &emsp;&emsp;&emsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/limav/flat-gradient-social/256/Stackoverflow-icon.png"" width=""30px""> Open StackOverflow</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/designbolts/seo/256/Time-Management-icon.png"" width=""32px""> Time &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/marcus-roberto/google-play/256/Google-Calendar-icon.png"" width=""32px""> Date &emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;&nbsp;  <img src=""https://icons.iconarchive.com/icons/cornmanthe3rd/plex/256/Media-play-music-icon.png"" width=""32px""> Play Music &emsp;&ensp; <img src=""https://icons.iconarchive.com/icons/mkho/christmas/256/Bell-icon.png"" width=""32px""> Send Notification &nbsp;&nbsp; <img src=""https://icons.iconarchive.com/icons/wineass/ios7-redesign/256/Calculator-icon.png"" width=""30px""> Maths Calculation</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/xenatt/minimalism/256/App-dictionary-icon.png"" width=""32px""> Words Meaning &ensp;&ensp; <img src=""https://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/weather-icon.png"" width=""32px""> Weather &ensp;&emsp;&emsp;&ensp;&nbsp; <img src=""https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Status-battery-080-icon.png"" width=""32px""> Battery &emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/sbstnblnd/plateau/256/Apps-notes-icon.png"" width=""32px""> Write Notes &emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/hopstarter/soft-scraps/256/Button-Log-Off-icon.png"" width=""30px""> ShutDown</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/256/Downloads-icon.png"" width=""32px""> Download Video &nbsp;&ensp; <img src=""https://icons.iconarchive.com/icons/custom-icon-design/flatastic-11/256/Cloud-icon.png"" width=""32px""> WordCloud &emsp;&ensp;&nbsp; <img src=""https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Emotes-face-smile-icon.png"" width=""32px""> Jokes &nbsp;&ensp;&emsp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/icons8/windows-8/256/Computer-Hardware-Restart-icon.png"" width=""30px""> reSTART &emsp;&nbsp;&ensp;&emsp;&emsp;&ensp;&nbsp; <img src=""https://icons.iconarchive.com/icons/itzikgur/my-seven/256/Recycle-Bin-full-icon.png"" width=""32px""> Empty Recycle Bin</p>")
    put_html("<p><img src=""https://icons.iconarchive.com/icons/dapino/summer-holiday/256/camera-icon.png"" width=""32px""> Take a Photo &ensp;&emsp;&emsp; <img src=""https://icons.iconarchive.com/icons/inipagi/job-seeker/256/notes-icon.png"" width=""32px""> Show Notes &nbsp;&nbsp;&ensp;&ensp; <img src=""https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/lock-icon.png"" width=""30px""> Lock Window &nbsp; <img src=""https://icons.iconarchive.com/icons/paomedia/small-n-flat/256/map-marker-icon.png"" width=""32px""> Search Locations &ensp;&ensp; <img src=""https://icons.iconarchive.com/icons/wwalczyszyn/android-style-honeycomb/256/Talk-icon.png"" width=""32px""> Personal Talk</p><br>")
    put_buttons(
        [dict(label='Next', value='outline-success', color='outline-success')], onclick=main)
    put_html("<hr><h4 align=""left"">&copy; Satyam Tripathi</h4>")
hold()
