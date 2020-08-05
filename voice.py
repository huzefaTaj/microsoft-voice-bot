import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engin=pyttsx3.init('sapi5')
voices=engin.getProperty('voices')
engin.setProperty('voice',voices[1].id)
def speak(audio):
    engin.say(audio)
    engin.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<11:
        speak("goodmorning")
    elif hour>=12 and hour<5:
        speak("good afternoon")
    else:
        speak("good evening")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listining....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recog...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        # print(e)
        print("say it again.....")
        return takecommand()
    return query



if __name__ == '__main__':
    wishme()
    speak("hello huzefa ")
    while True:
        query= takecommand().lower()

        #wikipedia
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("search","")
            query=query.replace("wikipedia","")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipidia")
                print(results)
                speak(results)
            except Exception as  e:
                speak("sorry i cant find any result on wikipedia")



        #     hello
        elif 'hello' in query:
            speak("hello how may i help you")

        #youtube
        elif 'youtube' in query:
            query = query.replace("search", "")
            query = query.replace("open", "")
            query = query.replace("on", "")
            query = query.replace("youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}" )


        # search
        elif 'search' in query:
            query=query.replace("search","")
            speak("searching")
            speak(query)
            webbrowser.open(f"https://www.google.com/search?safe=active&rlz=1C1GGRV_enIN865IN866&sxsrf=ALeKk03uOSKxP2_XwbEHf25NLgRUA_Vksw%3A1595876959287&ei=XyYfX9STEZiR4-EP6riy8Aw&q={query}&oq={query}+&gs_lcp=CgZwc3ktYWIQAxgAMgQIIxAnMgcIABCxAxBDMgUIABCxAzIICAAQsQMQgwEyBwguELEDEEMyCAgAELEDEIMBMgQILhBDMgUIABCxAzIFCAAQsQMyAggAOgcIIxCwAxAnOg0ILhCxAxCDARCwAxBDOgkIABCwAxAHEB46CAgAELEDELADOgsIABCxAxCDARCwAzoFCAAQsANQ288BWNvPAWCN4gFoBHAAeACAAagCiAGoApIBAzItMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab")

        # google
        elif'open google' in query:
            webbrowser.open("www.google.com")

        # github
        elif 'open github' in query:
            webbrowser.open("https://github.com/huzefaTaj")

        #facebook
        elif 'facebook' in query:
           webbrowser.open("www.facebook.com")

        elif 'instagram' in query:
           webbrowser.open("www.instagram.com")

        elif 'open' in query:
           query = query.replace("open", "")
           webbrowser.open(f"www.{query}.com")


        #music
        elif'music' in query:
            music_dir='D:\\music\\Hindi songs'#choase your path here
            songs=os.listdir(music_dir)
            print("wait for a minute")
            speak("wait for a minute")
            os.startfile(os.path.join(music_dir,songs[0]))

        #time
        elif'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(strtime)

        elif'who created you' in query:
            speak("I created by a ginus person, name is huzefa taj ")


        # exit
        elif 'exit' in query:
            speak("Thank you for visiting here")
            exit(0)

        elif query in query:
            webbrowser.open( f"https://www.google.com/search?safe=active&rlz=1C1GGRV_enIN865IN866&sxsrf=ALeKk03uOSKxP2_XwbEHf25NLgRUA_Vksw%3A1595876959287&ei=XyYfX9STEZiR4-EP6riy8Aw&q={query}&oq={query}+&gs_lcp=CgZwc3ktYWIQAxgAMgQIIxAnMgcIABCxAxBDMgUIABCxAzIICAAQsQMQgwEyBwguELEDEEMyCAgAELEDEIMBMgQILhBDMgUIABCxAzIFCAAQsQMyAggAOgcIIxCwAxAnOg0ILhCxAxCDARCwAxBDOgkIABCwAxAHEB46CAgAELEDELADOgsIABCxAxCDARCwAzoFCAAQsANQ288BWNvPAWCN4gFoBHAAeACAAagCiAGoApIBAzItMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab")

