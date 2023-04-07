name = "Patricio"

def myFirstFunction(unParametro):
    #Los parametros de las funciones son equivalentes a variables
    #Las variables declaradas dentro de una función solo existen dentro de la funcion
    variable1=6
    print("Hello "+str(unParametro))

variable1=10
myFirstFunction(variable1)

def sayHello2(nombre):
    #Las variables tienen precedencia según donde estan declaradas
    #Una variable declarada dentro de la funcion con el mismo nombre de un parametro, pisa su valor
    print("Hello",name)

sayHello2(name)
print(name)

def multiplicarAbsoluto(numero1, numero2=2, numero3=6):
   result =  numero1*numero2*numero3
   if result >0:
       return result
   else:
       return -result

valor=8
print(multiplicarAbsoluto(valor))
print(multiplicarAbsoluto(valor, 7))
print(multiplicarAbsoluto(numero2=4, numero3=7))
print(multiplicarAbsoluto(valor, numero3=7))
print(valor)

valor = multiplicarAbsoluto(valor, 4)
print(valor)