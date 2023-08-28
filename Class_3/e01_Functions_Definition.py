"""
- Puedo tener un archivo que solo declare funciones
- Nos permite utilizar un archivo para tener funciones utiles
"""

# function with default parameters
def printLine(character="*",numberOfTimes=10):
    print(character*numberOfTimes)  # Que sucede cuando multiplico un string por un numero?

# function with required parameters
def printShortLine(character):
    printLine(character,25)

def printLongLine(character):
    printLine(character,100)
