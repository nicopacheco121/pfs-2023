
'''String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning'''

'''String Methods
Python has a set of built-in methods that you can use on strings.
'''

"""
strip()
Remueve los espacios en blanco al principio y al final de un string
"""
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"


'''
lower()
Retorna un string en minusculas
'''

a = "Hello, World!"
print(a.lower())

'''
upper()
Retorna un string en mayusculas
'''

a = "Hello, World!"
print(a.upper())
print(a)  # no modifica el string original

'''
replace()
Reemplaza un string por otro
'''

a = "Hello, World!"
# toma 2 parametros, el primero es el string a reemplazar, el segundo es el string que reemplaza
print(a.replace("Hello", "Hola"))


'''
split()
Divide el string en sub-strings en base a un separador

Me devuelve una lista con los sub-strings
El patron NO se incluye en el resultado

Es util para cando hacemos web scraping, es decir, cuando queremos extraer informacion de una pagina web.
'''

a = "Hello, World!"
print(a.split(", "))  # returns ['Hello', ' World!']
print(a.split(","))  # que pasa si no hay espacio despues de la coma?

original_string = "ab_cd_ef"
split_string = original_string.split("_")
print(split_string)

# Ejemplo, queremos quedarnos solo con la palabra valor
print("dato: unmonton de cosas:$valor".split(":")[2].split('$')[1])


"""
endswith()
Retorna True si el string termina con el valor especificado
"""
ticker = 'BTCBUSD'
print(ticker.endswith('USDT'))

"""
startswith()
Retorna True si el string comienza con el valor especificado"""
ticker = 'MERV - XMEV - AL30 - CI'
print(ticker.startswith('MERV'))

"""
join()
Concatena los elementos de un iterable (lista, tupla, etc) en un string, utilizando un string como separador

La inversa al split
"""
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

print(",".join([str(x) for x in range(1, 100)]))


'''Escape Character
Para insertar caracteres especiales, usamos un escape character.

Es un backslash \ seguido del caracter que queremos insertar.

Por ejemplo, si queremos insertar una comilla doble dentro de un string que esta rodeado por comillas dobles, 
usamos el escape character \", de lo contrario, python no sabria donde termina el string.
'''

# txt = "We are the so-called "Vikings" from the north."
'''To fix this problem, use the escape character \":'''

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = 'We are the so-called "Vikings" from the north.'  # tambien podria usar comillas simples
print(txt)

'''Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote
\\	Backslash: la primer barra es el escape character, la segunda es el caracter que quiero insertar
\n	New Line: En python el caracter \n es un salto de linea
\r	Carriage Return: En otros sistemas operativos se utiliza \r\n para salto de linea
\t	Tab
\b	Backspace
'''




