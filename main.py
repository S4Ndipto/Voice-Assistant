import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import requests
import datetime
import random
import songs
import operations

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def tell_day():
    day = datetime.datetime.now().strftime("%A")
    speak(f"Today is {day}.")

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}.")



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "tell me a joke" in c.lower():
        tell_joke()

    elif "what is the day" in c or "day today" in c:
        tell_day()

    elif "what is the time" in c or "current time" in c:
        tell_time()

    elif "roll a dice" in c or "roll dice" in c:
        operations.roll_dice()

    elif "flip a coin" in c:
        operations.flip_coin()

    elif "calculate" in c:
        expression = c.replace("calculate", "").strip()
        operations.calculator(expression)

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = songs.music[song]
        webbrowser.open(link)

    elif "check palindrome" in c:
        operations.isPalindrome()

    elif "exit" in c:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I don't understand that command.")
    return True

if __name__ == "__main__":
    speak("Initializing Steve...")
    while True:

        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio=r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            # Listen for wake word, obtain audio from microphone
            if(word.lower() == "hello steve"):
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Steve is active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    #processCommand(command)
                    should_continue = processCommand(command)
                    if not should_continue:
                        break

        except Exception as e:
            print("Error; {0}".format(e))

