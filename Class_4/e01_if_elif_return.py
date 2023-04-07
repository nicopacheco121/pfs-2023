



number = 8


#usando elif
def oddOrEven(number):
    #voy a tomar el modulo de la division
    mod = number%2
    output = None
    if mod == 0:
        output = "even"
    elif mod == 1:
        output = "odd"
    elif mod == None:
        output = ""
    return output

print(oddOrEven(number))

def oddOrEven2(number):
    #voy a tomar el modulo de la division
    mod = number%2
    if mod == 0:
        return "even"
    else:
        return "odd"
    print("estoy por la linea 30")

    return False

def oddOrEven3(number):
    #voy a tomar el modulo de la division
    mod = number%2
    output = "odd"
    if mod == 0:
        output = "even"
    return output

def maximo(a,b,c):
    if a>b:
        if a>c:
            return a
        return c
    elif b>c:
        return b
    return c

def maximo2(a,b,c):
    resultado = c
    if a>b:
        if a>c:
            resultado = a
    elif b>c:
        resultado = b
    return resultado


print(maximo(4,10,8))
print(maximo(6,2,12))


def outOfBand(security,order):
    outOfBand = False
    priceLimitType = security.priceLimitType
    price = security.marketdata["LA"]["price"] if "LA" in security.marketdata and security.marketdata["LA"] and "price" in security.marketdata["LA"] and security.marketdata["LA"]["price"] else security.marketdata["CL"] if "CL" in security.marketdata and security.marketdata["CL"] else 0

    if (priceLimitType == "PRICE" and (order.price <= security.lowLimitPrice or order.price >= security.highLimitPrice)):
        outOfBand = True
    elif (price and priceLimitType == "PERCENTAGE" and ((order.side == "SELL" and order.price <= price*(1-security.lowLimitPrice/100)) or (order.side == "BUY" and order.price >= price*(1+security.highLimitPrice/100)))):
        outOfBand = True
    elif (price and priceLimitType == "HARD" and (order.price <= price*(1-security.lowLimitPrice/100) or (order.price >= price*(1+security.highLimitPrice/100)))):
        outOfBand = True
    return outOfBand


'''Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

Example
One line if statement:'''
a=15
b=10
if a > b: print("a is greater than b")


'''Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

Example
One line if else statement:'''

a = 2
b = 330
print("A") if a > b else print("B")
ambiente = "produccion"
#url = "http://www.rofexproduccion" if ambiente=="produccion" else None
url = "url de produccion" if ambiente == "produccion" else "url de pruebas"
if ambiente == "produccion":
    url = "url de produccion"
else:
    url = "url de pruebas"


'''This technique is known as Ternary Operators, or Conditional Expressions.

You can also have multiple else statements on the same line:

Example
One line if else statement, with 3 conditions:'''

a = 333
b = 335
print("A") if a > b else (print("=") if a == b else print("B") )

