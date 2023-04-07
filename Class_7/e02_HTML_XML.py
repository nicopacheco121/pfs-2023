import bs4

with open("cem.html",encoding="utf8") as html:
#html = requests.get("https://www.rofex.com.ar/cem/TickByTick.aspx",verify=False).text
    soup = bs4.BeautifulSoup(html,features="lxml")

table = soup.find('table',attrs={"id":"ctl00_ContentPlaceHolder1_gvFuturos"})

headers = [header.text for header in table.find_all('th')]

results = {}

for i,row in enumerate(table.find_all('tr')):
    if i == 0:
        continue
    item = None
    #inicializo un diccionario donde las claves son los titulos de las columnas
    #y los valores son 0
    data = {headers[i]:0 for i in range(1,len(headers))}
    for index,cel in enumerate(row.find_all('td')):
        if index == 0:
            #en la columna 0 siempre tenemos el nombre del porducto
            item = cel.text
            #inicializo el diccionario resultado con una lista vacia
            if not item in results:
                results[item] = []
        else:
            data[headers[index]] = cel.text
    #me queda una lista de diccionarios addentro de cada producto
    results[item].append(data)


print(headers)
print(results)
data = {}
for k,row in results.items():
    if not k in data:
        data[k] = {"precio":0,"volumen":0,"cantidad":0}
    for trade in row:
        data[k]["cantidad"] += 1
        data[k]["precio"] += float(trade["Precio"].replace(".","").replace(",","."))
        data[k]["volumen"] += int(trade["Volumen"])

for value in data.values():
    value["precio"] = round(value["precio"]/value["cantidad"])

print("{0:10} {1:10} {2:10} {3:10}".format("Instrumento","Precio Promedio","Volúmen","Cantidad op"))
for k,v in data.items():
    print("{0:12} {precio:>10} {volumen:>10} {cantidad:>10}".format(k,**v))


xml = '''<?xml version="1.0" encoding="UTF-8"?>
            <loginTicketRequest version="1.0">
                <header>
                    <uniqueId>{uniqueId}</uniqueId>
                    <generationTime>{generationTime}</generationTime>
                    <expirationTime>{expirationTime}</expirationTime>
                </header>
                <service>{service}</service>
            </loginTicketRequest>'''

import xmltodict
from base64 import b64decode
import datetime
try:
    with open("wsfe.txt","r") as t:
        tokenXML = t.read()
except FileNotFoundError:
    print("No existe el archivo")
if tokenXML:
    print("Found token in cache. Will see if it's still valid")
    dict = xmltodict.parse(tokenXML)
    token = dict["loginTicketResponse"]["credentials"]["token"]
    sign = dict["loginTicketResponse"]["credentials"]["sign"]
    decodedXML = b64decode(token)
    dictToken = xmltodict.parse(decodedXML)
    time = dictToken["sso"]["id"]["@exp_time"]
    validToken = datetime.datetime.now() < datetime.datetime.fromtimestamp(int(time))
print(validToken)