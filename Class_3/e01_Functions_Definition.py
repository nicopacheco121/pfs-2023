#function with default parameters
def printLine(character="*",numberOfTimes=10):
    print(character*numberOfTimes)

#function with required parameters
def printShortLine(character):
    printLine(character,25)

def printLongLine(character):
    printLine(character,100)
