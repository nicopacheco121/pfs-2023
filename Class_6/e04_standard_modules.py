'''Python comes with a vast library of functions ready to use by developers'''

'''Documentacion
https://docs.python.org/3/library/index.html

Ejemplos en código
https://github.com/dhellmann/pymotw-3

'''

import math
from math import pi as pie
from math import ceil

ceil(11.5)
print(pie)
print(math.pi)
print(math.e)
'''
The math module includes three functions for converting floating point values to whole numbers. Each takes a different 
approach, and will be useful in different circumstances.

The simplest is trunc(), which truncates the digits following the decimal, leaving only the significant digits making 
up the whole number portion of the value. floor() converts its input to the largest preceding integer, 
and ceil() (ceiling) produces the largest integer following sequentially after the input value.'''
print(math.trunc(math.pi))
print(math.floor(math.pi))
print(math.ceil(math.pi))
print(math.trunc(-10.50))
print(math.floor(-10.50))
print(math.ceil(-10.50))

'''Alternate Representations of Floating Point Values
modf() takes a single floating point number and returns a tuple containing the fractional and whole number parts of the input value.'''

print(math.modf(2.5))
print(math.modf(8.5))
print(math.modf(-10.3))
print(math.modf(1.98772))
print(math.modf(-3.00033))
print(math.modf(0.333))

'''Decimal
Decimal values are represented as instances of the Decimal class. The constructor takes as argument one integer or string. 
Floating point numbers can be converted to a string before being used to create a Decimal, letting the caller explicitly 
deal with the number of digits for values that cannot be expressed exactly using hardware floating point representations. 
Alternately, the class method from_float() converts to the exact decimal representation.
'''
print(1.1+2.2)
nuevo_valor = round(1.1+2.2,2)
print(nuevo_valor)
if nuevo_valor > 3.3:
    print("Es mayor")
else:
    print("No es mayor")

import decimal
from decimal import Decimal
from decimal import Decimal as MiObjeto
decimal.getcontext().prec = 20
print(decimal.Decimal(1.1+2.2))
print(decimal.Decimal(1.1)+decimal.Decimal(2.2))
print(decimal.Decimal('1.1')+decimal.Decimal('2.2'))
print(Decimal('1.1')+Decimal('2.2'))
print(Decimal.from_float(1.1)+Decimal.from_float(2.2))
MiObjeto()


'''
random

The random module provides a fast pseudorandom number generator based on the Mersenne Twister algorithm. 
Originally developed to produce inputs for Monte Carlo simulations, Mersenne Twister generates numbers with nearly 
uniform distribution and a large period, making it suited for a wide range of applications.'''

import random

'''Seeding
random() produces different values each time it is called and has a very large period before it repeats any numbers. 
This is useful for producing unique values or variations, but there are times when having the same data set available 
to be processed in different ways is useful. One technique is to use a program to generate random values and save 
them to be processed by a separate step. That may not be practical for large amounts of data, though, so random 
includes the seed() function for initializing the pseudorandom generator so that it produces an expected set of values.'''

random.seed(100)
print(random.randrange(0,100))
print(random.randrange(0,100))
print(random.randrange(0,100))
#print(random.randint(0,100))

''''''

'''Sampling
Many simulations need random samples from a population of input values. The sample() function generates samples
 without repeating values and without modifying the input sequence. This example prints a random sample of words 
 from the system dictionary.

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

import os

import os.path

for user in [ '', 'root', 'postgres' ]:
    lookup = '~' + user
    print(lookup, ':', os.path.expanduser(lookup))

for path in [ '.', '..', './one/two/three', '../one/two/three']:
    print(path, os.path.abspath(path))

print(os.path.abspath(os.path.curdir))
#os.chdir("/")
#print(os.path.abspath(os.path.curdir))
print(os.path.abspath(os.path.pardir))
print(os.path.abspath(os.path.curdir))
print(os.path.abspath("~")+"Documents/REM364.json")


'''
time — Time access and conversions

    """
    strftime(format[, tuple]) -> string
    
    Convert a time tuple to a string according to a format specification.
    See the library reference manual for formatting codes. When the time tuple
    is not present, current time as returned by localtime() is used.
    
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
    """'''

from time import *
print(strftime("%d %B %Y %H:%M:%S %p", gmtime()))

day = strptime("30/11/2000", "%d/%m/%Y")
print(day)

print(time())

'''
datetime — Basic date and time types
'''
import datetime as dt

''' la libreria esta compuesta por varios tipos de datos. Los mas importantes son

datetime.datetime: una fecha y una hora
dateime.date: que es solamente una fecha
datime.time: que es una hora
datetime.timedelta: que es el intervalo entre 2 fechas/momentos en el tiempo'''

now = dt.datetime.now()
print(now)
jan1 = dt.datetime.strptime("01/01/2020","%d/%m/%Y")
print(jan1)
resultado = now-jan1
print(resultado.days)
fivedays = dt.timedelta(days=5,hours=12)
print(now+fivedays)

'''
logging — Logging facility for Python
'''
#jaksjflkajsf
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='{asctime} {levelname} ({threadName:10s}) {message}',
    style='{'
)

logging.debug("debug message paso algo ")
logging.info("logueo algo")
logging.warning("paso algo ")
logging.error("se rompio el programa")

