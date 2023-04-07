def greet(name):
    return "Hello, "+name+"!"
def simon(func):
    return func("Simon")
simon(greet)


def respect(maybe):
    def congrats():
        return "Congrats, bro!"
    def insult():
        return "You're silly!"
    if maybe == "yes":
        return congrats
    else:
        return insult

print(respect("no")())



def startstop(func):
    def wrapper(*params):
        print("Starting...")
        func(*params)
        print("Finished!")
    return wrapper


@startstop
def matias(a,b):
    print("Probando matias",a,b)


@startstop
def otrafunc(a,b,c,d):
    print("Probando el otrafunc",a,b,c,d)

matias(1,2)
otrafunc("a","b","c","d")

def safe(func):
    def wrapper(*params):
        try:
            func(*params)
            print("Finished!")
        except Exception as error:
            print(error)
    return wrapper

@safe
def nuevafuncion():
    return 3/0

nuevafuncion()
@safe
def funcionmultiple(parametro1,parametro2,parametro3):
    print(parametro1,parametro2,parametro3)
    return 3/0

funcionmultiple(4,6,8)
