'''

Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Example
Get the character at position 1 (remember that the first character has the position 0):'''

a = "Hello, World!"
print(a[1])


'''Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example
Get the characters from position 2 to position 5 (not included):'''

b = "Hello, World!"
print(b[2:5])

'''Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters from position 5 to position 1, starting the count from the end of the string:'''

b = "Hello, World!"
print(b[-5:])


'''String Length
To get the length of a string, use the len() function.

Example
The len() function returns the length of a string:'''

a = "Hello, World!"
print(len(a))
