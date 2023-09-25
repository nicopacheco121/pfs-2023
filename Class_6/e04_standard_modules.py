'''Python comes with a vast library of functions ready to use by developers'''

'''Documentacion
https://docs.python.org/3/library/index.html

Ejemplos en código
https://github.com/dhellmann/pymotw-3
'''

"""

Math

"""

import math  # importamos un modulo completo
from math import ceil  # importamos una funcion especifica
from math import pi as pie  # importamos una funcion especifica y le cambiamos el nombre
### CUIDADO si utilizamos variables con el mismo nombre que las funciones que importamos

print(math.pi)  # utilizando el nombre de la libreria y un punto, accedemos a la libreria
print(math.e)

print(ceil(11.5))  # utilizamos la funcion que importamos
print(pie)


'''
El modulo math incluye tres funciones para convertir valores de punto flotante a numeros enteros.
Cada uno toma un enfoque diferente y sera util en diferentes circunstancias.

- trunc(), saca los decimales y deja el entero
- floor() redondea al mas chico
- ceil() (techo) redondea al mas grande
'''
print(math.trunc(math.pi))
print(math.floor(math.pi))
print(math.ceil(math.pi))
print(math.trunc(-10.5050))
print(math.floor(-10.50))
print(math.ceil(-10.50))

'''
modf() devuelve una tupla con la parte decimal y la parte entera de un numero
'''

print(math.modf(2.5))
print(math.modf(8.5))
print(math.modf(-10.3))
print(math.modf(1.98772))
print(math.modf(-3.00033))
print(math.modf(0.333))

'''Decimal

Los numeros pierden precision cuando se representan como numeros flotantes.
Esto es problematico cuando se trabaja con grandes numeros o numeros que requieren una precision muy alta.

El modulo decimal proporciona soporte para numeros decimales precisos y ajustables.
Los numeros decimales pueden representarse exactamente.

Decimal values are represented as instances of the Decimal class. The constructor takes as argument one integer or string. 
Floating point numbers can be converted to a string before being used to create a Decimal, letting the caller explicitly 
deal with the number of digits for values that cannot be expressed exactly using hardware floating point representations. 
Alternately, the class method from_float() converts to the exact decimal representation.
'''
print(1.1+2.2)
nuevo_valor = round(1.1+2.2, 2)  # si uso round puedo solucionar el problema en este caso
print(nuevo_valor)

# nuevo_valor = 1.1+2.2  # si descomento esta linea, que me da el if?
if nuevo_valor > 3.3:
    print("Es mayor")
else:
    print("No es mayor")

# Si no deseo perder precision puedo utilizar decimal, el trade off es que es mas lento y algo mas complejo
import decimal
from decimal import Decimal
from decimal import Decimal as MiObjeto
decimal.getcontext().prec = 20

print(decimal.Decimal(1.1+2.2))  # si lo hago de esta manera, arrastro el problema
print(decimal.Decimal(1.1)+decimal.Decimal(2.2))  # si lo hago de esta manera, no arrastro el problema

print(decimal.Decimal('1.1')+decimal.Decimal('2.2'))
print(Decimal('1.1')+Decimal('2.2'))
# print(Decimal.from_float(1.1)+Decimal.from_float(2.2))
# MiObjeto()


'''
random

Permite generar valores aleatorios.

Si deseo testeear un algoritmo, puedo utilizar random para generar valores aleatorios y ver como se comporta mi algoritmo

'''

import random

# randrange devuelve un valor aleatorio entre el rango que le indiquemos
print(random.randrange(0, 100))

# randint devuelve un valor aleatorio entre el rango que le indiquemos, incluyendo el limite superior
print(random.randint(0, 100))


'''Seeding

random() produce valores diferentes cada vez que se llama y tiene un periodo muy largo antes de que se repitan.
Esto es util para producir valores unicos o variaciones, pero hay momentos en los que tener el mismo conjunto de datos
disponible para ser procesado de diferentes maneras es util.
Para ello podemos utilizar la funcion seed() para inicializar el generador de pseudorandom para que produzca un conjunto
de valores esperados.
Cada vez que inicializamos el generador con la misma semilla, obtenemos los mismos valores.
'''

random.seed(100)

print(random.randrange(0, 100))
print(random.randrange(0, 100))


'''
Sampling

sample me permite obtener una muestra aleatoria de una lista

'''
print(random.sample([10, 20, 30, 40, 50], k=4))


'''
Writing code to work with files on multiple platforms is easy using the functions included in the os.path module. 
Even programs not intended to be ported between platforms should use os.path for reliable filename parsing.

Parsing Paths
The first set of functions in os.path can be used to parse strings representing filenames into their component parts. 
It is important to realize that these functions do not depend on the paths actually existing; they operate solely on the strings.

Path parsing depends on a few variable defined in :mod:`os`:

os.sep - The separator between portions of the path (e.g., "/" or "\").
os.extsep - The separator between a filename and the file "extension" (e.g., ".").
os.pardir - The path component that means traverse the directory tree up one level (e.g., "..").
os.curdir - The path component that refers to the current directory (e.g., ".").
'''

"""
os

Lo utilizamos para interactuar con los archivos del sistema operativo
Cuando ejecutamos el programa, se ejecuta desde una ubicacion.
Por ejemplo puede que necesitemos abrir un archivo que esta en otro directorio.
Con os podemos saber en que ubicacion estamos y movernos a otras ubicaciones

"""

import os.path

# current directory
print(os.path.abspath(os.path.curdir))
print(os.getcwd())

# directorio padre
print(os.path.abspath(os.path.pardir))

# me muevo al directorio padre
os.chdir(os.path.pardir)

# current directory
print(os.path.abspath(os.path.curdir))


'''
time — Time access and conversions

time trabaja con el concepto de timezones, es decir, zonas horarias.

Commonly used format codes:

%Y  Year with century as a decimal number.
%m  Month as a decimal number [01,12].
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%M  Minute as a decimal number [00,59].
%S  Second as a decimal number [00,61].
%z  Time zone offset from UTC.
%a  Locale's abbreviated weekday name.
%A  Locale's full weekday name.
%b  Locale's abbreviated month name.
%B  Locale's full month name.
%c  Locale's appropriate date and time representation.
%I  Hour (12-hour clock) as a decimal number [01,12].
%p  Locale's equivalent of either AM or PM.

Other codes may be available on your platform.  See documentation for
the C library strftime function.
'''

from time import *

print(gmtime())  # gmtime() devuelve la hora en formato UTC
print(strftime("%d %B %Y %H:%M:%S %p", gmtime()))  # strftime() me permite formatear la hora

day = strptime("30/11/2000", "%d/%m/%Y")  # paso de string a time
print(day)

print(time())  # devuelve el timestamp, es decir, la cantidad de segundos desde el 1/1/1970 a las 00:00:00 UTC
# De esta forma obtengo el tiempo exacto


'''
datetime — Basic date and time types
'''

import datetime as dt

''' la libreria esta compuesta por varios tipos de datos. Los mas importantes son

datetime.datetime: una fecha y una hora
datetime.date: que es solamente una fecha
datetime.time: que es una hora
datetime.timedelta: que es el intervalo entre 2 fechas/momentos en el tiempo'''

# datetime datetime
now = dt.datetime.now()
print(now)
print(type(now))

# datetime date
today = dt.date.today()
print(today)
print(type(today))

# datetime time
now = dt.datetime.now()
print(now.time())
print(type(now.time()))


# Puedo pasar de string a datetime
jan1 = dt.datetime.strptime("01-01/2020","%d-%m/%Y")
print(jan1)
print(type(jan1))

# Puedo medir la diferencia entre 2 fechas
resultado = now-jan1
print(resultado)
print(type(resultado))

print(resultado.days)  # me devuelve la cantidad de dias
print(resultado.seconds)  # me devuelve la cantidad de segundos
print(type(resultado.days))


# Puedo sumarle dias a una fecha
fivedays = dt.timedelta(days=5, hours=12)
print(now+fivedays)


'''
logging — Logging facility for Python

Me permite generar distintos niveles de mensajes
Me permite ademas de imprimir en pantalla, guardar en un archivo, enviar por mail, etc

Hay 4 niveles:
- debug
- info
- warning
- error
'''

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='{asctime} {levelname} ({threadName:10s}) {message}',
    style='{'
)


logging.debug("debug message paso algo ")
logging.info("logueo algo")
logging.warning("paso algo ")
logging.error("se rompio el programa")

