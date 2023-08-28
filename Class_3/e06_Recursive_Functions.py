"""
Funciones Recursivas
Las funciones recursivas son funciones que se llaman a si mismas

Por ejemplo, la funcion factorial de un numero es el producto de todos los numeros enteros positivos desde 1 hasta ese numero.
O se podria decir que el factorial de n es igual al n multiplicado por el factorial de n-1.
Por ejemplo, el factorial de 5 es 1*2*3*4*5 = 120

La funcion factorial se puede definir de la siguiente manera:
    factorial(1) = 1
    factorial(n) = n * factorial(n-1)

Ejemplo:
    factorial(5) = 5 * factorial(4)
    factorial(4) = 4 * factorial(3)
    factorial(3) = 3 * factorial(2)
    factorial(2) = 2 * factorial(1)
    factorial(1) = 1

"""

# Vemos con el debug como se ejecuta la funcion factorial
def factorial(numero):
    if numero == 1:
        return 1
    return numero*factorial(numero-1)


print(factorial(5))