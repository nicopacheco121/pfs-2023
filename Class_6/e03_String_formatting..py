
"""

FORMAR


"""

age = 36
txt = "My name is John, and I am {}"  # {} es un placeholder
print(txt.format(age))
# no hizo falta cambiar age a string, lo hizo automaticamente

# Si tengo 2 placeholders, tengo que pasar 2 argumentos
age = 36
txt = "My name is John, and I am {}{}"
print(txt.format(True, age))  # el primer {} se reemplaza por True, el segundo por age

### NO ME TENGO QUE PREOCUPAR POR EL TIPO DE DATO

'''El orden de los argumentos es el orden en el que se reemplazan los placeholders'''
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print(myorder.format(quantity, price, itemno))


'''
Si quisiera repetir un argumento, puedo hacerlo de 2 formas
'''

# Puedo utilizar indices para asegurarme que los argumentos se reemplacen en los placeholders correctos
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1} {2} {0} {0}."

print(myorder.format(quantity, itemno, price))  # el primer argumento es el 0, el segundo el 1, etc

# Puedo utilizar nombres para los argumentos, pares clave-valor
q = 3
itemno = 567
precio = 49.95
myorder = "I want to pay {price} dollars for {quantity} pieces of item {itemno}."

print(myorder.format(quantity=itemno, itemno=itemno, price=precio))  # no nos interesa el orden



'''
FORMATO DE SALIDA
Hasta ahora no indicamos el formato de salida. Ahora vamos a ver como hacerlo.

El formato de salida se especifica despues de los : en el placeholder

{[<name>][!<conversion>][:<format_spec>]}

<format_spec> represents the guts of the Python .format() method’s functionality. 
It contains information that exerts fine control over how values are formatted prior to being inserted into the template string. 

The general form is this:
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


print ("This site is {0}!!".
       format(100))  # no le indico el tipo, por defecto es string

print ("This site is {0:b}!!".
       format(100))  # b es para binario

print ("This site is {0:f}!!".
       format(100))  # f es para float

print ("This site is {0:%}!!".
       format(0.5))  # % es para porcentaje


print ("This site is {0:c}!!".
       format(100))
print ("This site is {0:o}!!".
       format(100))
print ("This site is {0:x}!!".
       format(100))
print ("This site is {0:e}!!".
       format(100))



# Especificar la cantidad de decimales
print ("My average of this {0} was {1:.5f}"
       .format("semester", 78.2))
# Estoy utilizando numeros para los placeholders. El segundo argumento es un float y le indico
# con el .5 que quiero 5 decimales y con la f que es un float


# Salteamos, queda para que lo vean
# For no decimal places
print ("My average of this {0} was {1:.1f}    %"
       .format("semester", 78.294876))
print ("My average of this {0} was {1:%}"
       .format("semester", 0.78234876))
print ("My average of this {0} was {1:.1%}"
       .format("semester", 0.78234876))


'''
fill y align

fill y align son subcomponentes de <format_spec> que controlan como se rellena y posiciona el valor dentro del campo especificado
Dichos componentes solo tienen sentido cuando el valor no ocupa todo el ancho del campo, lo cual solo puede pasar si especificamos un ancho minimo con <width>
Si no especificamos <width>, entonces <fill> y <align> son ignorados

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field'''

# Luego de los dos puntos le puedo indicar cuanto quiero que ocupe el string
# Y tambien le puedo indicar como quiero que este posicionado dentro del campo
# Utilizando strings la alineacion es a la izquierda por defecto
print("{0:6}, is the computer science portal for {1:^20}!"
      .format('hola', "geeks"))

# Cuando es un entero la alineacion es a la derecha
print("It is {0:5} degrees outside !"
      .format(40))

# numeros y strings
print("{0:40} was founded in {1:16}!"
      .format("GeeksforGeeks", 2009))


# FILL, para rellenar con un caracter
print("{0:*>16} was founded in {1:<6}!"
      .format("Geeks", 2009))
# luego de los dos puntos, le indico el caracter con el que quiero rellenar

print("{:*^20s}".format("Geeks"))


#grouping
# Se utiliza para separar los miles, se puede con coma o con underscore
print('{0:,.2f}'.format(1234543423467.8947727))  # 2f que quiere decir?
print('{0:_.2f}'.format(1234543423467.8947727))


# Separamos miles cambiando la coma por un punto y luego reemplazamos el punto por una coma
print('{0:,.2f}'.format(1234543423467.8947727).replace(".",";").replace(",",".").replace(';', ','))




"""
Forma organizada y no organizada de imprimir valores
"""


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


"""
Tambien es util para api rest.

Podemos armar la url con un diccionario
"""
parametros = {
    "servidor": "google.com",
    "puerto": "8080",
    "funcionalidad": "action",
    "instrumento": "GGAL",
    "otrovalor": "juan",  # puede tener valores que no se utilicen
    "mascosas": "tute"
}

# utilizamos ** para pasarle los parametros del diccionario a la funcion format. Le paso clave-valor
url = "http://{servidor}:{puerto}/{funcionalidad}/{instrumento}".format(**parametros)

#url = "http://{servidor:50}:{puerto}/{funcionalidad}/{instrumento}".format(servidor="google.com",puerto="8990",funcionalidad="action",instrumento="GGAL")

print(url)

"""

F STRINGS


"""

name = "matias"
print(f'hola {name}')  # f string

# Funciona igual que el format.
print(f"imprimi {name:>10}    {name:<10}")  # el primer name se imprima la derecha y con 10 caracteres
print(f"tambien puedo ejecutar expresiones del estilo 2*3 = {2*3:10}")

# Puedo llamar a metodos
to_upper = "en mayusculas"
print(f"o llamar a funciones {to_upper.upper()}")

# Puedo generar output dinamicos
x = 8
print(f"el numero es {'mayor' if x > 10 else 'menor'}")  # Le agrego un if dentro del placeholder


'''
Here’s a speed comparison:

La libreria timeit sirve para medir el tiempo de ejecucion de un codigo

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


# Puedo generar un string multilinea
texto = '''Tambien puedo guardar en una variable
            Texto en varias lineas
            siempre y cuando ese texto esté entre comillas triples'''

print(texto)