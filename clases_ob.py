from datetime import datetime

"""
asunto -----> nombre
palabras claves -----

recordar cada cierto tiempo segun prioridad
corto, mediano, largo plazo


dia y alarma de recordatorio

"""
class tiempo:
    dia = 0
    mes = 0
    anio = 0
    hora = 0
    minuto = 0

    def __init__(self,_anio,_mes,_dia,_hora,_minuto):
        self.anio = _anio
        self.mes = _mes
        self.dia = _dia
        self.hora = _hora
        self.minuto = _minuto

    def setFecha(self, _anio, _mes, _dia):
        self.anio = _anio
        self.mes = _mes
        self.dia = _dia
    
    def setHora(self, _hora, _minuto):
        self.hora = _hora
        self.minuto = _minuto

    def getFecha(self):
        fecha = f"{self.dia},{self.mes},{self.anio} "
        instante = f"{self.hora},{self.minuto} " 
        return fecha + instante

    def setHoy(self):
        dia = datetime.datetime()
        print(dia)
        return dia


class Recuerdo:
    asunto = ""
    palabras_claves = ""
    hora_registro = ""
    anticipacion_recordatorio = ""
    hora_programada = ""
    alarma = "" 

    def __init__(self, _asunto):
        self.asunto = _asunto
        hora_registro = datetime.now()

    def setAsunto(self, _asunto):
        self.asunto = _asunto

    def setAnticipacion(self, _anticipacion_recordatorio):
        self.anticipacion_recordatorio = _anticipacion_recordatorio
        
    def setHoraProgramada(self, _hora_programada):
        self.hora_programada = _hora_programada
    
    def setAlarma(self, _alarma):
        self.alarma = _alarma


