'''
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
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
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

#lets open the following file for reading and print lines where methods are documented
file = open("readme.txt","r")
for line in file.readlines():
    if line.startswith("* **"):
        print(line)

file.close()

file = open("miprueba.csv","w")
header = ["nombre","apellido","dni","edad"]
data = {"nombre":"matias",
        "apellido":"rodriguez",
        "dni":28282828,
        "edad":33}

for titulo in header:
    file.write(titulo+",")
    print(file.tell())

file.seek(file.tell()-1)
file.write("\n")

for titulo in header:
    file.write(str(data[titulo])+",")

file.seek(file.tell()-1)
file.write("\n")
file.close()

file = open("miprueba.csv","a+")

line = ""
for titulo in header:
    line += str(data[titulo])+","

line = line[:-1]
file.writelines([line])
file.close()

import csv

data = {}

with open("tickbytick.csv") as csvfile:
    hh = csv.reader(csvfile)
    for line in hh:
        head = line
        break
    reader = csv.DictReader(csvfile,head)
    for row in reader:
        if not row["Posición"] in data:
            data[row["Posición"]] = {"precio":0,"volumen":0,"cantidad":0}
        data[row["Posición"]]["cantidad"] += 1
        data[row["Posición"]]["precio"] += float(row["Precio"])
        data[row["Posición"]]["volumen"] += int(row["Volumen"])

    for value in data.values():
        value["precio"] = round(value["precio"]/value["cantidad"])

print("{0:10} {1:10} {2:10} {3:10}".format("Instrumento","Precio Promedio","Volúmen","Cantidad op"))
for k,v in data.items():
    print("{0:12} {precio:>10} {volumen:>10} {cantidad:>10}".format(k,**v))
    print("{0:12} {precio:>10} {volumen:>10} {cantidad:>10}".format(k,precio=v["precio"],volumen=v["volumen"],cantidad=v["cantidad"]))

import random
import csv
productos = ["Leche","Pan","Chocolate","Vino","Manteca","Cerveza"]

almacen = {"A"+str(indice):{"nombre":producto
    ,"precio":random.randint(50*(indice+1),400)
    ,"descuento":random.randint(10,20)/100
    ,"impuesto":random.randint(10,21)/100} for indice,producto in enumerate(productos)}


with open("productos.txt",'w') as productos:
    writer = csv.DictWriter(f=productos,fieldnames=list(almacen.values())[0])
    writer.writeheader()
    writer.writerows(list(almacen.values()))

