'''Set
Es una coleccion desordenada y no indexada.
No permite duplicados.
Se escriben con llaves {}

Lo que vimos en listas para acceder a los elementos NO se puede utilizar en sets.
'''

### SINTAXIS
# Creamos un set
thisset = {"apple", "banana", "cherry", "banana", "banana"}
print(thisset)

conjunto = "voy a transformar una cadena de caracteres en un conjunto sin repetidos"
print(set(conjunto))  # toma cada caracter como un elemento del conjunto

print(list(conjunto))

#############################################
# ACCEDEMOS A LOS ELEMENTOS
#############################################
'''
Nota: Los conjuntos son desordenados, por lo que no se puede saber en que orden aparecerán los elementos.

Acceder a los elementos de un conjunto
No se puede acceder a los elementos de un conjunto haciendo referencia a un índice, ya que los conjuntos están desordenados los elementos no tienen índice.

Pero se puede recorrer con un bucle for, o preguntar si un valor especifico está presente en un conjunto, usando la palabra reservada in.
'''

thisset = {"apple", "banana", "cherry"}

print(thisset)
for x in sorted(thisset):  # sorted() ordena los elementos del conjunto. No lo modifica, si no que devuelve una lista ordenada
    print(x)

nueva = list(thisset)  # crea una lista con los elementos del conjunto
print(nueva)
nueva.sort(reverse=True)  # ordena la lista
print(nueva)  # como me queda la lista?

'''Example
Check if "banana" is present in the set:'''

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#############################################
# AGREGAMOS LOS ELEMENTOS
#############################################
'''Add Items
Para agregar un elemento a un conjunto, use el método add().
Para agregar más de un elemento a un conjunto, use el método update().
'''

# Add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Update
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "apple", "cherry"])

print(thisset)

'''Get the Length of a Set
To determine how many items a set has, use the len() method.

Example
Get the number of items in a set:'''

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#############################################
# ELIMINO ELEMENTOS
#############################################
'''Remove Item
Para eliminar un elemento en un conjunto, estan los métodos remove(), o discard().
'''

# Remove
# Si el valor no existe, remove() generará un error
thisset = {"apple", "banana", "cherry"}

thisset.remove("apple")

print(thisset)


# Discard
# Si el valor no existe, discard() NO generará un error
thisset = {"apple", "banana", "cherry"}

thisset.discard("matias")

print(thisset)


'''
Pop
Tambien se puede eliminar un elemento con el método pop(), este método eliminará el último elemento. 
Recuerde que los conjuntos están desordenados, por lo que no sabrá qué elemento se eliminará.
El valor de retorno de pop() es el elemento eliminado.
'''

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)


'''Clear
El método clear() vacía el conjunto:'''
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

'''Example
The del keyword will delete the set completely:'''

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


#############################################
# OPERADORES DE CONJUNTOS
#############################################

'''Join Two Sets
Existen varios métodos para unir dos o más conjuntos en Python.
Podemos usar el método union() que devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos, 
o el método update() que inserta todos los elementos de un conjunto en otro:
'''

# Union
set1 = {"a", "b", "c"}
set2 = {"a", 2, 3, "b", "c"}

set3 = set1.union(set2)  # une los elementos de set1 y set2 en un NUEVO conjunto
print(set3)
print(set1)

# Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)  # une los elementos de set2 en set1, MODIFICANDO set1
print(set1)
print(set2)


'''Note: Both union() and update() will exclude any duplicate items.

There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates, check the full list of set methods in the bottom of this page.

The set() Constructor
It is also possible to use the set() constructor to make a set.

Example
Using the set() constructor to make a set:'''

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

'''Set Methods
Python has a set of built-in methods that you can use on sets.

Method	            Description
add()	            Adds an element to the set
clear()	            Removes all the elements from the set
copy()	            Returns a copy of the set
difference()	    Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	        Remove the specified item
intersection()	    Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	    Returns whether two sets have a intersection or not
issubset()      	Returns whether another set contains this set or not
issuperset()	    Returns whether this set contains another set or not
pop()	            Removes an element from the set
remove()	        Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	            Return a set containing the union of sets
update()	        Update the set with the union of this set and others'''