import pyttsx3 #pip install pyttsx3
import speech_recognition as voice #pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes


engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id);
name= "Manikantasripadi"
assistant_name= "neo"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    wsp= ''
    if hour>=0 and hour<12:
        wsp= "Good Morning!"

    elif hour>=12 and hour<18: 
         wsp= "Good Afternoon!"
    else: 
        wsp= "Good Evening!"

    speak(wsp+" I am "+ assistant_name +" . How can I help you")       


def takeCommand(int):
    #It takes microphone input from the user and returns string output

    r = voice.Recognizer()
    with voice.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"{name} said: {command}\n")
    except Exception as e:
        #print(e) 
        return None
    if int == 1:
        return command.lower()
    else :
       return command.upper()
    


def sendEmail(to, content):
    server = smtplib.SMTP('mail.smtp2go.com', 25)
    server.ehlo()
    server.starttls()
    server.login('smtp@neoistone.com', 'QWERvbn@123')
    server.sendmail('noreplay_ai@neoistone.com', to, content)
    server.close()

def Searching_wikipedi(query) :
      if query is not None:
          results = wikipedia.summary(query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        command = takeCommand(1)
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'who the heck is' in command:
            Searching_wikipedi(command.replace('who the heck is', ''))
        elif 'date' in command:
            speak('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif "open youtube" == command:
            webbrowser.open("https://youtube.com")
        elif "open google" == command:
            webbrowser.open("https://google.com")
        elif "send a mail" in command:
            speak("who i sent mail say email address " + name + " bro.")
            email = takeCommand(1);
            speak("What should I say in email ?")
            command = takeCommand(1);
            speak("sending email to "+email)
            try :
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
               speak("Sorry my dear friend I am not able to send this email")  
        elif "bye" in command:
            exit()
        else:
            if None is not command: 
                Searching_wikipedi(command)
            else:
              pass
