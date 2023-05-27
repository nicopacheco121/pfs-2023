import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import datetime

#
# # // libreria requests tiene los metodos dentro de la libreria
# # // OJO Los mensajes en http viajan en forma de texto, cualquiera los puede leer
# # // http vs httpS = https encripta la informacion
#
# response = requests.get("http://datacenter.matba.com.ar/ajustesdc.aspx", verify=False)
# # // en verify=False le estamos diciendo que no es necesario que verifique el certificado de seguridad
# # Debug y ver tipo status code, url y text
#
# panda = pd.read_html(
#     response.text,
#     # "http://datacenter.matba.com.ar/ajustesdc.aspx",  # tambien se puede poner directamente el url
#     attrs={"id":"ctl00_Cuerpo_ASPxPageControl1_ASPxCallbackPanel1_ASPxGridView1_DXMainTable"},  # buscar en la pagina la tabla
#     header=0,
#     decimal=',',
#     thousands='.',
#     encoding="utf-8")[0]
# # // La semana pasada con bs4 teniamos que poner a mano el header, separar miles, etc.
# # // Pandas me deja colocar la configuracion de la tabla a leer
# # // La parte artesanal de este trabajo va en identificar los hedaers, decimales, etc.
#
# panda.info()
# print(panda[["Posición","Cierre"]])

""" ----------------------------------------------------------------------------------------------- """

#
# url = "https://www.rofex.com.ar/cem/TickByTick.aspx"
# html = requests.get(url, verify=False).text
#
# panda = pd.read_html(
#     html,
#     attrs={'id': 'ctl00_ContentPlaceHolder1_gvFuturos'},
#     header=0,
#     decimal=',',
#     thousands='.')[0]
#
# # // Vemos la sumatoria de contratos y cantidad de operaciones por POSICION
# print(panda.groupby("Posición").agg({"Volumen": ["sum", "count"], "Precio": "mean"}))
#
# # // Vamos a generar nuevamente el perfil de volumen (lo hicimos la semana pasada)
# panda["precio_normalizado"] = (panda["Precio"] // 1000) * 1000
#
# result = panda.groupby(["Posición","precio_normalizado"]).Volumen.sum()  # Agrupamos posicion y precio normalizado y sumamos el volumen
# print(result.loc["RFX20062023"])
#
# result.loc["RFX20062023"].plot.barh()  # graficamos barras horizontales
# plt.show()  # mostramos el grafico
# #panda.to_excel("out.xlsx",index=False)  # guardamos el excel

""" ----------------------------------------------------------------------------------------------- """

# # // Vamos a buscar la cotizacion del dolar en el bna
#
# # Buscamos el url al que hay que pegarle
# response = requests.get('https://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha=01%2F05%2F2023&filtroEuro=1&filtroDolar=1')
# html = response.text
#
# # Una vez que tenemos el url, tenemos que inspeccionar el codigo fuente de la pagina para ver donde esta la cotizacion
# print(float(html.split('<td class="dest">')[1].split("<")[0].replace(",",".")))
#
# # // Vemos el url y notamos que podemos cambiar la fecha
# fecha = "08/12/2021"
# response = requests.get(f"https://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha={fecha}&filtroEuro=1&filtroDolar=1", verify=False)
# html = response.text
# print(float(html.split('<td class="dest">')[1].split("<")[0].replace(",",".")))


""" ----------------------------------------------------------------------------------------------- """

# *NO* LO VEMOS EN CLASE
# session = requests.session()
# session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})
# url = 'https://www.wsj.com/market-data/stocks?id={"application":"WSJ","marketsDiaryType":"overview"}&type=mdc_marketsdiary'
# response = session.get(url)
# output = json.loads(response.text)
# print(output)


""" ----------------------------------------------------------------------------------------------- """
# # // Veo requests POST con parametros.

# # // Diferencia entre POST y GET es que POST envia los parametros en el body del mensaje y GET en la URL
# # // Inspeccionando pagina buscar URL y PAYLOAD

# url = "https://www.origendirecto.com/ecommerce/api/getPrices"
# parametros = {"artCodes": ["022", "020", "255", "289", "307", "291", "018", "060", "146"]}
# response = requests.post(url, data=parametros, verify=False).text
# print(response)
# js = json.loads(response)
# print(js)


""" ----------------------------------------------------------------------------------------------- """
# # // Ahora vemos api que requieren autenticacion
# # https://remarkets.primary.ventures/index.html y ver la documentacion de la api
# # // Veremos el token de autenticacion
#
#
# server = "https://api.remarkets.primary.com.ar"
# # #server = "https://api.primary.com.ar"
# url = "/auth/getToken"
# username = "matiasrivera364"
# password = "ePMoRh7@"
#
# # // Cuando hacemos session.get la diferencia contra request.get es que session.get guarda la cookie de la sesion. Me emula realmente un navegador web
# session = requests.session()
#
# # we set the post method
# response = session.post(
#     server + url,
#     headers={
#         "X-Username": username,  # case sensitive
#         "X-Password": password},  # case sensitive
#     verify=False)
#
# token = response.headers.get("X-Auth-Token")  # Buscamos el token dentro de headers / _store
# if not token:
#     raise Exception("User or password incorrect")
#
# session.headers["X-Auth-Token"] = token  # Lo guardo en el header de la sesion para que lo use en cada request
#
# # // Vamos a buscar data historica de un futuro
# # // En la doc tenemos que buscar el endpoint que nos interesa. Leemos el endopoint, los parametros y el response
#
# url = '/rest/data/getTrades'
# market_id = "ROFX"
# symbol = "RFX20/JUN23"
# date_from = "2023-05-20"
# date_to = datetime.date.today().strftime("%Y-%m-%d")
#
# hist = f'{url}?marketId={market_id}&symbol={symbol}&dateFrom={date_from}&dateTo={date_to}'
#
# # response = session.get(server+hist, verify=False)
# # data = response.text
# # # // Vemos que el response es un json con una lista de trades
# #
# # // Vamos a trabajar con pandas
# # trades = json.loads(data)  # convierto el json a un diccionario
# # panda = pd.DataFrame(trades["trades"])  # convierto el diccionario a un dataframe
# #
# # # // Backup en un pickle para no tener que hacer el request cada vez que quiero trabajar
# # panda.to_pickle("trades")
#
# # // leo el pickle
# panda = pd.read_pickle("trades")
#
# # // Primero vamos a ver el volumen operado dia por dia
# panda["day"] = panda["datetime"].str.split(expand=True)[0]  # separo la fecha de la hora
# r = panda.groupby("day")["size"].sum()
#
# # // Segundo Vamos a ver el volumen operado por precio
# # panda["norm"] = (panda["price"]//1000)*1000  # normalizo el precio
# # r = panda.groupby("norm")["size"].sum()  # agrupo por precio y sumo el volumen
#
# # // Graficamos
# plt.rcParams.update({'font.size': 5})  # cambio el tamaño de la letra
# r.plot.bar()  # vertical
# # r.plot.barh()  # horizontal
# plt.show()


""" ----------------------------------------------------------------------------------------------- """

# # // Vamos a ver data del gobierno desde https://www.datos.gob.ar/dataset
# # Lo importante es saber que hay mucha data publica y que se puede acceder a ella de forma programatica
# panda = pd.read_csv('http://datos.energia.gob.ar/dataset/1c181390-5045-475e-94dc-410429be4b17/resource/80ac25de-a44a-4445-9215-090cf55cfda5/download/precios-en-surtidor-resolucin-3142016.csv')
# print(panda)

""" ----------------------------------------------------------------------------------------------- """


# # // Vamos a ver la cotizacion oficial del dolar historicamente
# response = requests.get("https://apis.datos.gob.ar/series/api/series/?ids=168.1_T_CAMBIOR_D_0_0_26&limit=5000&format=json")
# data = json.loads(response.text)  # convierto el json a un diccionario
#
# panda = pd.DataFrame(data["data"])  # convierto el diccionario a un dataframe
# panda.rename(columns={0: "fecha", 1: "usd"}, inplace=True)  # renombro las columnas, OJO con el inplace
# panda.set_index("fecha", inplace=True)  # seteo el indice. Ver previo cual era el indice antes
#
# panda.plot()
# print(panda)
# plt.show()


""" ----------------------------------------------------------------------------------------------- """
# // Vamos a ver la cotizacion ccl del dolar historicamente desde https://www.ambito.com/
desde = "2023-01-01"
hasta = datetime.date.today().strftime("%Y-%m-%d")
data2 = requests.get(f"https://mercados.ambito.com//dolarrava/cl/historico-general/{desde}/{hasta}").text
data = json.loads(data2)

data = pd.DataFrame(data[1:], columns=data[0])  # tomo la primera fila como header
data.set_index("Fecha", inplace=True)

data["dolar"] = data["Referencia"].apply(lambda x: float(x.replace(",", ".")))  # reemplazo las comas por puntos y convierto a float
data.index = pd.to_datetime(data.index, format="%d/%m/%Y")  # convierto el indice a datetime

print(data)
data["dolar"].plot()  # grafico solo el dolar
plt.show()
