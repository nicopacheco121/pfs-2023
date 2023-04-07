x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

x = "global"

def faa():
    x = x * 2
    print(x)

faa()


def fee():
    y = "local"


fee()
print(y)


def fii():
    y = "local"
    print(y)

fii()

x = "global "

def fuu():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

fuu()

x = 5

def fo():
    x = 10
    print("local x:", x)


fo()
print("global x:", x)