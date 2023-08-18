''''
Operator	Name	        Example	Try it
+	        Addition	        x + y
-	        Subtraction	        x - y
*	        Multiplication	    x * y
/	        Division	        x / y
%	        Modulus	            x % y
**	        Exponentiation	    x ** y
//	        Floor division	x // y
'''

# Operaciones aritmeticas que puedo hacer entre strings
operand1 = "string1"
operand2 = "string2"


print(operand1+operand2)
print(operand1-operand2)
print(operand1*operand2)
print(operand1/operand2)
print(operand1%operand2)
print(operand1**operand2)

# Operaciones aritmeticas que puedo hacer entre enteros
operand1 = 11
operand2 = 3

print(operand1 + operand2)
print(operand1 - operand2)
print(operand1 * operand2)
print(operand1 ** operand2)
print(operand1 / operand2)
print(operand1 % operand2)  # por ejemplo se puede utilizar para encontrar multiplos
print(operand1 // operand2)  # por ejemplo se puede utilizar para obtener los nominales a operar

# Operaciones aritmeticas que puedo hacer entre un string y un numero
operand1 = "-"
operand2 = 10

# print(operand1+operand2)
# print(operand1-operand2)
print(operand1*operand2)
# print(operand1/operand2)
# print(operand1%operand2)
# print(operand1**operand2)

# Quiero modificar el contenido de mi variable aplicandole algun operador algebraico
operand1 = 0
operand1 += 1
operand1 = operand1 + 1
operand1 += 1
print(operand1)
#esto mismo se puede hacer con todos los operadores
operand1 *= 4
print(operand1)

# Operaciones aritmeticas entre booleanos. Se comportan como si fueran ceros o unos.
operand1 = False  # 0
operand2 = True  # 1

print(operand1+operand2)
print(operand1-operand2)
print(operand1*operand2)
print(operand1/operand2)
print(operand1%operand2)
print(operand1**operand2)
print(bool(0))
print(bool(1))
print(True+True)


'''Operator	Example	Same As	Try it
=	        x = 5	x = 5	
+=	        x += 3	x = x + 3	
-=	        x -= 3	x = x - 3	
*=	        x *= 3	x = x * 3	
/=	        x /= 3	x = x / 3	
%=	        x %= 3	x = x % 3	
//=	        x //= 3	x = x // 3	
**=	        x **= 3	x = x ** 3
'''