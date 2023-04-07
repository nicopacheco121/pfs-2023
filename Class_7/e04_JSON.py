'''
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.
It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard
ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions
that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others.
These properties make JSON an ideal data-interchange language.

JSON is built on two structures:

A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash
table, keyed list, or associative array.
An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.
These are universal data structures. Virtually all modern programming languages support them in one form or another. It
makes sense that a data format that is interchangeable with programming languages also be based on these structures.

Example
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}
'''

import json

file = open("trades.json","r")
trades = json.load(file)
print(type(trades))
print(type(trades["trades"]))
print(trades["trades"])

output = {"poc":{}}
for trade in trades["trades"]:
    date = trade["datetime"].split(" ")[0]
    if not date in output:
        output[date] = {"precio":0,"volumen":0,"cantidad":0}
    output[date]["precio"] += trade["price"]
    output[date]["volumen"] += trade["size"]
    output[date]["cantidad"] += 1
    pocprice = trade["price"]//100*100
    if not pocprice in output["poc"]:
        output["poc"][pocprice] = 0
    output["poc"][pocprice] += trade["size"]

for k,item in output.items():
    if k != "poc":
        item["precio"] /= item["cantidad"]

print("{0:10} {1:10} {2:10} {3:10}".format("Fecha","Precio Promedio","Volúmen","Cantidad op"))
for k,v in output.items():
    if k != "poc":
        print("{0:12} {precio:>10.0f} {volumen:>10.0f} {cantidad:>10}".format(k,**v))


print("Precio","Cantidad")
for k in sorted(output["poc"].keys(),reverse=True):
    print(k,int(output["poc"][k])//50*"|")


import random
import csv
productos = ["Leche","Pan","Chocolate","Vino","Manteca","Cerveza"]

almacen = {"A"+str(indice):{"nombre":producto
    ,"precio":random.randint(50*(indice+1),400)
    ,"descuento":random.randint(10,20)/100
    ,"impuesto":random.randint(10,21)/100} for indice,producto in enumerate(productos)}

with open("productos.txt","a+") as filealmacen:
    json.dump(almacen,filealmacen)