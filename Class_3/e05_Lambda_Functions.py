'''
La funcion lambda es una forma simple de definir una funcion de 1 linea
Tiene una unica instruccion
Se puede asignar a una variable

- Sintaxis
- Lambda con un parametro
- Lambda con varios parametros


'''


def func(y):
    return y * 2


# esta funcion lambda es equivalente a la funcion func
x = lambda y: y * 2  # y es el parametro de la funcion, y*2 es el valor de retorno de la funcion

print(x(10))  # que imprime esta linea?

# asigno a x el retorno de x
z = x(2)

# asigno func a y
y = func  # diferencia entre usar con parametros y sin parametros
print(y(10))  # que imprime esta linea?

print('- - - - - - - - - - - - - - -')

# Lambda con varios parametros
sumarize = lambda x, y, z: x + y + z

print(sumarize(4, 1, 6))

print('- - - - - - - - - - - - - - -')


"""
En algunas situaciones es util utilizar funciones lambda en conjunto con otras funciones como por ejemplo filter.
Filter es una funcion que recibe como parametros:
 . una funcion (cuyo retorno debe ser verdadero o falso) y 
 . un conjunto de datos 
y devuelve los elementos que cumplen con la condicion de la funcion.

Es util cuando por ejemplo no me interesa guardar la funcion ya que solo la utilizaremos como el parametro de otra funcion
y luego no la utilizaremos mas. De esta manera no necesito definir una funcion con def y luego pasarla como parametro,
sino que puedo definir la funcion lambda directamente como parametro de la funcion.
Con esto logramos que el codigo sea mas legible y mas corto.

"""
datos = range(0, 100)  # gener un conjunto de datos del 0 al 99
datos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'aaa', 'aj']

resultado = list(filter(lambda x: x.startswith('a'), datos))  # que hace la funcion lambda?
# con "list" convierto el resultado en una lista
print(resultado)  # que obtengo como resultado?

print('- - - - - - - - - - - - - - -')

# Otro ejemplo con otra funcion
def condicion(valor=50):
    return valor > 10.0 and valor < 20.0  # devuelve verdadero solo si el valor es mayor a 10 y menor a 20


variable = condicion
variable()
resultado2 = list(filter(condicion, range(0, 100)))
print(resultado2)  # que obtengo como resultado?


# La misma funcion pero con lambda
resultado3 = list(filter(lambda x: x > 10.0 and x < 20.0, range(0, 100)))
print(resultado3)  # que obtengo como resultado?

print('- - - - - - - - - - - - - - -')

"""
Funcion map
La funcion map recibe como parametros:
    . una funcion y
    . un conjunto de datos
y devuelve un conjunto de datos con el resultado de aplicar la funcion a cada elemento del conjunto de datos.
"""

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))  # cual es el nuevo valor de cada elemento de la lista?

print(new_list)

print('- - - - - - - - - - - - - - -')

"""
Funciones como variables
A veces quiero ejecutar de manera dinamica una cantidad de funciones, es decir, no se cuantas funciones voy a ejecutar.
Para esto puedo crear una lista de funciones y luego recorrerla para ejecutar cada funcion.
"""


lista = [condicion, str, x, int]  # creo una lista con 4 funciones. x es la funcion lambda que definimos antes

for item in lista:  # con el for recorro la lista y obtengo cada elemento, en este caso elemento es una funcion
    print(item(12))

# Es igual a hacer esto:
print(condicion(12))
print(str(12))
print(x(12))
print(int(12))

# Es mas potente hacerlo con el for ya que puedo agregar o quitar funciones de la lista y el codigo sigue funcionando
