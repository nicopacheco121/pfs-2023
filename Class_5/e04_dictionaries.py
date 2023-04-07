'''Dictionary
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.

Example
Create and print a dictionary:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


'''Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:'''

x = thisdict["model"]
print(x)


'''There is also a method called get() that will give you the same result:

Example
Get the value of the "model" key:'''

x = thisdict.get("model")
print(x)

'''Change Values
You can change the value of a specific item by referring to its key name:

Example
Change the "year" to 2018:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

print(thisdict)

'''Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example
Print all key names in the dictionary, one by one:'''

for x in thisdict:
    print(x)


'''Example
Print all values in the dictionary, one by one:'''

for x in thisdict:
    print(thisdict[x])


'''Example
You can also use the values() function to return values of a dictionary:'''

for x in thisdict.values():
    print(x)


'''Example
Loop through both keys and values, by using the items() function:'''

for x, y in thisdict.items():
    print(x, y)


'''Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

Example
Check if "model" is present in the dictionary:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


'''Dictionary Length
To determine how many items (key-value pairs) a dictionary has, use the len() method.

Example
Print the number of items in the dictionary:'''

print(len(thisdict))


'''Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

Example'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
if "color" not in thisdict:
    thisdict["color"] = "red"

print(thisdict)


'''Removing Items
There are several methods to remove items from a dictionary:

Example
The pop() method removes the item with the specified key name:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
valor = thisdict.pop("model")
print(thisdict)
print(valor)


'''Example
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
valor = thisdict.popitem()
print(thisdict)
print(valor)

'''Example
The del keyword removes the item with the specified key name:'''

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
print(thisdict) #this will cause an error because "thisdict" no longer exists.


'''Example
The clear() method empties the dictionary:'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

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
mydict = thisdict.copy()
mydict["matias"]="nuevaclave"
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
mydict = dict(thisdict)
print(mydict)


'''Nested Dictionaries
A dictionary can also contain many dictionaries, this is called nested dictionaries.

Example
Create a dictionary that contain three dictionaries:'''

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

'''Or, if you want to nest three dictionaries that already exists as dictionaries:

Example
Create three dictionaries, than create one dictionary that will contain the other three dictionaries:'''

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

myfamily = {
    ("child1","Linus") : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)
print(myfamily[("child1","Linus")]["year"])
myfamily["child3"]["year"] = 2020
print(myfamily["child3"]["year"])
print(child3["year"])
child3["year"] = 2040
print(myfamily["child3"]["year"])

'''The dict() Constructor
It is also possible to use the dict() constructor to make a new dictionary:

Example'''
thisdict = dict(brand="Ford", model="Mustang", year=1964)
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

midiccionario = {}

midiccionario.setdefault("nombre","matias")
midiccionario.setdefault("nombre","juan")
print(midiccionario)