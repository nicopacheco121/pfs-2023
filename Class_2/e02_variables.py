'''
Creating Variables
Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

Example'''

# Tiene 2 partes, el nombre de la variable y el valor que le asignamos
# Para asignar un valor a una variable usamos el signo =

x = 5
y = "John"
print(x)
print(y)

# El valor que le asignamos puede ser una instruccion, cuyo resultado es el valor que se le asigna a la variable
z = 5 + 5

'''Variables do not need to be declared with any particular type and can even change type after they have been set.
Example'''
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

'''String variables can be declared either by using single or double quotes:
Example'''
x = "John"
# is the same as
x = 'John'

'''Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
Example'''
# Case sensitive
myvar = "John"
myVar = "John"
MYVAR = "John"

# Pueden comenzar con _ o tener _ en el nombre
_my_var = "John"  # si comienza con _ es una variable privada o protegida
my_var = "John"

# Pueden tener numeros pero NO comenzar con un numero
myvar2 = "John"

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Estandares de nombres de variables
nombreDeUsuario = "John"
nombre_de_usuario = "John"


'''
Assign Value to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example'''
# Declaramos 3 variables y le asignamos un valor a cada una
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''And you can assign the same value to multiple variables in one line:

Example'''
# Le asignamos el mismo valor a las 3 variables
# a x le asignamos el valor de y, a y le asignamos el valor de z y a z le asignamos el valor de x
x = y = z = "Orange"
print(x)
print(y)
print(z)

'''Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

Example'''
# Concatenamos un string con una variable
x = "awesome"
print("Python is " + x)


# Variable sin asignacion de valor (None)

myVariable = None

print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))  # Evaluamos el valor de verdad de la variable con contenido None
print("-----")

print("", bool(""))  # Evaluamos el valor de verdad de la variable con contenido ""
print(0, bool(0))  # Evaluamos el valor de verdad de la variable con contenido 0


myVariable = 2
print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))  # cualquier cosa distinta de None, 0 o "" es True
print("-----")

myVariable = str(myVariable)
print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))  # un string con el valor "2" tambien es True
print("-----")

myVariable = bool(myVariable)  # Cual es el valor de verdad del string "2"?
print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))

#Assignment expression
# print(x := 5)  # con el := puedo crear la variable y a su utilizarlo como input a una funcion
# print(x)
# print(x:="Hola")
# print(x)