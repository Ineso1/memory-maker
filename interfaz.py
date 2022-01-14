import tkinter as tk
from tkinter import *
from tkinter import ttk
from Inspector_csv import *
from clases_ob import *
"""
    *   Alias de libreria tkinter ----> tk
    *   ttk se importa para uso de funciones extras de tkinter
"""

"""

Inicio de la interfaz del asistente personal
se trata de probar las clases creadas y el resto del codigo de guardado de recuerdos en archivo csv

Se tiene un error en la funcion get fecha en la clase de ---> recuerdo ---> tiempo 

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



"""--------------------------------------------------------------------------"""





class Interfaz:
    
    #   ----Inicializacion de interfaz inicial----
    def __init__(self, _ventana):

        self.ventana = _ventana
        self.ventana.title("Asistente personal")
        #self.ventana.resizable(0,0)

        #   ----Creacion de variable de caja de registro recordatorio----
        inicio = LabelFrame(self.ventana,text = "Recordatorio")
        inicio.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #   ----Asignacion de textos y cajas de texto a caja de registro de recordatorio----
        #   Asunto
        Label(inicio, text = "Asunto").grid(row = 1, column = 0, sticky = W)
        self.asunto = Entry(inicio)
        self.asunto.focus()
        self.asunto.grid(row = 1, column = 1)

        #   Hora Programada ---> Hora
        Label(inicio, text = "Hora Programada (hr:min)").grid(row = 2, column = 0, sticky = W)
        self.hora_programada_hr = Entry(inicio)
        self.hora_programada_hr.grid(row = 2, column = 1)
        #   Hora programada ---> Minutos
        Label(inicio, text = ":").grid(row = 2, column = 2, sticky = W)
        self.hora_programada_min = Entry(inicio)
        self.hora_programada_min.grid(row = 2, column = 3)
        #   Hora programada ---> dia
        Label(inicio, text = "dia").grid(row = 1, column = 5)
        Label(inicio, text = ",  ").grid(row = 2, column = 4, sticky = W)
        self.hora_programada_dia = Entry(inicio)
        self.hora_programada_dia.grid(row = 2, column = 5)
        #   Hora programada ---> mes
        Label(inicio, text = "mes").grid(row = 1, column = 7)
        Label(inicio, text = " / ").grid(row = 2, column = 6, sticky = W)
        self.hora_programada_mes = Entry(inicio)
        self.hora_programada_mes.grid(row = 2, column = 7)
        #   Hora programada ---> anio
        Label(inicio, text = "anio").grid(row = 1, column = 9)
        Label(inicio, text = " / ").grid(row = 2, column = 8, sticky = W)
        self.hora_programada_anio = Entry(inicio)
        self.hora_programada_anio.grid(row = 2, column = 9)

        #   Alarma
        Label(inicio, text = "Alarma").grid(row = 3, column = 0, sticky = W)
        self.alarma_hr = Entry(inicio)
        self.alarma_hr.grid(row = 3, column = 1)
        #   Alarma ---> Minutos
        Label(inicio, text = ":").grid(row = 3, column = 2, sticky = W)
        self.alarma_min = Entry(inicio)
        self.alarma_min.grid(row = 3, column = 3)
        #   Alarma ---> dia
        Label(inicio, text = ",  ").grid(row = 3, column = 4, sticky = W)
        self.alarma_dia = Entry(inicio)
        self.alarma_dia.grid(row = 3, column = 5)
        #   Alarma ---> mes
        Label(inicio, text = " / ").grid(row = 3, column = 6, sticky = W)
        self.alarma_mes = Entry(inicio)
        self.alarma_mes.grid(row = 3, column = 7)
        #   Alarma ---> anio
        Label(inicio, text = " / ").grid(row = 3, column = 8, sticky = W)
        self.alarma_anio = Entry(inicio)
        self.alarma_anio.grid(row = 3, column = 9)

        ttk.Button(inicio, text = "Guardar recordatorio", command = self.agregar_recuerdo).grid(row =  5, columnspan = 2, sticky = W + E)

        # Mensaje (Inicialmente invisible)
        self.mensaje = Label(text = '', fg = 'green')
        self.mensaje.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)


    def validacion_recuerdo(self):
        return len(self.asunto.get()) != 0 and len(self.hora_programada_hr.get()) != 0


    def agregar_recuerdo(self):
        if self.validacion_recuerdo():
            recuerdo_generado = Recuerdo(self.asunto.get())
            recuerdo_generado.setHoraProgramada(self.hora_programada_hr.get(),self.hora_programada_min.get(),self.hora_programada_dia.get(),self.hora_programada_mes.get(),self.hora_programada_anio.get())
            if self.alarma_hr != 0 or self.alarma_min != 0:
                recuerdo_generado.setAlarma(self.alarma_hr.get(),self.alarma_min.get(),self.alarma_dia.get(),self.alarma_mes.get(),self.alarma_anio.get())
            cargar_archivos()
            registro_recuerdo(recuerdo_generado.getRecuerdo())

            self.mensaje['fg'] = 'black'
            self.mensaje['text'] = 'El recordatorio {} ha sido agregado con exito'.format(self.asunto.get())
            self.asunto.delete(0, END)
            self.hora_programada_hr.delete(0, END)
            self.hora_programada_min.delete(0, END)
            self.hora_programada_dia.delete(0, END)
            self.hora_programada_mes.delete(0, END)
            self.hora_programada_anio.delete(0, END)
            self.alarma_hr.delete(0, END)
            self.alarma_min.delete(0, END)
            self.alarma_dia.delete(0, END)
            self.alarma_mes.delete(0, END)
            self.alarma_anio.delete(0, END)
        else:
            self.mensaje['fg'] = 'red'
            self.mensaje['text'] = 'Se necesita indicar el asunto y hora programada'



if __name__ == '__main__':
    ventana = Tk()
    #window.iconbitmap("beehigh.ico")
    aplication = Interfaz(ventana)
    ventana.mainloop()