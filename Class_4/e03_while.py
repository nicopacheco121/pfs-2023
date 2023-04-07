entero = 1

while entero <= 10:
    print(f"Iterando por {entero} vez")
    if entero % 4 == 0:
        entero -=5
    entero += 5

import random
numero = random.randint(0,10)
intento = 0
while intento <= 5 and (prueba := int(input("ingrese numero")))!=numero:
    intento+=1
    if prueba > numero:
        print("El numero ingresado es mayor al buscado")
    else:
        print("El numero ingresado es menor al buscado")
if numero == prueba:
    print("Ganaste el numero es:",numero,"usaste ",intento, "intentos")
else:
    print("Perdiste")

'''Serie fibonacci'''

def fib(n):    # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a+b


fib(50)


def cantidadMultiplos(a,b):
    cantidad = 1
    multiplo = a+a
    while multiplo <= b:
       cantidad += 1
       multiplo += a
    return cantidad

print(cantidadMultiplos(4,100))


#Quiero mostrar la cantidad de multiplos de n numeros
#Mientras los numeros tengan mas de 1 multiplo hasta 100
multiplo = 2
numero = 1
while multiplo > 1:
    multiplo = cantidadMultiplos(numero, 100)
    print("Multiplos de " + str(numero) + ": " + str(multiplo))
    numero+=1
