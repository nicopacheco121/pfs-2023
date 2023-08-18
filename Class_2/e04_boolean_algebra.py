'''
Evaluaciones que podemos hacer entre distintos operandos:
Operator	Name	                    Example	Try it
==	        Equal	                    x == y
!=	        Not equal	                x != y
>	        Greater than	            x > y
<	        Less than	                x < y
>=	        Greater than or equal to	x >= y
<=	        Less than or equal to	    x <= y

Operadores del algebra de bool y combinacion
Operator	Description	                                                Example	Try it
and 	Returns True if both statements are true	                    x < 5 and  x < 10
or	    Returns True if one of the statements is true	                x < 5 or x < 4
not	    Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)

Comparar si dos tipos de datos son iguales
Operator	Description	                                            Example	Try it
is 	        Returns True if both variables are the same object	    x is y
is not	    Returns True if both variables are not the same object	    x is not y

Comprobar si el valor de la variable esta contenido en el conjunto de valores almacenado en la otra variable
Operator	Description	                                                                            Example	Try it
in 	        Returns True if a sequence with the specified value is present in the object	        x in y
not in	    Returns True if a sequence with the specified value is not present in the object	    x not in y
'''

# Dadas dos variables con valores booleanos, veremos el algebra de bool
a = True
b = False

print(a)
print(b)
print(a and b)
print(a or b)
print(not a)
print(not b)
print(not (a and b))

# Puedo utilizar el algebra de book a la hora de asignar el valor a una variable
z = a and b
print(z)

# in
print("a" in ("True", "a", "True"))
print("b" not in ("True", "a", "True"))

# is
c = None
print(c is None)

# Evaluaciones entre distintos operandos
print(1 > 2)
print(1 >= 2)
print(1 == 2)
print(1 != 2)
print("10" > "2")
# orden natural

print(True > True)


# is
print(type(1) is int)
print(type(1) is float)
print(type(1.0) is float)
print(type(1) is bool)