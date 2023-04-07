'''Set
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

Example
Create a Set:'''

thisset = {"apple", "banana", "cherry","banana","banana"}
print(thisset)

conjunto = "voy a transformar una cadena de caracteres en un conjunto sin repetidos"
print(set(conjunto))


'''Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Access Items
You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

Example
Loop through the set, and print the values:'''

thisset = {"apple", "banana", "cherry"}

for x in sorted(thisset):
    print(x)

'''Example
Check if "banana" is present in the set:'''

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


'''Add Items
To add one item to a set use the add() method.

To add more than one item to a set use the update() method.

Example
Add an item to a set, using the add() method:'''

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


'''Example
Add multiple items to a set, using the update() method:'''

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "apple","cherry"])

print(thisset)

'''Get the Length of a Set
To determine how many items a set has, use the len() method.

Example
Get the number of items in a set:'''

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


'''Remove Item
To remove an item in a set, use the remove(), or the discard() method.

Example
Remove "banana" by using the remove() method:
Note: If the item to remove does not exist, remove() will raise an error.
'''

thisset = {"apple", "banana", "cherry"}

thisset.remove("matias")

print(thisset)


'''

Example
Remove "banana" by using the discard() method:
Note: If the item to remove does not exist, discard() will NOT raise an error.
'''

thisset = {"apple", "banana", "cherry"}

thisset.discard("matias")

print(thisset)


'''

You can also use the pop(), method to remove an item, but this method will remove the last item. 
Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.

Example
Remove the last item by using the pop() method:'''

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


'''Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

Example
The clear() method empties the set:'''

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

'''Example
The del keyword will delete the set completely:'''

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


'''Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

Example
The union() method returns a new set with all items from both sets:'''

set1 = {"a", "b" , "c"}
set2 = {"a", 2, 3}

set3 = set1.union(set2)
print(set3)
print(set1)

'''Example
The update() method inserts the items in set2 into set1:'''

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
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