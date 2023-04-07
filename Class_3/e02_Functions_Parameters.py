from Class_3.e01_Functions_Definition import *

char = "-"

#I can call a function that uses another function
printShortLine(char)
printLongLine(char)
printLine()
printLine(numberOfTimes=50)
printLine(character="~",numberOfTimes=100)

#required positional parameter error
#printShortLine()

'''Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Arbitrary Arguments are often shortened to *args in Python documentations.

Example
If the number of arguments is unknown, add a * before the parameter name:'''
print("matias",1,"Julian",50)

def my_print(*parameters):
    for value in parameters:
        print(str(value)+" ")

my_print("matias",1,50)

def my_function(*kids):
    for kid in kids:
        print("The youngest child is " + kid)

my_function("Emil", "Tobias", "Linus","Matias")


'''Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

Example
If the number of keyword arguments is unknown, add a double ** before the parameter name:'''

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes",matias="OK")