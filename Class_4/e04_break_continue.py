"""
Break
Termina el ciclo actual

Continue
Saltea la iteracion actual y continua con la siguiente iteracion
"""


#usando break y continue en fors anidados
for i in range(4):  # que valores puede tomar i ?
    if i == 2:
        continue  # saltea la iteracion actual y continua con la siguiente iteracion
    for j in range(4):
        if j == 2:
            break  # rompe el for mas interno
        print("The number is ",i,j)

print('- - - - - - - - - -')

# Codigo para encontrar numeros primos
# Un numero primo es un numero que solo es divisible por si mismo y por 1
# Tarea para ver cada uno.
for n in range(2, 10):  # que valores puede tomar n ?
    for x in range(2, n):  # que valores puede tomar x ?
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:  # si el for no se ejecuta nunca, ejecuta el else. Es similar a un if
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print('- - - - - - - - - -')

'''sumar impares de la primer cadena con pares de la segunda'''
cadena1 = "1234"
cadena2 = "5678"

even = lambda y: y % 2 == 0

result = 0
for l1 in cadena1:
    l1 = int(l1)
    if even(l1):
        continue
    for l2 in cadena2:
        l2 = int(l2)

        if not even(l2) and l2 != 5:
            break
        result += l1+l2

    break  # este break rompe el for principal y continua con la ejecucion del programa

print(result)


# Ejemplo de continue
# Para ver como tarea
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)