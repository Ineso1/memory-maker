#Necesita tener previemente descargadas las librerias pyytsx3, pywhatkit, speech recognition en el entorno

import speech_recognition as sr
import pyttsx3, pywhatkit
from clases_ob import *
from Inspector_csv import *

"""
    Librerias importadas y creadas

    *   pyttsx3 ----> Conversor de texto a voz
    *   speech recognition ----> Convierte audio a texto 
    *   clases_ob ----> Clases de objetos programados 
                            +Hora
                            +Dia
                            +Tiempo
                            +Recuerdo
    *   Inspector_csv ----> Carga y guarda archivo csv 
    *   pyehatkit ----> Manda mensajes de whats y reproduce titulos en youtube
"""

#  -----Declaracion de lista par crear matriz (variable global)-----

registro_recuerdos = []

#   -----Carga la matriz en una lista vacia-----

def cargar_archivos():
    cargarMatriz(Recuerdos_csv,registro_recuerdos)

#   -----Busca elementos en una columna dada de una matriz (strings)-----
#   Regresa el id del elemento en la matriz
#   Regresa -1 si no exite en la matriz 


def buscar_elemento(matriz, columna, valor):
    id_elemento = -1
    for x in range(len(matriz)):
        if valor == matriz[x][columna].upper():
            id_elemento = x
            break
        else:
            id_elemento = -1
    return id_elemento


#   -----Anade y registra recuerdo-----
#   Anade el recuerdo a la matriz de memoria temporal
#   Registra en el archivo de memoria csv

def registro_recuerdo(recuerdo):
    
    registro_recuerdo_anadir = [recuerdo]
    registro_recuerdos.append(registro_recuerdo_anadir)
    guardarMatriz(Recuerdos_csv,registro_recuerdos)
    print("Recuerdo guardado")


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

# -----Funcion general (menu provicional)----
def run_Nessy():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciondo " + music)
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)

if __name__ == '__main__':
    run_Nessy()



    