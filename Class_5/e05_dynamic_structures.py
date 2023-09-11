"""
Estuvimos creando listas, tuplas y diccionarios de forma manual, pero Python
tiene una forma más rápida de hacerlo, usando listas por comprensión.

Las listas por comprensión proporcionan una forma concisa de crear listas.

Las aplicaciones comunes, por ejemplo, podría ser generar nuevas listas donde cada elemento es el
resultado de algunas operaciones aplicadas a cada miembro de otra lista.
"""

### CREAMOS LISTAS
lista = [2, 4, 6]

# Creamos una nueva lista con los valores de la lista original multiplicados por 3

# Pongo los corchetes para que decirle a Python que quiero una lista
# Con el for le digo que quiero que recorra la lista y que guarde el valor en x
# Con el 3*x le digo que quiero que guarde el valor de 3*x en la nueva lista
lista2 = [3 * x for x in lista]
print(lista2)


# Añadimos un filtro
# Creamos una nueva lista con los valores de la lista original multiplicados por 3 pero solo si el valor es menor a 2
# Ahora con el if le digo que solo guarde el valor si x es menor a 2
lista3 = [3 * x for x in lista if x > 3]  # cuantos elementos tiene la lista?
# *** CUANDO la condicion ESTA A LA DERECHA EL FOR, solo los valores que cumplan con la condicion se guardan en la lista

print(lista3)

print([3*x for x in lista if x < 2 or x > 100])  # cuantos valores tiene la lista?

# Cuando el IF esta a la izquierda del for, NO FILTRA, sino que reemplaza los valores que no cumplen la condicion por lo que esta en el else
print([3*x if x < 4 else None for x in lista])


### CREAMOS DICCIONARIOS
lista = [2, 4, 6]
# pongo llave para que python sepa que quiero un diccionario
dict_1 = {str(x): x for x in lista}  # pongo clave y valor
print(dict_1)

print({str(3*x): x**3 for x in lista if x > 3 or x > 100})
print([3*x if x < 2 else None for x in lista])


### CREAMOS ESTRUCTURAS COMPUESTAS

# Listas por comprensión anidadas. Creamos lista de listas
print([[x, x**2] for x in lista])  # cuantos elementos tiene la lista principal? y cuantos elementos tiene cada lista interna?


### PUEDO TENER FOR ANIDADOS
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print([x*y for x in vec1 for y in vec2])
# Primero x toma el valor de 2, y hace las combinaciones con todos los valores de vec2
# Luego x toma el valor de 4, y hace las combinaciones con todos los valores de vec2

print([vec1[i] * vec2[i] for i in range(len(vec1))])  # hago la multiplicacion de los valores de la misma posicion de cada lista


### PUEDO LLAMAR A FUNCIONES
# Pueden aplicarse a expresiones complejas y funciones anidadas
print([str(round(355/113.0, i)) for i in range(1, 6)])

### PUEDO TRABAJAR CON MATRICES
# Listas por comprensión anidadas
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# Para intercambiar filas y columnas
print([[fila[i] for fila in mat] for i in range(len(mat))])

# puedo hacer lo mismo pero sin listas por comprension
matriz_nueva = []
for i in range(len(mat)):
    fila_nueva = []
    #por cada elemento de
    for fila in mat:
        fila_nueva.append(fila[i])
    matriz_nueva.append(fila_nueva)
print(matriz_nueva)


# UTILIZO FUNCIONES LAMBDA
print(list(filter(lambda x: x < 10, [i+j for i in range(0, 10) for j in range(1, 10)])))


# CREO UN DICCIONARIO
a = dict([(x, x ** 2) for x in (2, 4, 6)])  # use a list por comprensión
print(a)
print(a[2])  # que valor imprime?
