'''Lambda functions are a simple way of defining a 1 line function'''

def func(y):
    return y*2

x = lambda y : y * 2

print(x(10))


sumarize = lambda x,y,z: x+y+z

print(sumarize(4,1,6))

def condicion(valor=50):
    return valor >10.0 and valor<20.0

resultado = list(filter(lambda x: x%2==0,range(0,100)))
print(resultado)
variable = condicion
variable()
resultado2 = list(filter(condicion,range(0,100)))
print(resultado)
print(resultado2)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)


lista = [condicion,str,x,int]

for item in lista:
    print(item(12))

x(12)
condicion(12)
str(12)