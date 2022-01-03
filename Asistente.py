#Necesita tener previemente descargadas las librerias pyytsx3, pywhatkit, speech recognition en el entorno

import speech_recognition as sr
import pyttsx3, pywhatkit
from clases_ob import *

"""
    *   pyttsx3 ----> Conversor de texto a voz
    *   speech recognition ----> Convierte audio a texto 
    *   clases_ob ----> Clases de objetos programados 
                            +Hora
                            +Dia
                            +Tiempo
                            +Recuerdo
    *   pyehatkit ----> Manda mensajes de whats y reproduce titulos en youtube
"""

# -----Nombre del asistente-----
Nombre_asistente = "yo" 

# -----Objeto listener y engine----- 
oido = sr.Recognizer()
Conversor_voz = pyttsx3.init()

# -----Propiedades de la voz del asistente----- 
voices = Conversor_voz.getProperty('voices')
Conversor_voz.setProperty('voice', voices[0].id)

# -----Funcion voz del asistente-----
def talk(text):
    Conversor_voz.say(text)
    Conversor_voz.runAndWait()

# -----Funcion para escuchar al usuario-----
def listen():
    try:                                        # ---Try-catch
        with sr.Microphone() as source:
            print("\nEscuchando... \n")
            pc = oido.listen(source)
            rec = oido.recognize_google(pc)
            rec = rec.lower()
            if Nombre_asistente in rec:
                rec = rec.replace(Nombre_asistente, '')
    except:
        pass

    return rec

# -----
def run_Nessy():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciondo " + music)
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)

if __name__ == '__main__':
    run_Nessy()



    