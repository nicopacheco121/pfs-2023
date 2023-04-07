# encoding: utf-8
import sys
# Usando el método items()
caballeros = {'gallahad': 'el puro', 'robin': 'el valiente'}

for k, v in caballeros.items():
    print (k, v)

for v in caballeros.keys():
    print(v)

for v in caballeros.values():
    print(v)


# Usando la función enumerate()
for i, v in enumerate(['ta', 'te', 'ti']):
    print (i, v)



# Usando la función zip()
preguntas = ['nombre', 'objetivo', 'color favorito']
respuestas = ['lancelot', 'el santo grial', 'azul']

for p, r in zip(preguntas, respuestas):
    print ('Cual es tu {0}?  {1}.'.format(p, r))


print({p:r for p, r in zip(preguntas, respuestas)})


    #print ('Cual es tu {0}?  {1}.'.format(p, r))

# Usando la función reversed()
for i in reversed(list(range(1, 10, 2))):
    print (i)

# Usando la función sorted()
canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana']
print(canasta)
#print(sorted(canasta))
#print(canasta)
canasta.sort()
#print(canasta)
for f in sorted(set(canasta)):
    print (f)
print (canasta)
