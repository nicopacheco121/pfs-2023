'''String Format

<template>.format(<positional_argument(s)>, <keyword_argument(s)>)

'''
'''Example
Use the format() method to insert numbers into strings:'''

age = 36
txt = "My name is John, and I am {}{}"
print(txt.format(age,True))


'''The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

Example'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print(myorder.format(quantity, price, itemno))


'''You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

Example'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1} {2} {0}."

print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
precio = 49.95
myorder = "I want to pay {price} dollars for {quantity} pieces of item {itemno}."

print(myorder.format(quantity=quantity, itemno=itemno, price=precio))

'''The <format_spec> Component
The <format_spec> component is the last portion of a replacement field:

{[<name>][!<conversion>][:<format_spec>]}

<format_spec> represents the guts of the Python .format() method’s functionality. It contains information that exerts fine control over how values are formatted prior to being inserted into the template string. The general form is this:

:[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]

The ten subcomponents of <format_spec> are specified in the order shown. They control formatting as described in the table below:

Subcomponent	Effect
:	Separates the <format_spec> from the rest of the replacement field
<fill>	Specifies how to pad values that don’t occupy the entire field width
<align>	Specifies how to justify values that don’t occupy the entire field width
<sign>	Controls whether a leading sign is included for numeric values
#	Selects an alternate output form for certain presentation types
0	Causes values to be padded on the left with zeros instead of ASCII space characters
<width>	Specifies the minimum width of the output
<group>	Specifies a grouping character for numeric output
.<prec>	Specifies the number of digits after the decimal point for floating-point presentation types, and the maximum output width for string presentations types
<type>	Specifies the presentation type, which is the type of conversion performed on the corresponding argument'''

'''Type Specifying :
More parameters can be included within the curly braces of our syntax. Use the format code syntax {field_name:conversion}, 
where field_name specifies the index number of the argument to the str.format() method, and conversion refers to the 
conversion code of the data type.

s – strings
d – decimal integers (base-10)
f – floating point display
c – character
b – binary
o – octal
x – hexadecimal with lowercase letters after 9
X – hexadecimal with uppercase letters after 9
e – exponent notation
% - percentage

'''

#Types

print ("This site is {0}!!".
       format(100))

print ("This site is {0:b}!!".
       format(100))

print ("This site is {0:f}!!".
       format(100))

print ("This site is {0:c}!!".
       format(100))

print ("This site is {0:b}!!".
       format(100))

print ("This site is {0:o}!!".
       format(100))

print ("This site is {0:x}!!".
       format(100))

print ("This site is {0:e}!!".
       format(100))

print ("This site is {0:%}!!".
       format(0.5))

# To limit the precision
print ("My average of this {0} was {1:.0f}"
       .format("semester", 78.2))

# For no decimal places
print ("My average of this {0} was {1:.0f}%"
       .format("semester", 78.234876))

print ("My average of this {0} was {1:%}"
       .format("semester", 0.78234876))

print ("My average of this {0} was {1:.1%}"
       .format("semester", 0.78234876))


'''The <fill> and <align> Subcomponents
<fill> and <align> control how formatted output is padded and positioned within the specified field width. These subcomponents only have meaning when the formatted field value doesn’t occupy the entire field width, which can only happen if a minimum field width is specified with <width>. If <width> isn’t specified, then <fill> and <align> are effectively ignored. You’ll cover <width> later on in this tutorial.

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field'''

# To demonstrate spacing when
# strings are passed as parameters
print("{0:6}, is the computer science portal for {1:^20}!"
      .format(12, "geeks"))

# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
      .format("40"))

# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
      .format("GeeksforGeeks", 2009))


# To demonstrate aligning of spaces
print("{0:->16} was founded in {1:<4}!"
      .format("Geeks", 2009))

print("{:*^20s}".format("Geeks"))


#grouping
print('{0:,.2f}'.format(1234543423467.8947727).replace(".",";").replace(",",".").replace(";",","))
print('{0:_.2f}'.format(1234543423467.8947727))



# which prints out i, i ^ 2, i ^ 3,
#  i ^ 4 in the given range

# Function prints out values
# in an unorganized manner
def unorganized(a, b):
    for i in range (a, b):
        print ( i, i**2, i**3, i**4 )

    # Function prints the organized set of values
def organized(a, b):
    for i in range (a, b):

        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))

unorganized(1,5)
organized(1,5)



parametros = {"servidor":"google.com"
              ,"puerto":"8080"
                ,"funcionalidad":"action"
              ,"instrumento":"GGAL"
              ,"otrovalor":"juan"
              ,"mascosas":"tute"}

url = "http://{servidor}:{puerto}/{funcionalidad}/{instrumento}".format(**parametros)

#url = "http://{servidor:50}:{puerto}/{funcionalidad}/{instrumento}".format(servidor="google.com",puerto="8990",funcionalidad="action",instrumento="GGAL")

print(url)

name="matias"
print(f"imprimi {name:>10}    {name:<10}")
print(f"tambien puedo ejecutar expresiones del estilo 2*3 = {2*3:10}")
to_upper = "en mayusculas"
print(f"o llamar a funciones {to_upper.upper()}")
x=11
print(f"el numero es {'mayor' if x > 10 else 'menor'}")

'''
Here’s a speed comparison:

>>> import timeit
>>> timeit.timeit("""name = "Eric"
... age = 74
... '%s is %s.' % (name, age)""", number = 10000)
0.003324444866599663

>>> timeit.timeit("""name = "Eric"
... age = 74
... '{} is {}.'.format(name, age)""", number = 10000)
0.004242089427570761

>>> timeit.timeit("""name = "Eric"
... age = 74
... f'{name} is {age}.'""", number = 10000)
0.0024820892040722242
As you can see, f-strings come out on top.'''

texto = '''Tambien puedo guardar en una variable
            Texto en varias lineas
            siempre y cuando ese texto esté entre comillas triples'''

print(texto)