'''List

Una lista es una coleccion que esta ordenada y es modificable.
En Python las listas se escriben con corchetes y los elementos se separan con comas.
'''

### SINTAXIS
# Creamos una lista
thislist = ["apple", "banana", "cherry"]  # utilizamos corchetes y separamos los elementos con comas
print(thislist)

# hoy estaremos utilizando el shortcut alt + shift + e para ejecutar el codigo seleccionado

#############################################
# ACCEDEMOS A LOS ELEMENTOS
#############################################

'''
Acceder a los elementos de una lista
Se puede accerdea los elementos de una lista utilizando el nombre de la lista y el indice del elemento que queremos acceder.
'''

# Accedemos e imprimimos el segundo elemento de la lista
# En python los indices comienzan en 0 (zero based indexing)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

'''
Indexado negativo
Python tambien permite el indexado negativo, esto significa que comienza a contar desde el final de la lista.
-1 es el ultimo elemento de la lista
-2 es el penultimo elemento de la lista
'''

# Imprimimos el ultimo elemento de la lista
# Como los indices comienzan en 0, el ultimo elemento de la lista es el n-1. No me interesa saber el tamaño de la lista.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


'''
Quiero acceder a un rango de elementos de una lista
Para acceder a un rango de una lista, debo especificar donde comienza el rango y donde termina el rango.
Para acceder a un rango de elementos de una lista, se utiliza el operador de rango " : "

El retorno sera una NUEVA lista con los elementos especificados.
Esto se llama slice operator
'''

# Hago un slice y obtengo una nueva lista con los elementos desde el indice 2 hasta el indice 5
# El rango comenzara en el indice 2 (incluido) y terminara en el indice 5 (no incluido).
# Como vimos con range en la clase pasada
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist)
print(thislist[-4:-1])

'''
Si dejo el primer indice vacio, el rango comenzara desde el principio de la lista
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[:-3])  # tambien con indices negativos


'''
Si dejo el segundo indice vacio, el rango terminara en el final de la lista
'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print(thislist[-1:])

'''
Rango de indices negativos
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


'''
Range
Le puedo especificar un tercer parametro al slice operator
Este parametro sera el step, que es cada cuantos elementos quiero que me devuelva.
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[::2])
print(thislist[1::2])


#############################################
# MODIFICAR ELEMENTOS
#############################################


'''
Cambiar el valor de un elemento de una lista
Para cambiar el valor de un elemento de una lista, debo acceder al elemento y asignarle un nuevo valor.
'''

thislist = ["apple", "banana", "cherry"]
thislist[1] = "mango"
print(thislist)

#############################################
# RECORRER UNA LISTA
#############################################


'''
Recorrer una lista
Podemos recorrer una lista utilizando un for
'''

thislist = ["apple", "banana", "cherry"]

for x in thislist:  # x es el elemento de la lista
    print(x)

# A veces necesitamos saber ademas del valor, tambien el indice del elemento
for x in range(len(thislist)):  # x es el indice del elemento de la lista.
    # Len me devuelve el tamaño de la lista y range me devuelve una lista de numeros desde 0 hasta el tamaño de la lista
    print(x, thislist[x])  # Imprimo el indice y el elemento de la lista
    #print()

'''
Chequear si un elemento esta en una lista
Se utiliza el operador in
'''

# chequeamos si apple esta en la lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

else:
    print('no esta')


'''List Length
To determine how many items a list has, use the len() function:

Example
Print the number of items in the list:'''

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#############################################
# MANIPULAR ELEMENTOS
#############################################


'''
Para agregar un elemento a una lista, se utiliza el metodo append()
Se agrega el elemento al final de la lista

*Un metodo es una funcion que pertenece a un objeto.
Para llamar un metodo utilizamos el nombre del objeto, un punto y el nombre del metodo seguido de parentesis.
Por ejemplo append() es un metodo de las listas.

'''

# agregamos un elemento a la lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# METODO INDEX
# El metodo index() devuelve el indice del elemento especificado.
# Si existen mas de un elemento con el mismo valor, devuelve el indice del primer elemento que encuentre.
thislist = ["banana", "apple", "cherry", "apple"]
print(thislist.index("apple"))
print(thislist.index("apple", 2))  # Busca el elemento apple desde el indice 2

'''
Insertar un valor
Para insertar un elemento en una posicion especifica, se utiliza el metodo insert()
'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # el primer parametro es el indice donde quiero insertar el elemento
# Donde quedará orange en la lista?
print(thislist)


'''
Eliminar un elemento
Existen varios metodos para eliminar un elemento de una lista
'''

# Remove
# Utilizando el metodo remove se elimina el elemento especificado
# El elemento a eliminar debe existir en la lista, sino da error
thislist = ["apple", "banana", "cherry"]
thislist.remove('banana')
print(thislist)


# Pop
# El metodo pop() elimina el elemento del indice especificado
# Si no se especifica el indice, se elimina el ultimo elemento
thislist = ["apple", "banana", "cherry"]
variable = thislist.pop()  # Almaceno el elemento eliminado en una variable
print(thislist)
print(variable)

# Del
# Con del puedo eliminar un elemento de una lista utilizando el indice
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# Puedo eliminar una lista entera utilizando del
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

# Clear
# Si quiero vaciar una lista, pero no eliminarla, puedo utilizar el metodo clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#############################################
# *** IMPORTANTE ***
#############################################
'''
Una lista es un objeto
Cuando yo creo una lista, en memoria se crea un objeto que contiene los elementos de la lista.
Cuando le asigno una lista a una variable, la variable no contiene la lista, sino que contiene una REFERENCIA dicho lugar en memoria.
'''

thislist = ["apple", "banana", "cherry"]  # creo una lista y la referencio con la variable thislist
mylist = thislist  # creo una variable mylist y le asigno la variable thislist, esta variable no contiene la lista, sino que contiene una referencia a la lista
# Ahora estoy apuntando a la misma lista con dos variables distintas

thislist.append("otro")
mylist.append("unonuevo")
print(mylist)
print(thislist)

'''
Copiar una lista
No puedo copiar simplemente una lista utilizando el operador de asignacion list2 = list1
Porque list2 sera una referencia a list1, y los cambios que haga en list1 se haran automaticamente en list2

Existen varias formas de copiar una lista, una de ellas es utilizando el metodo copy()
'''

# Copy
thislist = ["apple", "banana", "cherry"]  # creo una lista y la referencio con la variable thislist

mylist = thislist.copy()  # ahora existen 2 listas, una referenciada por thislist y otra por mylist

thislist.append("otro")
mylist.append("unonuevo")
print(mylist)
print(thislist)


# List
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
mylist.append("nuevo")
print(mylist)
print(thislist)


'''
Concateno dos listas (join)
'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Utilizando el operador de suma
list3 = list1 + list2  # esta suma me devuelve una nueva lista con los elementos de list1 y list2
print(list3)
print(list1)
print(list2)


# Otra forma es agregar los elementos de una lista a otra lista
# Utilizando append
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Utilizando extend
# De esta manera no se crea una nueva lista, sino que se agregan los elementos de una lista a otra
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


'''The list() Constructor
It is also possible to use the list() constructor to make a new list.

Example
Using the list() constructor to make a List:'''

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)


'''List Methods
Python has a set of built-in methods that you can use on lists.

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list

*** sort()	    Sorts the list (siempre y cuando los elementos sean ordenables) *** '''