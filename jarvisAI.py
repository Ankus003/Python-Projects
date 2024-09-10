import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Set the voice to the first one in the list
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# Function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice command from user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Command Sir!")
        r.pause_threshold = 1
        
        # Adjust the timeout and phrase_time_limit as needed
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Timeout; no speech detected.")
            speak("Sorry Lord, I didn't hear anything. Please try again.")
            return None

    try:
        print("Analyzing the speech..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except sr.UnknownValueError:
        print("Could not understand the audio.")
        speak("Sorry Lord, I didn't understand. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry Lord, I'm unable to reach the recognition service. Please try again.")
        return None
    
    return query

# Function to wish the user
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis. Command Me")
    
 
#send email
def sendEmail(to, content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('ankushmazumdar003@gmail.com', 'xhfr odym dnmv fkvw')
    server.sendmail('ankushmazumdar003@gmail.com', to, content)
    server.close()

    
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand()
        if query:
            query = query.lower()

            if "open notepad" in query:
                npath = "C:\\Windows\\notepad.exe"
                os.startfile(npath)
                
            elif "open command prompt" in query or "open cmd" in query:
                os.system("start cmd")
                speak("Command Prompt opened.")
                
            elif "open adobe reader" in query:
                mpath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader XI.lnk"
                os.startfile(mpath)
                
            elif "ip address" in query:
                ip= get("https://api.ipify.org").text
                speak(f"your IP Address is {ip}")
                
            elif "wikipedia" in query:
                speak("Searching Wikipedia")
                query= query.replace("wikipedia","")
                results= wikipedia.summary(query, sentences= 7)
                speak("According to wikipedia")
                speak(results)
                print(results)
                
            elif "open camera" in query or "take picture" in query:
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    speak("Error: Camera not found or not accessible.")
                    print("Error: Camera not found or not accessible.")
                    continue
                speak("Camera is now open. Say 'capture picture' to take a photo.")
                while True:
                    ret, img = cap.read()
                    if not ret:
                        speak("Error: Failed to grab frame.")
                        print("Error: Failed to grab frame.")
                        break
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(1)
                    if k == 27:  # Esc key to exit
                        break
                    command = takecommand()
                    if command and "capture picture" in command.lower():
                        filename = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.jpg')
                        cv2.imwrite(filename, img)
                        full_path = os.path.abspath(filename)
                        speak(f"Picture captured and saved as {full_path}")
                        print(f"Picture captured and saved as {full_path}")

                cap.release()
                cv2.destroyAllWindows()

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

            elif "open stack overflow" in query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in query:
                speak("Sir what do you want to search on google")
                cm= takecommand().lower()
                if cm:
                    webbrowser.open(f"https://www.google.com/search?q={cm}")

            elif "send whatsapp message" in query:
                kit.sendwhatmsg("+919031778900", "Hi", 21, 30)
                speak("WhatsApp message scheduled successfully.")

            elif "play songs on youtube" in query:
                kit.playonyt("see you again")

            elif "email to maa" in query:
                try:
                    speak("what should I say?")
                    content= takecommand().lower()
                    to= "montimazumdar1221@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent to maa")
                except Exception as e:
                    print(e)
                    speak("sorry sir I am not able to sent this mail to maa")

            elif "no thanks" in query:
                speak("Thanks for using me sir! Please command again!")
                sys.exit()
            speak("sir do you have any other work?")
                

            
