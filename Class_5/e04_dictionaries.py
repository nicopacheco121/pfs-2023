'''Dictionary
Es una coleccion desordenada y mutable
Es indexada, pero no se indexa por numeros, sino por claves

Se escriben con llaves {} y tienen claves y valores
Las claves de un diccionario funcionan como un conjunto, es decir, no pueden haber claves repetidas
'''

### SINTAXIS
# Creamos un diccionario
thisdict = {
    "brand": "Ford",  # clave: valor
    "model": "Mustang",
    "year": 1964,
}
print(thisdict)


#############################################
# ACCEDEMOS A LOS ELEMENTOS
#############################################
'''
Accedemos a los elementos referenciando a la clave
Si la clave no existe, da error
'''

x = thisdict["model"]
print(x)


'''
Hay un metodo llamado get() que hace lo mismo.
Pero si la clave no existe, no da error, sino que devuelve None
'''
x = thisdict.get("model")
# x = thisdict.get("motor")
print(x)


#############################################
# MODIFICAR ELEMENTOS
#############################################


'''Change Values
Podemos cambiar el valor de un elemento referenciando a su clave
'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    'km': 100000
}

thisdict["km"] = 10  # modifico el valor de la clave km

print(thisdict)


#############################################
# RECORRER UN DICCIONARIO
#############################################

'''Loop Through a Dictionary
Podemos recorrer un diccionario con un bucle for

El bucle for recorre las claves del diccionario
'''

for x in thisdict:  # recorro las claves del diccionario
    print(x)

# Recorro las claves y accedo a los valores
for x in thisdict:
    print(thisdict[x])


'''
Vemos 3 metodos para recorrer el diccionario
'''

# values, para acceder a los valores
for x in thisdict.values():  # .values devuelve una lista con los valores
    print(x)

# keys, para acceder a las claves
for x in thisdict.keys():  # .keys devuelve una lista con las claves
    print(x)

# items, para acceder a los pares clave-valor
for x in thisdict.items():  # .items devuelve una lista con los pares clave-valor
    print(x)


print(thisdict)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())


'''
Check si una clave o un valor existe
'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# chequeamos si existe una key
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# otra forma de hacer lo mismo
if "model" in thisdict.keys():
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# chequeamos si un valor existe
if 'Mustang' in thisdict.values():
    print("Yes, 'Mustang' is one of the values in the thisdict dictionary")

'''
Cantidad de elementos
'''

print(len(thisdict))

#############################################
# MANIPULAR ELEMENTOS
#############################################
'''
Agregar elementos
Se agrega un elemento referenciando a una NUEVA clave
'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

if "color" not in thisdict:
    thisdict["color"] = "red"

print(thisdict)

# Si a una clave existente le asigno un valor, lo MODIFICO
thisdict['color'] = 'blue'
print(thisdict)

# *** Si la clave no existe, la crea, y si existe, la modifica


'''Remover elementos
Hay distintas formas
pop
popitem
del
'''

# Pop remueve el elemento con la clave indicada
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
valor = thisdict.pop("model")  # remueve el elemento con la clave indicada y devuelve el valor
print(thisdict)
print(valor)


# Popitem remueve el ultimo elemento
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


valor = thisdict.popitem()  # remueve el ultimo elemento y devuelve una tupla con la clave y el valor
print(thisdict)
print(valor)


# Del remueve el elemento con la clave indicada
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)


'''Example
The del keyword can also delete the dictionary completely:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


del thisdict
# print(thisdict)
#this will cause an error because "thisdict" no longer exists.


'''Example
The clear() method empties the dictionary:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)


#############################################
# *** IMPORTANTE ***
#############################################

'''Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Example
Make a copy of a dictionary with the copy() method:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict  # mydict es una referencia a thisdict
mydict["matias"] = "nuevaclave"  # modifico mydict
print(mydict)
print(thisdict)

'''Another way to make a copy is to use the built-in method dict().

Example
Make a copy of a dictionary with the dict() method:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)  # mydict es una COPIA de thisdict
print(mydict)

mydict = mydict.copy()  # mydict es una COPIA de mydict
print(mydict)


'''
Un diccionario puede contener diccionarios, esto se llama diccionarios anidados.
'''

# en este diccionario tengo 3 claves, donde el value de cada clave es un diccionario
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

'''
Tambien puedo aniadir diccionarios a un diccionario existente
'''

# Creo 3 diccionarios
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

# Creo un diccionario y a cada clave le asigno un diccionario previamente creado
myfamily = {
    "child1": child1,
    "child2" : child2,
    "child3" : child3
}


### Para acceder a los valores de un diccionario anidado, referencio a la clave del diccionario anidado

print(myfamily)

# Accedo a los valores del diccionario anidado
# Utilizo el subindice.
# Con myfamily["child1"] accedo al diccionario child1 y con ["year"] accedo al valor de la clave year
print(myfamily["child1"]["year"])

# Modifico el valor de la clave year del diccionario child3
myfamily["child3"]["year"] = 2020  # modifico el valor de la clave year del diccionario child3
print(myfamily["child3"]["year"])
print(child3["year"])  # que pasa si imprimo esto? por que me da este valor?


child3["year"] = 2040  # modifico el valor como hice antes
print(myfamily["child3"]["year"])  # que pasa si imprimo esto? por que me da este valor?



'''The dict() Constructor
It is also possible to use the dict() constructor to make a new dictionary:

Example'''
thisdict = dict(brand="Ford", model="Mustang", year=1964)  # la clave va sin comillas
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


'''Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, 
                with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''