'''Escribir un programa que simule un carrito de compras. El programa debe permitir, dada una coleccion de items elegidos por
 un cliente y pre-configurados con precio, descuento y % de impuestos a aplicarle, calcular el total a abonar por un cliente, discriminando

a) Monto Neto, monto descuento, monto impuestos, monto bruto item x item
b) Monto Neto, monto descuento, monto impuestos, monto bruto Total del la compra
'''

# Qué estructura podemos usar? Lista, tupla, diccionario?


import random  # importamos el modulo random para generar numeros aleatorios

# BASE DE DATOS
productos = ["Leche", "Pan", "Chocolate", "Vino", "Manteca", "Cerveza"]

# Generamos un diccionario con los productos y sus precios, descuentos e impuestos.
# Lo hacemos de forma dinamica y aleatoria

almacen = {
    "A"+str(indice): {  # utilizamos un codigo de producto para identificarlo
        "nombre": producto,  # el nombre es un atributo mas del producto
        "precio": random.randint(50*(indice+1), 400),  # randint(a,b) devuelve un numero aleatorio entre a y b
        "descuento": random.randint(10, 20) / 100,
        "impuesto": random.randint(10, 21) / 100}

    for indice, producto in enumerate(productos)  # enumerate devuelve un indice y el elemento de la lista
}

# No utilizamos el nombre del producto ya que puede haber mas de un producto con el mismo nombre, y las claves deben
# ser unicas. Generando entonces el codigo de producto con el indice, nos aseguramos que sea unico.

print(almacen)


# GENERAMOS EL CARRITO DE COMPRAS

# Carrito segun una lista de tuplas
carrito = [
    (producto, random.randint(1, 6)) for producto in almacen if almacen[producto]["precio"] < 300
]  # generamos una lista de tuplas con los productos y la cantidad de cada uno. Solo elegimos los productos que cuestan
# menos de 300

# Carrito segun una lista de diccionarios
carrito2 = [
    {"producto": producto, "cantidad": random.randint(1, 6)} for producto in almacen if almacen[producto]["precio"] < 300
]

print(carrito)
print(carrito2)

# Hasta ahora solo hemos generado las estructuras necesarias, almacen y carrito. Ahora debemos procesarlas para obtener
# la factura

factura = []  # iremos guardando los datos de la factura en esta lista

# Vamos a generar los renglones de la factura para luego mostrarla en pantalla

for item in carrito2:  # vamos a ir iterando el carrito y generando los renglones de la factura

    # Cada item tiene 2 atributos, producto y cantidad
    prod = almacen[item["producto"]]  # obtenemos el producto del almacen
    cantidad = item["cantidad"]  # obtenemos la cantidad del item
    #prod = almacen[item[0]]
    #cantidad = item[1]

    # calculamos los montos
    neto = prod["precio"] * cantidad
    descuento = prod["descuento"] * neto
    impuesto = prod["impuesto"] * neto
    subtotal = neto - descuento + impuesto

    # Guardo un diccionario con los datos de la factura
    factura.append(
        {
            "nombre": prod["nombre"],
            "cantidad": cantidad,
            "neto": neto,
            "descuento": descuento,
            "impuesto": impuesto,
            "subtotal": subtotal
        }
    )

print(factura)

# Generamos el output de la factura


# Esto lo vemos mas adelante. Vamos a generar output con formato
print(f"{'Producto':10}  {'Cantidad'}     {'Neto':8}  {'Descuento'}   {'Impuesto'}    {'Subtotal'}")

total = 0  # inicializamos el total de la factura
for renglon in factura:
    total += renglon['subtotal']  # que hace el operador += ?

    # Imprimimos cada renglon de la factura
    print(f"{renglon['nombre']:10}  {renglon['cantidad']:7}     ${renglon['neto']:>8.2f}  ${renglon['descuento']:>6.2f}     ${renglon['impuesto']:>6.2f}  ${renglon['subtotal']:>8.2f}")

print(f"{'Total':*>52}    ${total:8.2f}")