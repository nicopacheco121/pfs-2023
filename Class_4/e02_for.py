
"""
Vamos a ver al sintaxis del for

Recorremos una cadena de texto

"""
unaCadena = "esta es una cadena de texto"

# Vemos la sintaxis del for
for variable1 in unaCadena:  # variable1 es una variable que va a ir tomando el valor de cada elemento de la cadena
    print(variable1)  # que valor va tomando variable1 ?
# cuando termina el for, continua la ejecucion del programa
# el nombre variable1 es arbitrario, puede ser cualquier nombre valido de variable

print('- - - - - - - - - -')

"""
Recorremos una cadena y hacemos un if con cada elemento

"""


def isVocal(letter):
    vocales = "aeiou"
    return letter in vocales


for letter in unaCadena:
    if not isVocal(letter):  # si la letra no es vocal, la imprimimos
        print(letter)

print(isVocal("aei"))  # que valor devuelve esta funcion ?

print('- - - - - - - - - -')

'''The range() Function

El range() es una funcion que devuelve una secuencia de numeros
Tiene 3 parametros, start, stop, step
Si no se especifica start, por default es 0
Si no se especifica step, por default es 1
El parametro stop es OBLOGATORIO
El stop es el numero hasta el cual se va a generar la secuencia sin incluirlo.

'''
print(*range(10))
print('- - - - - - - - - -')
print(*range(1, 10))  # start, stop
print('- - - - - - - - - -')
print(*range(1, 10, 2))  # start, stop, step
print('- - - - - - - - - -')
print(*range(1, -10, -2))  # Tambien se puede usar numeros negativos

print('- - - - - - - - - -')

# La puedo utilizar en un for para recorrer una secuencia de numeros
for x in range(10):
    print(x)

print('- - - - - - - - - -')

'''
For anidados
mostrar la combinatoria de las letras de dos cadenas de caracteres
'''

cadena1 = "1234"
cadena2 = "5678"


for l1 in cadena1:  # Recorro la primer cadena
    for l2 in cadena2:  # Recorro la segunda cadena
        print(l1+l2)
# Debugeamos el codigo para ver que esta pasando

print('- - - - - - - - - -')

"""
Hacemos un for dentro de una funcion
"""
isMultiplo = lambda y, z: y % z == 0  # funcion lambda que devuelve True si la variable y es multiplo de z


def cantidadMultiplos(a,b):  # funcion que devuelve la cantidad de multiplos de a hasta el numero b
    cantidad = 0  # almaceno la cantidad de multiplos
    for x in range(1, b+1):  # que me devuelve el range ?
        if isMultiplo(x, a):  # por cada valor de x, pregunto si es multiplo de a
            cantidad += 1  # si es multiplo, incremento la cantidad
    return cantidad
# Debugeamos el codigo para ver que esta pasando

print(cantidadMultiplos(4,100))