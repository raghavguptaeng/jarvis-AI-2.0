#-- a virtual assistant to help you . his name is jarvis --------------------------------------------
# --- version 2.0 -----------------------------------------------------------------------------------
# Whats new ?----------------------------------------------------------------------------------------
#=1).- added right swipe feature for tinder ---------------------------------------------------------
#=2).- added a function to take small notes ---------------------------------------------------------
#=3).- added exit function to exit the assistant when command is given ------------------------------
#=4).- added a function to tell the commands given on a particular date -----------------------------
#--- DEVELOPED BY - RAGHAV GUPTA --------------------------------------------------------------------
#--- contact - raghavgermany@gmail.com or E19CSE258@bennett.edu.in ----------------------------------
#-------------- THANKS FOR YOUR SUPPORT -------------------------------------------------------------
from datetime import datetime
import pyttsx3
import speech_recognition as speech
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
from pynput.mouse import Button, Controller
import time
from selenium.webdriver.common.keys import Keys
#---------- OUR PROGRAM STARTS FROM HERE ------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#-------- the following function will take voice command from the user ------------------------------
def takeCommand():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
#----------------------------------------------------------------------------------------
# -- setting up voice engines -----------------------------------------------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# ---------------------------------------------------------------------------------------
# ----- the following function will give the speech output from device ------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return 0
# ---------------------------------------------------------------------------------------
# ---------- the following function will wish you in the begning ------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    elif hour >= 18 and hour < 20:
        speak("Good Evening!")
    else:
        speak("Good Night")
    speak('I am Jarvis Sir.Your personal assistant. Please tell me how may I help you')
# ---------------------------------------------------------------------------------------
# ------------ the followinfg function will send the mail to a person on command---------
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    return 0;
# ---------------------------------------------------------------------------------------
# ------- the following function will perform tinder right swipe ------------------------
def tinder(num):
    mouse = Controller()
    driver = webdriver.Chrome(r"C:\Users\RAGHAV GUPTA\PycharmProjects\jarvis AI v2.0\chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.get("https://tinder.com")
    driver.fullscreen_window()
    time.sleep(3)
    mouse.position = (647, 503)
    mouse.click(Button.left, 1)
    time.sleep(30)
    mouse.position = (1000, 700)
    opt = random.randint(4)
    for i in range(num):
        mouse.click(Button.left, 1)
        time.sleep(opt)
    driver.quit()
#----------------------------------------------------------------------------------------
#-------- the following function will take a short note from user -----------------------
def takenote():
    note = takeCommand()
    note='\n'+note+' '+"{:%B %d, %Y}".format(datetime.now())
    file=open('notes.txt','a')
    file.write(note)
#----------------------------------------------------------------------------------------
#-the following function will tell us the note which was to be remembered by the assistant
def tellnote():
    speak(' sir for what date you want the note for ?')
    date = takeCommand()
    file = open('notes.txt','r')
    notetoken=0
    for i in file:
        if date in i:
            notetoken = 1
            speak(i)
            break
    if notetoken == 0:
        speak('sorry sir , no notes found for the given date ')
#------------------------------------------------------------------------------------------
#-------- following function is used for searching of a particular query on google --------
def search(query):
    driver = webdriver.Chrome(r'C:\Users\RAGHAV GUPTA\PycharmProjects\automation\drivers\chromedriver.exe')
    driver.set_page_load_timeout(10)
    driver.get('https://www.google.com')
    driver.fullscreen_window()
    driver.find_element_by_name("q").send_keys(query)
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
#---------------------------------------------------------------------------------------
#--------- following is the display of the assistant menu ------------------------------
def display():
    print('\t\t\t WELCOME TO JARVIS ASSISTANT\n')
    print('\t You can give the following commands to assistant \n')
    print('\t- take notes for me')
    print('\t- search dogs on google')
    print('\t- open google ')
    print('\t- open youtube')
    print('\t- lets start swiping tinder ')
    print('\t- tell me the current time ')
    print('\tMANY MORE FEATURES COMMING SOON')
# --------------------------------------------------------------------------------------
#-------- THE EXECUTION OF MAIN FUNCTION STARTS FROM HERE ------------------------------
def main():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "enter the senders email id here "
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")
        elif 'search' in query:
            speak(" what shall i search for you ? ")
            quer = takeCommand()
            search(quer)
        elif 'tinder' in query:
            speak('sir , how many right swipes you want ?')
            number = takeCommand()
            speak(' sir , you have to manually enter the login id and password of your tinder account ')
            tinder(number)
        elif 'exit' in query:
            speak(' it was nice talking to you sir , we will meet soon ')
            return (0)
        elif 'take notes' in query:
            speak('shure sir , what would you like me to take in note ?')
            takenote()
        elif ' tell note' in query:
            tellnote()
#------these are function calls for execution of program -------------------------
#---------------------------------------------------------------------------------
display()
main()
#-------------- THANKS FOR TESTING ME --------------------------------------------