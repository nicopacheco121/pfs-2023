"""
- Sintaxis
- Parametros
- Por que esta en gris la variable1? Por que esta en gris nombre en la funcion sayHello2?
- Que pasa si no le paso un parametro a la funcion?
- variable1 esta en el main y dentro de la funcion, son la misma variable?
- Debuggear el codigo y notamos que al ver la funcion solo sabe que existe pero no hace nada
- Debug diferencia entre F8 y F7
- Debug con F7 entramos a la función y vemos las distintas variables que existen dentro de la función
- Python me permite utilizar variables del mundo exterior dentro de la funcion (mala practica). Si no encuentra la variable
dentro de la funcion, la busca en el mundo exterior. Si no la encuentra en el mundo exterior, tira error.
"""

name = "Patricio"


# Definimos una funcion, vemos la SINTAXIS
def myFirstFunction(unParametro):
    # Los parametros de las funciones son equivalentes a variables
    # Las variables declaradas dentro de una función solo existen dentro de la funcion
    variable1 = 6  # Esta variable esta en gris porque no la estoy utilizando
    print("Hello " + str(unParametro))


# Ejecutamos la funcion
variable1 = 10
myFirstFunction(variable1)  # Ver que pasa si no le paso un parametro a la funcion


def sayHello2(nombre):
    # Las variables tienen precedencia según donde estan declaradas
    # Una variable declarada dentro de la funcion con el mismo nombre de un parametro, pisa su valor
    print("Hello", name)


# Vemos que hace la funcion sayHello2
sayHello2(name)
sayHello2("Juan")  # que imprime la funcion?


"""
- Parametros opcionales

- Return para devolver un valor al mundo exterior
- Cuando ejecuta el return termina la ejecucion de la funcion
- Diferencia entre print y return, el print muestra por pantalla y el return devuelve un valor
- Guardamos el valor de retorno de la funcion en la variable valor

- Orden de los parametros

- Guardamos el valor de retorno de la funcion en la variable valor
"""


def multiplicarAbsoluto(numero1, numero2=2, numero3=6):
    result = numero1 * numero2 * numero3
    if result > 0:
        return result
    else:
        return -result


valor = 8
print(multiplicarAbsoluto(valor))

# Que devuelve si imprimo el valor de retorno de sayHello2?
print(sayHello2("Juan"))

print(multiplicarAbsoluto(valor, 7, 9))  # orden de parametros
print(multiplicarAbsoluto(numero2=4, numero3=7))  # que pasa si intento ejecutar esta funcion?
print(multiplicarAbsoluto(1, numero3=7))  # puedo pasar el valor indicando el nombre del parametro
print(valor)  # que valor tiene la variable valor?

# Guardamos el valor de retorno de la funcion en la variable valor
valor = multiplicarAbsoluto(valor, 4)
print(valor)
