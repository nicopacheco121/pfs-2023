"""
RECORREMOS ELEMENTOS CON ALGUNOS METODOS O FUNCIONES

"""

# Recorremos diccionarios utilizando items(), keys() y values()
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}

for k, v in caballeros.items():
    print(k, v)

for v in caballeros.keys():
    print(v)

for v in caballeros.values():
    print(v)

# Recorremos una lista utilizando enumerate()
# enumerate devuelve una tupla con el indice y el valor
for i, v in enumerate(['ta', 'te', 'ti']):
    print(i, v)

# Recorro 2 o mas listas a la vez
# Usando la función zip()
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']

for p, r in zip(preguntas, respuestas):  # p toma los valores de preguntas y r los de respuestas
    print(p, r)
    # print('Cual es tu {0}?  {1}.'.format(p, r))


# print({p:r for p, r in zip(preguntas, respuestas)})

# Recorremos una lista en orden inverso
# Usando la función reversed()
for i in reversed(list(range(1, 10, 2))):
    print(i)

# Recorremos una lista ordenando sus elementos
# Usando la función sorted()
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
print(canasta)
print(sorted(canasta))
print(canasta)  # la lista esta o no ordenada?

# Ordenamos la lista utilizando el método sort()
canasta.sort()
print(canasta)


for f in sorted(set(canasta)):
    print(f)
print(canasta)

