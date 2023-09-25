"""
Retorno de valores
- Las funciones pueden retornar uno o varios valores.
- Si no se especifica un valor de retorno, la funcion devuelve None.
- El retorno puede ser cualquier tipo de dato.

- Vemos que devuelve la funcion noValue
- Que hace la funcion multiplyByTwo?
- Utilizamos el valor de retorno de la funcion multiplyByTwo para llamar a la funcion multiplyByTwo nuevamente

"""


def noValue(number1, number2):
    resultado = number1*number2
    print(resultado)

x = noValue(5,10)  # que valor tiene x?
print(x)


def multiplyByTwo(number):
    # print(multiplyTwoNumbers(number,2))
    return multiplyTwoNumbers(number,2)


def multiplyTwoNumbers(number1,number2):
    return number1*number2


y = multiplyByTwo(5)  # que valor tiene y?
print(y)

number = multiplyByTwo(5)  # que valor tiene number?

print(multiplyByTwo(number))

print(multiplyByTwo(multiplyByTwo(multiplyByTwo(18))))



