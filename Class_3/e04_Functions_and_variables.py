"""
Scope de variables

- Puedo declarar una variable fuera de una funcion y utilizarla dentro de la funcion
"""

x = "global"

def foo():
    print("x inside:", x)


foo()  # que imprime la funcion?
print("x outside:", x)  # que imprime esta linea?

x = "global"


"""
Declaro una variable dentro de una funcion intentando utilizarla antes de asignarle un valor
"""
def faa():
    x = x * 2  # no puedo utilizar una variable declarada dentro de una funcion antes de asignarle un valor
    # z = x * 2
    print(x)

# faa()


"""
No puedo utilizar una variable declarada dentro de una funcion fuera de la funcion
"""


def fee():
    y = "local"

fee()
# print(y)


def fii():
    y = "local"
    print(y)  # ahora si puedo utilizar la variable y

fii()


"""
Puedo utilizar una variable global dentro de una funcion si la declaro como global
No es una buena practica utilizar variables globales

"""

x = "global"


def fuu():
    global x  # declaro la variable x como global
    y = "local"
    x = x * 2  # puedo utilizar la variable x declarada como global
    print('Vemos el valor de x que ahora es global dentro de la funcion:', x)
    print(y)


fuu()
print('Vemos el valor de x fuera de la funcion:', x)


# Modificamos el valor de x pero sin colocar la palabra reservada global
x = 5

def fo():
    x = 10
    print("local x:", x)


fo()
print("global x:", x)