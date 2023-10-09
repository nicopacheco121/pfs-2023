import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import datetime
# from io import StringIO

"""
Algunos comentarios previos:

// libreria requests tiene los metodos dentro de la libreria
// OJO Los mensajes en http viajan en forma de texto, cualquiera los puede leer
// http vs httpS = https encripta la informacion
// cuando nosotros escribimos una direccion en el navegador y damos a enter, estamos haciendo un request GET
"""


""" ----------------------------------------------------------------------------------------------- """
"""
Vamos a leer la misma tabla de la semana pasada pero esta vez con PANDAS.
Ya no vamos a tener que buscar los tr, td y th, etc. Pandas lo hace por nosotros, no utilizaremos bs4
"""
# response = requests.get("http://datacenter.matba.com.ar/ajustesdc.aspx", verify=False)  # metodo GET
# # // en verify=False le estamos diciendo que no es necesario que verifique el certificado de seguridad
#
# # Debug y ver objeto responde, tipo status code, url y text
#
# panda = pd.read_html(
#     # StringIO(response.text),
#     response.text,
#     # "http://datacenter.matba.com.ar/ajustesdc.aspx",  # tambien se puede poner directamente el url
#     attrs={"id": "ctl00_Cuerpo_ASPxPageControl1_ASPxCallbackPanel1_ASPxGridView1_DXMainTable"},  # buscar en la pagina la tabla
#     header=0,  # le decimos que la primer fila es el header
#     decimal=',',  # el separador de decimales es la coma
#     thousands='.',  # el separador de miles es el punto
#     encoding="utf-8")[0]
# # // La semana pasada con bs4 teniamos que poner a mano el header, separar miles, etc.
# # // Pandas me deja colocar la configuracion de la tabla a leer
# # // La parte artesanal de este trabajo va en identificar los hedaers, decimales, etc.
#
# panda.info()
# print(panda[["Posición", "Cierre"]])

""" ----------------------------------------------------------------------------------------------- """
"""
A partir de datos tick by tick vamos a generar el perfil de volumen
"""

# url = "https://www.rofex.com.ar/cem/TickByTick.aspx"
#
# html = requests.get(url, verify=False).text  # ya directamente traigo el html con el .text
#
# panda = pd.read_html(
#     html,
#     attrs={'id': 'ctl00_ContentPlaceHolder1_gvFuturos'},
#     header=0,
#     decimal=',',
#     thousands='.')[0]
#
# # // Vemos la sumatoria de contratos, cantidad de operaciones y precio promedio por POSICION
# print(panda.groupby("Posición").agg({"Volumen": ["sum", "count"], "Precio": "mean"}))
#
# # // Vamos a generar nuevamente el perfil de volumen (lo hicimos la semana pasada)
# # Primero normalizamos el precio
# panda["precio_normalizado"] = (panda["Precio"] // 10) * 10  # usamos // para que no tome decimales y * 10 para que tome decenas
#
# # Agrupamos posicion y precio normalizado y sumamos el volumen
# result = panda.groupby(["Posición", "precio_normalizado"]).Volumen.sum()
# print(result.loc["DLR022024"])
#
# result.loc["DLR022024"].plot.barh()  # graficamos barras horizontales
# plt.show()  # mostramos el grafico


""" ----------------------------------------------------------------------------------------------- """
"""
Trabajamos con la cotizacion del dolar desde la pagina del bna
Intentaremos obtener la fecha del dolar oficial para una fecha determinada
"""
#
# # Vemos la pagina del bna
# # https://www.bna.com.ar
# # Si hacemos boton derecho e inspeccionar, hay un tag que se llama network.
# # Actualizamos la pagina y vemos lo que se carga en network
# # Tocamos el boton de cotizaciones, seccion ver historico, ponemos una fecha, y previo a dar ok, borramos con clear
# # Damos ok, y vemos que se carga un nuevo elemento en network, este elemento comienza con HistoricoPrincipales
# # Si apretamos sobre esto, nos aparecen distintos elementos, entre ellos un headers y dentro de este, un request url
#
#
# # El url que aparece en request url es el que vamos a usar para hacer el request
# response = requests.get('https://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha=01%2F05%2F2023&filtroEuro=1&filtroDolar=1')
#
# html = response.text
#
# # Una vez que tenemos el url, tenemos que inspeccionar el codigo fuente de la pagina para ver donde esta la cotizacion
# # El html es un TEXT, por lo que podemos usar los metodos de string para buscar la cotizacion
# # Notamos que la cotizacion esta dentro de un tag <td class="dest">, por lo que podemos buscarlo
# print(float(html.split('<td class="dest">')[1].split("<")[0].replace(",", ".")))
#
# # // Vemos el url y notamos que podemos cambiar la fecha
# fecha = "08/12/2021"
# # Ejecutamos el mismo codigo anterior pero con la fecha cambiada
# response = requests.get(f"https://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha={fecha}&filtroEuro=1&filtroDolar=1", verify=False)
# html = response.text
# print(float(html.split('<td class="dest">')[1].split("<")[0].replace(",", ".")))


""" ----------------------------------------------------------------------------------------------- """

# # *NO* LO VEMOS EN CLASE
# session = requests.session()
# session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})
# url = 'https://www.wsj.com/market-data/stocks?id={"application":"WSJ","marketsDiaryType":"overview"}&type=mdc_marketsdiary'
# response = session.get(url)
# output = json.loads(response.text)
# print(output)


""" ----------------------------------------------------------------------------------------------- """
"""
Intentaremos traer los precios y productos de la pagina de origen directo

https://www.origendirecto.com/

Trabajamos con metodo POST
"""

# # Vamos a la pagina
# # Seleccionamos una categoria
# # Inspeccionamos, vamos a network, actualizar y notaremos que se carga un elemento nuevo llamado getPrices
# # Notamos que en headers, esta vez vemos que el metodo es POST
#
# # // Diferencia entre POST y GET es que POST envia los parametros en el body del mensaje y GET en la URL
#
# # Notamos que en payload, hay un json con los parametros que envia
#
# url = "https://www.origendirecto.com/ecommerce/api/getPrices"
# parametros = {"artCodes": ["022", "020", "255", "289", "307", "291", "018", "060", "146"]}
# response = requests.post(url,
#                          data=parametros,  # parametros que enviamos
#                          verify=False).text
# print(response)
# js = json.loads(response)  # convierto el json a un diccionario
# print(js)


""" ----------------------------------------------------------------------------------------------- """
"""
Estuvimos trabajando con api publicas, ahora vamos a ver una api privada que requiere autenticacion

https://remarkets.primary.ventures/index.html
Entramos a la doc y vemos en el indique que hay una seccion llamada "ConectándosealaAPIportokendeautenticación"

"""
#
# server = "https://api.remarkets.primary.com.ar"
# # server = "https://api.primary.com.ar"
# url = "/auth/getToken"
# username = "matiasrivera364"
# password = "ePMoRh7@"
#
# # // Cuando hacemos session.get la diferencia contra request.get es que session.get guarda la cookie de la sesion. Me emula realmente un navegador web
# session = requests.session()
#
# # seteo el header de la sesion
# response = session.post(
#     server + url,
#     headers={
#         "X-Username": username,  # case sensitive
#         "X-Password": password},  # case sensitive
#     verify=False)
#
#
# token = response.headers.get("X-Auth-Token")  # Buscamos el token dentro de headers / _store
# if not token:
#     raise Exception("User or password incorrect")
#
# print(token)
#
# session.headers["X-Auth-Token"] = token  # Lo guardo en el header de la sesion para que lo use en cada request
#
# # // Vamos a buscar data historica de un futuro
# # // En la doc tenemos que buscar el endpoint que nos interesa. Leemos el endopoint, los parametros y el response
#
# url = '/rest/data/getTrades'
# market_id = "ROFX"
# symbol = "RFX20/JUN23"
# date_from = "2023-06-10"
# date_to = datetime.date.today().strftime("%Y-%m-%d")
#
# # Como el metodo es GET, los parametros van en la URL
# hist = f'{url}?marketId={market_id}&symbol={symbol}&dateFrom={date_from}&dateTo={date_to}'
#
# # response = session.get(server+hist, verify=False)
# # data = response.text
# # # // Vemos que el response es un json con una lista de trades
# #
# # # // Vamos a trabajar con pandas
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
# # # // Segundo Vamos a ver el volumen operado por precio
# # panda["norm"] = (panda["price"]//10000)*10000  # normalizo el precio
# # r = panda.groupby("norm")["size"].sum()  # agrupo por precio y sumo el volumen
#
# # // Graficamos
# plt.rcParams.update({'font.size': 5})  # cambio el tamaño de la letra
# r.plot.bar()  # vertical
# # r.plot.barh()  # horizontal
# plt.show()


""" ----------------------------------------------------------------------------------------------- """
"""
Podemos ver informacion publuca del gobierno
"""

# # // Vamos a ver data del gobierno desde https://www.datos.gob.ar/dataset
# # Lo importante es saber que hay mucha data publica y que se puede acceder a ella de forma programatica
# panda = pd.read_csv('http://datos.energia.gob.ar/dataset/1c181390-5045-475e-94dc-410429be4b17/resource/80ac25de-a44a-4445-9215-090cf55cfda5/download/precios-en-surtidor-resolucin-3142016.csv')
# print(panda)

""" ----------------------------------------------------------------------------------------------- """
"""
Graficaremos el dolar oficial y el CCL historico
"""

# # En la web https://apis.datos.gob.ar, en series, podemos buscar la data del dolar oficial desde el 2014
# # // Vamos a ver la cotizacion oficial del dolar historicamente
# response = requests.get("https://apis.datos.gob.ar/series/api/series/?ids=168.1_T_CAMBIOR_D_0_0_26&limit=5000&format=json")
# data = json.loads(response.text)  # convierto el json a un diccionario
#
# df_oficial = pd.DataFrame(data["data"])  # convierto el diccionario a un dataframe
# df_oficial.rename(columns={0: "fecha", 1: "usd"}, inplace=True)  # renombro las columnas, OJO con el inplace
# df_oficial.set_index("fecha", inplace=True)  # seteo el indice. Ver previo cual era el indice antes
#
# df_oficial.plot()
# print(df_oficial)
# plt.show()


""" ----------------------------------------------------------------------------------------------- """
# # // Vamos a ver la cotizacion ccl del dolar historicamente desde https://www.ambito.com/
# desde = "2023-01-01"
# hasta = datetime.date.today().strftime("%Y-%m-%d")
# data2 = requests.get(f"https://mercados.ambito.com//dolarrava/cl/historico-general/{desde}/{hasta}").text
# data = json.loads(data2)
#
# df_ccl = pd.DataFrame(data[1:], columns=data[0])  # tomo la primera fila como header
# df_ccl.set_index("Fecha", inplace=True)
#
# print(df_ccl)
#
# # reemplazo las comas por puntos y convierto a float
# df_ccl["dolar"] = df_ccl["Referencia"].apply(lambda x: float(x.replace(",", ".")))  # con apply aplico una funcion a cada elemento de la columna
# df_ccl.index = pd.to_datetime(df_ccl.index, format="%d/%m/%Y")  # convierto el indice a datetime
#
# print(df_ccl.info())
#
# print(df_ccl)
# df_ccl["dolar"].plot()  # grafico solo el dolar
# plt.show()
