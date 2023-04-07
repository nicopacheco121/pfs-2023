'''
Creating Variables
Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

Example'''

x = 5
y = "John"
print(x)
print(y)

'''Variables do not need to be declared with any particular type and can even change type after they have been set.

Example'''
x = 4 # x is of type int
x = "Sally" # x is now of type str
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
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
#2myvar = "John"
#my-var = "John"
#my var = "John"

'''Remember that variable names are case-sensitive

Assign Value to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''And you can assign the same value to multiple variables in one line:

Example'''
x = y = z = "Orange"
print(x)
print(y)
print(z)

'''Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

Example'''
x = "awesome"
print("Python is " + x)

#to define a variable we have to give it a name

myVariable = None

print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))
print("-----")

print("", bool(""))
print(0, bool(0))


myVariable = 2
print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))
print("-----")

myVariable = str(myVariable)
print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))
print("-----")

myVariable = bool(myVariable)
print("Valor",myVariable)
print("Type",type(myVariable))
print("Boolean",bool(myVariable))

#Assignment expression

print(x := 5)
print(x)
print(x:="Hola")
print(x)