'''Recursive functions are functions that call themselves'''

def factorial(numero):
    if numero == 1:
        return 1
    return numero*factorial(numero-1)

print(factorial(5))