'''1- Escribir una función que implemente el operador XOR del algebra de Boole'''




'''2- Escribir  un  programa  que  le  pregunte  al  usuario  una  cantidad  de  pesos,  una  tasa  de  interés
y  un  número  de  años  y   muestre  como  resultado  el  monto  final  a   obtener.  La  fórmula  a   utilizar
es:
Cn  =   C   ×   (1  +   x/100)n
Donde  C   es  el  capital  inicial,  x   es  la  tasa  de  interés  y   n   es  el  número  de  años  a   calcular.'''


'''3- Escribir  un  programa  que  convierta  un  valor  dado  en  grados  Fahrenheit  a   grados  Celsius.
Recordar  que  la  fórmula  para  la  conversión  es:  F   =   (9/5)  C   +   32'''


'''4- Implementar  algoritmos  que  permitan: (Googlear formulas si no las recuerdan)
a)  Calcular  el  perímetro  y   área  de  un  rectángulo  dada  su  base  y   su  altura.
b)  Calcular  el  perímetro  y   área  de  un  círculo  dado  su  radio.
c)  Calcular  el  volumen  de  una  esfera  dado  su  radio.
d)  Calcular  el  área  de  un  rectángulo  (alineado  con  los  ejes  x   e   y)  dadas  sus
coordenadas  x1,x2,y1,y2.
e)  Dados  los  catetos  de  un  triángulo  rectángulo,  calcular  su  hipotenusa'''



'''5- Escribir una funcion que convierta una cantidad expresada en litros a galones. La funcion debe tener un parametro
opcional que determine si la conversión se hará a galones imperiales o galones americanos. Googlear las conversiones
necesarias para realizar el cálculo'''


'''6- Escribir una funcion recursiva que calcule cuantas veces se puede dividir a un número por 2 y que la parte entera
del resultado sea mayor a 0
Por ejemplo, el numero 100 se lo puede dividir 6 veces por 2
100 / 2 = 50
50 / 2 = 25
25 / 2 = 12.5
12 / 2 = 6
6 / 2 = 3
3 / 2 = 1
1 / 2 = 0.5 fin'''



'''7- escribir una funcion lambda que tome dos parametros y diga si el primero es mutliplo del segundo'''



'''8- Esccribir una funcion que dado un tipo de BANDA (FIJA, PORCENTAJE o PRICE),devuelva si un precio esta o no dentro de una banda

Ejemplo: 
Para la banda FIJA, el rango valido se calcula con con un porcentaje sobre el ultimo operado (ej para 5% y ultimo operado 100 Low=95 - High = 105). 
Solo se aceptan precios entre 95 y 105 sean compras o ventas
Para banda de PORCENTAJE el low y high son dinamicos segun el ultimo operado +- porcentaje (ej para 5% y ultimo operado 100 Low=95 - High = 105)
se aceptan compras en el rango 0 - 105 y ventas en el rango 95 - +inf. No se aceptan compras > 105 ni ventas menor 95
Para banda de PRICE tenemos los valores de banda definidos y no dependen del ultimo operado. Se comportan como banda FIJA'''

def checkPriceBand(side,price,tipo):
    porcentaje = 5
    ultimo = 100