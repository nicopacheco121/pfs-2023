for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#usando break y continue en fors anidados
for i in range(4):
    if i == 2:
        continue
    for j in range(4):
        if j==2:
            break
        print("The number is ",i,j)

'''sumar impares de la primer cadena con pares de la segunda'''
cadena1 = "1234"
cadena2 = "5678"

even = lambda y:y%2==0

result = 0
for l1 in cadena1:
    l1 = int(l1)
    if even(l1):
        continue
    for l2 in cadena2:
        l2 = int(l2)
        #si el pri
        if not even(l2):
            break
        result += l1+l2
    break

print(result)

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)