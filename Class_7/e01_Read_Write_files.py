'''
Para manipular archivos en python:

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default) XXX
    'w'       open for writing, truncating the file first XXX SI ABRIMOS CON W PERDEMOS LO QUE HABIA ANTES
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists XXX
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
'''

"""
TRABAJANDO CON ARCHIVOS DE TEXTO
"""

# Leemos readme.txt
file = open("readme.txt", "r")  # utilizamos la funcion open para abrir el archivo. El primer parametro es el nombre del archivo, el segundo es el modo de apertura
# Cuando ejecuto un archivo de python, el path es el mismo que el archivo, por eso no hace falta poner la ruta completa

# Con un for puedo recorrer el archivo linea por linea
for line in file.readlines():  # con file.readlines() leo todas las lineas del archivo y las guardo en una lista
    if line.startswith("* **"):
        print(line)

file.close()  # Se debe cerrar el archivo cuando terminamos de usarlo para liberar recursos

"""
TRABAJANDO CON CSV y WRITE
"""


file = open("miprueba.csv", "w")  # Abrimos el archivo en modo escritura y vemos qué sucede

# Escribimos el archivo
header = ["nombre", "apellido", "dni", "edad"]
data = {"nombre": "matias",
        "apellido": "rodriguez",
        "dni": 28282828,
        "edad": 33}

# Debugeamos el codigo y vemos qué sucede
for titulo in header:
    file.write(titulo+",")  # Escribimos el titulo de cada columna
    print(file.tell())  # Con file.tell() podemos ver en qué byte estamos parados

# Lo que quiero hacer ahora es borrar la ultima coma
file.seek(file.tell()-1)  # Con file.seek() puedo mover el puntero a la posicion
file.write("\n")

# Escribimos los datos
for titulo in header:
    file.write(str(data[titulo])+",")

# Nuevamente borramos la ultima coma
file.seek(file.tell()-1)
file.write("\n")

# Cerramos el archivo
file.close()

"""
TRAJABANDO CON CSV y APPEND
"""
file = open("miprueba.csv", "a+")  # Con el a+ abrimos el archivo en modo append, es decir, agregamos datos al final del archivo

line = ""
for titulo in header:
    line += str(data[titulo])+","  # Concatenamos los datos en una linea

line = line[:-1]  # Borramos la ultima coma
file.writelines([line])  # Escribimos la linea en el archivo y le agrega un salto de linea

file.close()


"""
TRABAJAMOS CON CSV Y CON LA LIBRERIA CSV

Vemos el archivo tickbytick.csv
"""

import csv

data = {}

# Con with open() no hace falta cerrar el archivo ya que se cierra automaticamente al salir del bloque
with open("tickbytick.csv") as csvfile:  # le asignamos el nombre csvfile al archivo

    # Hay dos formas de leer un archivo csv, como lista o como diccionario

    # Lista
    hh = csv.reader(csvfile)  # con csv.reader() leo el archivo y lo guardo en una lista
    for line in hh:
        head = line  # que me queda en head?
        break

    # OJO CON EL PUNTERO! Ahora ya no estamos en la primera linea, sino en la segunda

    # Diccionario
    reader = csv.DictReader(csvfile, head)  # con csv.DictReader() leo el archivo y lo guardo en un diccionario

    # Vamos a contar el volumen de cada instrumento operado y el precio promedio
    for row in reader:
        if not row["Posición"] in data:  # si el instrumento no esta en el diccionario, lo agrego
            data[row["Posición"]] = {"precio": 0, "volumen": 0, "cantidad": 0}  # inicializo el diccionario

        data[row["Posición"]]["cantidad"] += 1  # Cada vez que aparece el instrumento, sumo 1 a la cantidad

        # Cuando leo el csv, los datos son strings, por lo que debo convertirlos a float o int
        data[row["Posición"]]["precio"] += float(row["Precio"])  # Sumo el precio
        data[row["Posición"]]["volumen"] += int(row["Volumen"])  # Sumo el volumen

    for value in data.values():
        value["precio"] = round(value["precio"]/value["cantidad"])

print("{0:10} {1:10} {2:10} {3:10}".format("Instrumento","Precio Promedio","Volúmen","Cantidad op"))
for k,v in data.items():
    print("{0:12} {precio:>10} {volumen:>10} {cantidad:>10}".format(k, **v))
    print("{0:12} {precio:>10} {volumen:>10} {cantidad:>10}".format(k, precio=v["precio"], volumen=v["volumen"], cantidad=v["cantidad"]))

"""
ESCRIBIMOS UN ARCHIVO CSV
"""

# Hacemos un almacen de productos, no vemos el codigo.
import random
import csv
productos = ["Leche", "Pan", "Chocolate", "Vino", "Manteca", "Cerveza"]

almacen = {"A"+str(indice): {"nombre": producto,
                             "precio": random.randint(50*(indice+1), 400),
                             "descuento": random.randint(10, 20)/100,
                             "impuesto": random.randint(10, 21)/100} for indice,producto in enumerate(productos)}

# Escribimos el archivo
with open("productos.txt", 'w') as productos:  # abrimos el archivo en modo escritura

    # genero el header
    header = list(almacen.values())[0]  # obtengo el primer valor del diccionario almacen

    writer = csv.DictWriter(f=productos, fieldnames=header)  # con csv.DictWriter() escribimos el archivo
    # el primer parametro es el archivo, el segundo es el nombre de las columnas

    writer.writeheader()  # escribimos el header
    writer.writerows(list(almacen.values()))  # escribimos los datos, le pasamos una lista de diccionarios
