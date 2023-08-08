from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime

root = Tk()
root.geometry("500x500")

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak("como puedo ayudarte?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='es-mx')
        except sr.UnknownValueError:
            print('no entendi, podrias decirlo de nuevo?')

    respond(voice_data)

def respond(voice_data):
    print(voice_data)
    if "nombre" in voice_data:
        speak("mi nombre es Hubert Blaine Wolfe­schlegel­stein­hausen­berger­dorff Sr")
        print("mi nombre es Hubert Blaine Wolfe­schlegel­stein­hausen­berger­dorff Sr")

    if "hora" in voice_data:
        speak("la hora actual es")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)

    if "gato" in voice_data:
        speak("hola chayanne")
        print("hola chayanne")
r_audio()

btn = Button(text = "iniciar", command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()