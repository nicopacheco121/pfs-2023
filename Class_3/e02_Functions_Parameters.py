"""
- Importar funciones de otro archivo, sintaxis
"""

# Importamos funciones
from Class_3.e01_Functions_Definition import *
# from Class_3.e01_Functions_Definition import printLine
# from Class_3.e01_Functions_Definition import printLine as pl

char = "-"

printLine()  # ejecuto la funcion printLine sin pasarle parametros
printLine(numberOfTimes=50)  # puedo modificar uno de los parametros
printLine(character="~", numberOfTimes=100)


# Puedo llamar a una funcion que utiliza otra funcion
printShortLine(char)  # Si quiero una linea corta uso esta funcion
printLongLine(char)  # Si quiero una linea larga uso esta funcion


'''
Parametros arbitrarios, *args
Si no sabes cuantos argumentos se pasarán a tu función, agrega un * antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
Los Argumentos Arbitrarios a menudo se acortan a *args en la documentación de Python.

- Declaramos una funcion con un parametro arbitrario
- *args es una tupla, es decir, un conjunto de valores
- Vemos los valores que tiene la tupla con el debug
'''
print("matias", 1, "Julian", 50, sep='.')  # que sucede si le paso varios parametros a la funcion print?


def my_print(*parameters):  # *parameters es una tupla, es decir, un conjunto de valores
    for value in parameters:  # recorro la tupla, el for lo veremos mas adelante
        print(str(value)+" ")

my_print("matias",1,50)


# otro ejemplo
def my_function(*kids):
    for kid in kids:
        print("The youngest child is " + kid)

my_function("Emil", "Tobias", "Linus","Matias")


'''
Parametros arbitrarios, **kwargs
Si no sabes cuántos argumentos de palabra clave se pasarán a tu función, agrega dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia.
Es decir, **kwargs es un diccionario, es decir, un conjunto de valores con clave y valor
'''


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes", matias="OK")

# LA DIFERENCIA ENTRE * Y ** ES QUE * ES UNA TUPLA Y ** ES UN DICCIONARIO