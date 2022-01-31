import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say('I am your Alexa')
engine.say('What can I do for you?')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
            else:
                talk('My name is Alexa!')
                # engine.say('My name is alexa!')
    except:
        pass
    return command

def run():
    command=takeCommand()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The time is now'+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person=command.replace('what is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        command=command.replace('open','')
        web=webbrowser.open('google.com')
        talk('Opening'+command)
    elif 'open youtube' in command:
        command=command.replace('open','')
        web=webbrowser.open('youtube.com')
        talk('Opening'+command)
    else:
        talk('I couldnt understand it')

while True:
    run()