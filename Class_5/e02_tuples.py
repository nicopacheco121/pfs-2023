'''Tuple
Es una colección ordenada e inmutable.
Se escriben entre parentesis.

Lo que vimos en listas para acceder a los elementos, también se puede hacer en tuplas.
La tupla NO es modificable, entonces no se puede agregar, modificar ni eliminar elementos.
'''

### SINTAXIS
# Creamos una tupla
thistuple = ("apple", "banana", "cherry")
print(thistuple)


'''Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

Example
Print the second item in the tuple:'''

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


'''Negative Indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the tuple:'''

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


'''Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

Example
Return the third, fourth, and fifth item:'''

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


'''Note: The search will start at index 2 (included) and end at index 5 (not included).

Remember that the first item has index 0.'''

'''Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:

Example
This example returns the items from index -4 (included) to index -1 (excluded)'''

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#############################################
# *** IMPORTANTE ***
#############################################

'''
Cambiar el valor de una tupla
Una vez que se crea una tupla, no se pueden cambiar sus valores. Las tuplas son inmutables.
Pero hay una solución. Puede convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.
'''

x = ("apple", "banana", "cherry")  # creo una tupla y la asigno a la variable x
z = x  # asigno la tupla a la variable z
y = list(x)  # genero una lista a partir de la tupla y la asigno a la variable y
y[1] = "kiwi"  # modifico el valor de la lista
x = tuple(y)  # convierto la lista en tupla y la asigno a la variable x

print(x)  # que pasa si imprimo x?
print(z)  # que pasa si imprimo z?


'''Loop Through a Tuple
You can loop through the tuple items by using a for loop.

Example
Iterate through the items and print the values:'''

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


'''Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:

Example
Check if "apple" is present in the tuple:'''

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


'''Tuple Length
To determine how many items a tuple has, use the len() method:

Example
Print the number of items in the tuple:'''

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#############################################
# *** IMPORTANTE ***
#############################################
'''Add Items
Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

Example
You cannot add items to a tuple:'''

thistuple = ("apple", "banana", "cherry")
thistuple[2] = "orange" # This will raise an error
print(thistuple)


#############################################
# *** IMPORTANTE ***
#############################################
'''
Crear una tupla con UN elemento
Para crear una tupla con solo un elemento, debe agregar una coma después del elemento
'''

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


'''Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

Example
The del keyword can delete the tuple completely:'''

thistuple = ("apple", "banana", "cherry")
del thistuple[0]
print(thistuple) #this will raise an error because the tuple no longer exists


'''Join Two Tuples
To join two or more tuples you can use the + operator:

Example
Join two tuples:'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

'''The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

Example
Using the tuple() method to make a tuple:'''

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#############################################
# *** IMPORTANTE ***
#############################################
'''Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found'''