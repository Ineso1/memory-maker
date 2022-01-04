import csv

#Variables globales .....................................

Recuerdos_csv = "Archivos_memoria/Recuerdos.csv"

#........................................................

#Genera matriz a partir de un archivo
#Parametro de ----->>  || archivo.csv inicio || nombre de matriz||

def cargarMatriz(archivo_de_convercion,matriz_generada):
    archivo_a_convertir = open(archivo_de_convercion)
    contenido = archivo_a_convertir.readlines()
    for line in contenido:
        matriz_generada.append(line.upper().strip().split(','))
    archivo_a_convertir.close()

#Guarda matriz modificada 
#parametro de ------>> || archivo.csv destino || matriz modificada 
def guardarMatriz(archivo_a_guardar,matriz_generada_guardar):
    string_content = ""
    for lines in matriz_generada_guardar:
        for idx, element in enumerate(lines):
            if idx == len(lines) -1:
                string_content += str(element) + '\n'
            else:
                string_content += str(element) + ','

    string_content = string_content.strip()
    archivo_productos = open (archivo_a_guardar, 'w')
    archivo_productos.write(string_content)
    archivo_productos.close()