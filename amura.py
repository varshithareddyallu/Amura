import openai
import speech_recognition as sr
import webbrowser
import pyttsx3
import sys

import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


system_content = "You are a virtual assistant named Amura skilled in general tasks like Alexa and Google Cloud. Give short responses please"
# user_content=input("enter")
def abcd(c):
       
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
        elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
        elif "open games" in c.lower():
            webbrowser.open("https://poki.com/")
        elif "open whatsapp web" in c.lower():
            webbrowser.open("https://web.whatsapp.com")
        elif "open flipkart" in c.lower():
            webbrowser.open("https://www.flipkart.com")
        elif "open snapchat" in c.lower():
            webbrowser.open("https://www.snapchat.com")
        elif "open instagram" in c.lower():
            webbrowser.open("https://www.instagram.com")
        elif "open today's weather" in c.lower():
            webbrowser.open("https://weather.com")
        elif c.lower().startswith("play"):
            song = c.lower().split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)

       
        
        
        else:
            client = openai.OpenAI(
        api_key="3dbc9049208040b7b382ea93ba60beae",
        base_url="https://api.aimlapi.com",
)

        chat_completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": c},
            ],
            temperature=0.7,
            max_tokens=128,
        )

        response = chat_completion.choices[0].message.content

        speak(response) 
        print("AI/ML API:\n", response)


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

if __name__ == "__main__":

    speak("Initializing amura....")
    speak("hello how can i help you today")
    while True:
        # Listen for the wake word "Amura"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=15, phrase_time_limit=10)
            word = r.recognize_google(audio)
            if(word.lower() == "amura"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("amura Active...")
                    audio = r.listen(source)
                    user_content = r.recognize_google(audio)
                    print(user_content)
                    abcd(user_content)
                    

                    


        except Exception as e:
            print("Error; {0}".format(e))