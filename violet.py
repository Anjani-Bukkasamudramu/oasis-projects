import pyttsx3
import datetime
import wikipedia
import subprocess
import webbrowser
import pywhatkit as wk
import os
import cv2
import pyautogui
import time
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r=sr.Recognizer()

    while True:
        with  sr.Microphone() as source:
            print("Listening")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
            return query.lower()

        except Exception as e:
            print("please say it again", e)
            return "None"
    
 
def username():
    speak("What should I call you, mam?")
    uname = takeCommand()
    if uname.lower() != 'none':
        speak("Welcome, Miss " + uname)
    else:
        speak("I'm sorry, I didn't catch your name.")
        username()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Mam")
    elif 12 <= hour < 18:
        speak("Good Afternoon Mam")
    else:
        speak("Good Evening Mam") 
    speak("I am your virtual assistant violet")

def open_in_browser(url, browser='chrome'):
    try:
        if browser.lower() == 'brave':
            subprocess.Popen([r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe', url])
        else:
            webbrowser.open(url)
    except Exception as e:
        print(f"Error opening in {browser}: {e}")

if __name__ == "__main__":
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()  
        
        if 'violet' in query:
            response="yes mam"
            print(response)
            speak(response)

        elif 'just open google' in query:
           open_in_browser('https://www.google.com', browser='brave')

        elif 'just open youtube' in query:
            open_in_browser('https://www.youtube.com', browser='brave')
           
        elif 'search on google' in query:
           speak("What should I search?")
           search_query = takeCommand().lower()
           search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
    
           webbrowser.open(search_url)
    
           try:
               results = wikipedia.summary(search_query, sentences=2)
               speak(results)
           except wikipedia.exceptions.DisambiguationError as e:
               speak("I found multiple results. Please be more specific.")
           except wikipedia.exceptions.PageError as e:
               speak("I'm sorry, but I couldn't find any information on that topic.")

        elif 'open youtube' in query:
            speak("What would you like to watch?")
            video_query = takeCommand().lower()
            wk.playonyt(f"{video_query}")

        elif 'search on youtube' in query:
            query=query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")


        elif 'who are you' in query:
            response='my name is violet'
            print(response)
            speak(response)
            print('I can do everything that my creator programmed me to do')
            speak('I can do everything that my creator programmed me to do')

        elif 'who created you' in query:
            response='I dont know her name I am created with python language in visual studio code'
            print(response)
            speak(response)

        elif 'how are you' in query:
            response = "I don't have feelings, but I'm here and ready to assist you. How can I help?"
            print(response)
            speak(response)

        elif 'what can you do' in query:
            response = "I can perform tasks for you"
            print(response)
            speak(response)
        
        elif 'what are my system specifications' in query:
            response="device name LAPTOP-EU6FGMJK , RAM 8.00 GB (7.85 GB usable)  system type 64-bit operating system, x64-based processor , No pen or touch input is available for this display "
            print(response)
            speak(response)
        
        elif 'ok' in query:
            response="anything else I can help you with"
            print(response)
            speak(response)

        elif 'thank you' in query:
            response = "You're welcome! If you have any more questions or need assistance, feel free to ask."
            print(response)
            speak(response)

        elif 'bye' in query:
            response = "bye ! have a good day"
            print(response)
            speak(response)

        elif 'what is' in query:
            try:
              speak("Searching Wikipedia...")
              query = query.replace("what is", "").strip()
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
              speak("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
              speak("I'm sorry, but I couldn't find any information on that topic.")

        elif 'who is' in query:
            try:
              speak("Searching Wikipedia...")
              query = query.replace("who is", "").strip()
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
              speak("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
              speak("I'm sorry, but I couldn't find any information on that topic.")

        elif 'where is' in query:
            try:
              speak("Searching Wikipedia...")
              query = query.replace("where is", "").strip()
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
              speak("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
              speak("I'm sorry, but I couldn't find any information on that topic.")

        elif 'close browser' in query:
            os.system("taskkill/f /im brave.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            os.system("taskkill/f /im cmd.exe")
        
        elif 'exact time now' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is {strTime}")


        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        
        elif 'lock the system' in query:
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif 'volume up' in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        
        elif 'volume down' in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            
        elif 'mute' or 'unmute' in query:
            pyautogui.press("volummemute")

        elif 'open camera' in query:
           cap = cv2.VideoCapture(0)
           if not cap.isOpened():
             print("Error: Unable to access the camera.")
             speak("Sorry, I'm unable to access the camera at the moment.")
           else:
              while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                   break
              cap.release()
              cv2.destroyAllWindows()

        
        elif'take screenshot' in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")
              
        else:
          print("...")

        




            


