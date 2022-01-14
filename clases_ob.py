from datetime import datetime
import json
import os

"""
asunto -----> nombre
palabras claves -----

recordar cada cierto tiempo segun prioridad
corto, mediano, largo plazo


dia y alarma de recordatorio

"""

#   Variable global de la fecha actual

hoy = datetime.now()


#   Clase Hora y dia -------------------------------------------------- 
#   Setter de hora contiene cambio de hora y minutos
#   Setter de dia contiene cambio de dia, mes y año

class Hora:
    hr = hoy.strftime("%H")
    minutos = hoy.strftime("%M")

    def __init__(self):
        self.hr = hoy.strftime("%H")
        self.minutos = hoy.strftime("%M")

    def setHora (self, _hr,_minutos):
        self.hr = _hr
        self.minutos = _minutos
    
    def getHora (self):
        return f"{self.hr}:{self.minutos}"

    def imprimirHora (self):
        print(f"{self.hr} : {self.minutos}")

class Dia:
    d = hoy.strftime("%d")
    mes = hoy.strftime("%m")
    anio = hoy.strftime("%Y")

    def __init__(self):
        self.d = hoy.strftime("%d")
        self.mes = hoy.strftime("%m")
        self.anio = hoy.strftime("%Y")

    def setDia(self, _d, _mes, _anio):
        self.d = _d
        self.mes = _mes
        self.anio = _anio

    def getDia (self):
        return f"{self.d}/{self.mes}/{self.anio}"

    def imprimirDia(self):
        print(f"{self.d} / {self.mes} / {self.anio}")

#   Clase tiempo -------------------------------------------------- 


class Tiempo:
    dia = Dia() 
    hora = Hora()

    def __init__(self):
        pass

    def setFecha(self, _hora, _minuto, _dia, _mes, _anio):
        self.dia.setDia(_dia, _mes, _anio)
        self.hora.setHora(_hora,_minuto)

    def setDia(self, _dia, _mes, _anio):
        self.dia.setDia(_dia, _mes, _anio)
    
    def setHora(self, _hora, _minuto):
        self.hora.setHora(_hora,_minuto)

    def getTiempo(self):
        return f"{self.dia.getDia()},{self.hora.getHora()}"

    def imprimirTiempo(self):
        print(f"{self.dia.getDia()},{self.hora.getHora()}")


#   Clase Recuerdo --------------------------------------------------

class Recuerdo:
    asunto = "none"
    palabras_claves = "none"
    hora_registro = Tiempo()
    anticipacion_recordatorio = Hora()
    hora_programada = Tiempo()
    alarma = Tiempo() 

    def __init__(self, _asunto):
        self.anticipacion_recordatorio.setHora(13,0)
        self.asunto = _asunto
        self.hora_registro = Tiempo()
        self.hora_programada = Tiempo()
        self.alarma = Tiempo() 
        

    def setAsunto(self, _asunto):
        self.asunto = _asunto

    def setAnticipacion(self, _anticipacion_recordatorio_hora, _anticipacion_recordatorio_minuto):
        self.anticipacion_recordatorio.setHora(_anticipacion_recordatorio_hora,_anticipacion_recordatorio_minuto)
        
    def setHoraProgramada(self, _hora_programada_hora,_hora_programada_minuto,_hora_programada_dia,_hora_programada_mes,_hora_programada_anio):
        self.hora_programada.setFecha(_hora_programada_hora,_hora_programada_minuto,_hora_programada_dia,_hora_programada_mes,_hora_programada_anio)
    
    def setAlarma(self, _alarma_hora,_alarma_minuto,_alarma_dia,_alarma_mes,_alarma_anio):
        self.alarma.setFecha(_alarma_hora,_alarma_minuto,_alarma_dia,_alarma_mes,_alarma_anio)

    def getRecuerdo(self):
        #recuerdo = f"{self.asunto},{self.hora_registro.getTiempo()},{self.anticipacion_recordatorio.getHora()},{self.hora_programada.getTiempo()},{self.alarma.getTiempo()}"
        recuerdo = f"{self.asunto},{self.hora_registro.getTiempo()},{self.anticipacion_recordatorio.getHora()},{self.hora_programada.getTiempo()},{self.alarma.getTiempo()}"
        return recuerdo

    def imprimirRecuerdo(self):
        print(f"""
        *Asunto: {self.asunto}
        *Hora programada: {self.hora_programada.getFecha()}
        *Alarma: {self.alarma.getFecha()}
        """)



#   Encoder Json -------------------------------------------------

class Recuerdo_Encoder_Json(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Recuerdo):
            return {'asunto':obj.asunto, 'hora_registro':obj.hora_registro.getTiempo(), 'hora_programada': obj.hora_programada.getTiempo(), 'alarma': obj.alarma.getTiempo(), 'anticipacion_recordatorio': obj.anticipacion_recordatorio.getHora()}
        return json.JSONEncoder.default(self, obj) 

"""
def Recuerdo_Encoder_Json_Python(diccionario):
    construccion_recuerdo = Recuerdo(diccionario['asunto'])
    return 
"""