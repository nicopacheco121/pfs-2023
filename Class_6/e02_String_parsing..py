'''String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning'''
'''String Methods
Python has a set of built-in methods that you can use on strings.

Example
The strip() method removes any whitespace from the beginning or the end:'''

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


'''Example
The lower() method returns the string in lower case:'''

a = "Hello, World!"
print(a.lower())

'''Example
The upper() method returns the string in upper case:'''

a = "Hello, World!"
print(a.upper())

'''Example
The replace() method replaces a string with another string:'''

a = "Hello, World!"
print(a.replace("Hello", "Hola"))


'''Example
The split() method splits the string into substrings if it finds instances of the separator:'''

a = "Hello, World!"


print(a.split(" ")) # returns ['Hello', ' World!']

original_string = "ab_cd_ef"

split_string = original_string.split("_")

print(split_string)


print("dato: unmonton de cosas:$valor".split(":$")[1])
print("dato$: unmonton de cosas:$140".split("xxxxx"))



'''Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example
You will get an error if you use double quotes inside a string that is surrounded by double quotes:'''

#txt = "We are the so-called "Vikings" from the north."
'''To fix this problem, use the escape character \":

Example
The escape character allows you to use double quotes when you normally would not be allowed:'''

txt = "We are the so-called \"Vikings\" from the north."
txt = 'We are the so-called "Vikings" from the north.'
print(txt)

'''Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
'''


print(",".join([str(x) for x in range(1,100)]))

