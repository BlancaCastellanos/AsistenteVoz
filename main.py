import speech_recognition as sr 
import time 
from time import ctime 
import webbrowser
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('I am sorry, i did not understand you')
        except sr.RequestError:
            alexa_speak('I am sorry, conection error')
        return voice_data


def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang="es")
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('My name is Jimena')
    if 'what time is it'in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        buscar = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('This is what i found for: ' + buscar)
    if "place" in voice_data:
        lugar = record_audio("What place do you want to look?")
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        alexa_speak('This is what i found for: ' + lugar)
    if 'favorite color' in voice_data:
        alexa_speak('My favorite color is gray')
    if 'favorite food' in voice_data:
        alexa_speak('My favorite food is hamburguers')
    if 'bye' in voice_data:
        exit()

time.sleep(1)
alexa_speak('How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)