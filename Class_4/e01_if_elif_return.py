"""
Vamos a ver distintas formas de llegar a la misma solucion

En este caso vamos a ver como determinar si un numero es par o impar

Utilizaremos el operador modulo (%)
"""


def oddOrEven(number):
    output = None  # Pre asigno el resultado para que no de error. Como todavia no se si es par o impar, le asigno None

    mod = number % 2  # Si el modulo es 0, es par, si es 1 es impar

    if mod == 0:
        output = "even"
    elif mod == 1:
        output = "odd"
    elif mod == None:  # Esto no se deberia ejecutar nunca
        output = ""
    return output


# Menos instrucciones utilizando return para cortar la ejecucion de la funcion y devolver el resultado
def oddOrEven2(number):
    mod = number % 2
    if mod == 0:
        return "even"
    else:
        return "odd"
    print("estoy por la linea 30")  # Esto linea nunca se va a ejecutar

    return False


# Asumimos un valor de retorno por defecto
def oddOrEven3(number):
    output = "odd"  # Asumimos que el numero es impar

    mod = number % 2
    if mod == 0:
        output = "even"  # Si el numero es par, sobreescribimos el valor de retorno
    return output


"""
Vemos otros 2 ejemplos de funcion que nos encuentre el maximo entre 3 numeros

"""


def maximo(a, b, c):
    if a > b:
        if a > c:
            return a
        return c  # Si a no es mayor que c, entonces c es el mayor
    elif b > c:
        return b  # Si b es mayor que c, entonces b es el mayor
    return c  # Si no se cumple ninguna de las condiciones anteriores, entonces c es el mayor


# Otra forma de resolverlo pre asignando el resultado
def maximo2(a, b, c):
    resultado = c  # Asumimos que c es el mayor
    if a > b:
        if a > c:
            resultado = a  # Reemplazamos el resultado por a
    elif b > c:
        resultado = b  # Reemplazamos el resultado por b

    # En este caso me sirve ya que si quisiera hacer algo con el resultado, lo podria hacer aca
    resultado += 2  # Esto no podria hacerlo si no hubiera pre asignado el resultado

    return resultado


print(maximo(4, 10, 8))
print(maximo2(18, 2, 12))

print('- - - - - - - - - -')

"""
Resultado del ejercicio de la clase 3
def outOfBand(security, order):
    outOfBand = False
    priceLimitType = security.priceLimitType
    price = security.marketdata["LA"]["price"] if "LA" in security.marketdata and security.marketdata[
        "LA"] and "price" in security.marketdata["LA"] and security.marketdata["LA"]["price"] else security.marketdata[
        "CL"] if "CL" in security.marketdata and security.marketdata["CL"] else 0

    if (priceLimitType == "PRICE" and (
            order.price <= security.lowLimitPrice or order.price >= security.highLimitPrice)):
        outOfBand = True
    elif (price and priceLimitType == "PERCENTAGE" and (
            (order.side == "SELL" and order.price <= price * (1 - security.lowLimitPrice / 100)) or (
            order.side == "BUY" and order.price >= price * (1 + security.highLimitPrice / 100)))):
        outOfBand = True
    elif (price and priceLimitType == "HARD" and (order.price <= price * (1 - security.lowLimitPrice / 100) or (
            order.price >= price * (1 + security.highLimitPrice / 100)))):
        outOfBand = True
    return outOfBand"""

'''
If en una sola linea
If you have only one statement to execute, you can put it on the same line as the if statement.
'''
a = 15
b = 10
if a > b: print("a is greater than b")  # ejecuto el if en una sola linea

print('- - - - - - - - - -')

'''
If en una sola linea con else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
'''

a = 2
b = 330
print("A") if a > b else print("B")  # primero se evalua la condicion, si es True se ejecuta el print("A"), si es False se ejecuta el print("B")

# Vemos como se puede utilizar el if en una sola linea para asignar un valor a una variable.
# Tenemos 2 ambientes, produccion y pruebas

ambiente = "produccion"
ambiente = 'cualquier cosa'
# url = "http://www.rofexproduccion" if ambiente=="produccion" else None
url = "url de produccion" if ambiente == "produccion" else "url de pruebas"

if ambiente == "produccion":
    url = "url de produccion"
else:
    url = "url de pruebas"

print('- - - - - - - - - -')

'''
Quiero evaluar varios if en una sola linea

'''

a = 2
b = 3
print("A") if a > b else (print("=") if a == b else print("B"))
# primero se evalua la condicion, si es True se ejecuta el print("A"),
# si es False se evalua la siguiente condicion, si es True se ejecuta el print("="), si es False se ejecuta el print("B")
