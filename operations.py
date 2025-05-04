import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def isPalindrome():
    speak("Tell the number or word")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit= 3)
        word = r.recognize_google(audio)
    l, r = 0, len(word)-1
    while l<=r:
        if word[l] == word[r]:
            l+=1
            r-=1
        else:
            speak("It is not palindrome")
            return
    speak("It is palindrome")

def calculator(query):
    try:
        result = eval(query)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't calculate that.")

def roll_dice():
    number = random.randint(1, 6)
    speak(f"You rolled a {number}")

def flip_coin():
    result = random.choice(["Heads", "Tails"])
    speak(f"It's {result}")