"""
While

No se sabe cuantas veces se va a ejecutar el codigo
Se ejecuta mientras la condicion sea verdadera
La condicion se evalua al principio de cada iteracion
Si la condicion es False, no se ejecuta el codigo dentro del while y continua la ejecucion del programa


"""

# Sintaxtis
entero = 1
while entero <= 10:  # condicion
    # Este bloque de codigo se ejecuta mientras la condicion sea verdadera
    # cuantas veces se ejecuta este bloque de codigo ?
    print(f"Iterando por {entero} vez")
    if entero % 4 == 0:
        entero -= 5
    entero += 5
# debugeamos

print('- - - - - - - - - -')

"""
vamos a hacer un juego
el usuario tiene 5 intentos para adivinar un numero entre 0 y 10
si el usuario adivina el numero, gana
si el usuario no adivina el numero, vuelve a intentar hasta que se le acaben los intentos
"""

import random  # este modulo nos permite generar numeros aleatorios

numero = random.randint(0,
                        10)  # generamos un numero aleatorio entre 0 y 10. Este numero es el que el usuario tiene que adivinar

intento = 0  # contador de intentos

# En el while tenemos 2 condiciones.
# La primema es que el usuario tenga intentos disponibles
# La segunda, comparamos el numero ingresado por el usuario con el numero que tiene que adivinar

while intento < 5 and (prueba := int(input("ingrese numero"))) != numero:
    intento += 1
    if prueba > numero:  # Le doy una ayuda al usuario
        print("El numero ingresado es mayor al buscado")
    else:
        print("El numero ingresado es menor al buscado")

if numero == prueba:
    print("Ganaste el numero es:", numero, "usaste ", intento, "intentos")
else:
    print("Perdiste")

print('- - - - - - - - - -')

'''Serie fibonacci'''


def fib(n):  # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b
fib(50)

print('- - - - - - - - - -')


"""
Vemos la cantidad de multiplos de a hasta b, ahora con un while
Lo que hicimos con for tambien lo podemos hacer con while
En este caso vemos una forma de hacerlo mas eficiente

"""
def cantidadMultiplos(a, b):
    cantidad = 1
    multiplo = a + a  # yo se que si el numero es multiplo de a, entonces el siguiente multiplo es a+a
    while multiplo <= b:  # mientas el multiplo sea menor o igual al limite
        cantidad += 1
        multiplo += a  # incremento el multiplo
    return cantidad

print(cantidadMultiplos(4, 100))  # cuantas veces se ejecuta este codigo ?

print('- - - - - - - - - -')


"""
While anidados
Queda como tarea para que lo vean
"""
# Quiero mostrar la cantidad de multiplos de n numeros
# Mientras los numeros tengan mas de 1 multiplo hasta 100
multiplo = 2
numero = 1
while multiplo > 1:
    multiplo = cantidadMultiplos(numero, 100)
    print("Multiplos de " + str(numero) + ": " + str(multiplo))
    numero += 1
