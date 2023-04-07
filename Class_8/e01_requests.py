# import bs4
# import requests
# import pandas as pd
# #response = requests.get("http://datacenter.matba.com.ar/ajustesdc.aspx",verify=False)
# #soup = bs4.BeautifulSoup(html,features="lxml")
# panda = pd.read_html("http://datacenter.matba.com.ar/ajustesdc.aspx",attrs={"id":"ctl00_Cuerpo_ASPxPageControl1_ASPxCallbackPanel1_ASPxGridView1_DXMainTable"},header=0,decimal=',',thousands='.',encoding="utf-8")[0]
# panda.info()
# print(panda[["Posición","Cierre"]])
#
# import pandas as pd
# import requests
# import matplotlib.pyplot as plt
# url="https://www.rofex.com.ar/cem/TickByTick.aspx"
# html = requests.get(url,verify=False).text
# panda = pd.read_html(html,attrs={'id':'ctl00_ContentPlaceHolder1_gvFuturos'},header=0,decimal=',',thousands='.')[0]
# panda["precio_normalizado"] = panda["Precio"]
# print(panda.groupby("Posición").agg({"Volumen":["sum","count"],"Precio":"mean"}))
# result = panda.groupby(["Posición","precio_normalizado"]).Volumen.sum()
# #result = panda.groupby("Posición").Volumen.sum()
# print(result.loc["RFX20122021"])
# result.loc["RFX20122021"].plot.barh()
# #result.plot.bar()
#
# plt.show()
# #panda.to_excel("out.xlsx",index=False)

# import requests
# fecha = "08/12/2021"
# response = requests.get(f"https://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha={fecha}&filtroEuro=1&filtroDolar=1",verify=False)
# html = response.text
# print(float(html.split('<td class="dest">')[1].split("<")[0].replace(",",".")))

import requests
import json
session = requests.session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})

# url = 'https://www.wsj.com/market-data/stocks?id={"application":"WSJ","marketsDiaryType":"overview"}&type=mdc_marketsdiary'
# response = session.get(url)
# output = json.loads(response.text)
# print(output)
#
#
# import requests
# import json
#
# url = "https://www.origendirecto.com/ecommerce/api/getPrices"
# items = "https://www.origendirecto.com/ecommerce/api/getItems"
# parametros = {"artCodes": ["022", "020", "255", "289", "307", "291", "018", "060", "146"]}
# #json = json.dumps(parametros)
# #items_result = requests.get(items,verify=False).text
# #item_result = json.loads(items_result)
# #item_result
# response = requests.post(url,data=parametros,verify=False).text
# print(response)
#
#


# import requests
# import datetime
# import pandas as pd
#
#
# server = "https://api.remarkets.primary.com.ar"
# # #server = "https://api.primary.com.ar"
# url= "/auth/getToken"
# username = "matiasrivera364"
# password = "ePMoRh7@"
# session = requests.session()
# #
# # #we set the post method
# response = session.post(server+url, headers={"X-Username":username,"X-Password":password},verify=False)
# token = response.headers.get("X-Auth-Token")
# if (not token):
#      raise Exception("User or password incorrect")
#
# session.headers["X-Auth-Token"] = token
# hist = "/rest/data/getTrades?marketId=ROFX&symbol=RFX20Dic21&dateFrom=2021-10-01&dateTo={today}".format(today=datetime.date.today().strftime("%Y-%m-%d"))
#
# response = session.get(server+hist,verify=False)
# data = response.text
# #print(data)
# import json
# import matplotlib.pyplot as plt
# trades = json.loads(data)
# panda = pd.DataFrame(trades["trades"])
# panda["day"] =panda["datetime"].str.split(expand=True)[0]
# panda["norm"] = (panda["price"]//1000)*1000
# r = panda.groupby("norm")["size"].sum()
# plt.rcParams.update({'font.size': 5})
# #r.plot.barh()
# #r = panda.groupby("day")["size"].sum()
# #r.plot.bar()
# r.plot.barh()
# plt.show()
# #print(type(trades))
# #print(type(trades["trades"]))

# import pandas as pd
#
# panda = pd.read_csv("https://infra.datos.gob.ar/catalog/sspm/dataset/336/distribution/336.1/download/activos-externos-componentes-datos-historicos.csv")
# panda
import pandas as pd

response = requests.get("https://www.mav-sa.com.ar",verify=False)
data = pd.read_html(response.text,attrs={'class':'tablecirculares'})
print(data)

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
response = requests.get("https://apis.datos.gob.ar/series/api/series/?ids=168.1_T_CAMBIOR_D_0_0_26&limit=5000&format=json")
data = json.loads(response.text)
panda = pd.DataFrame(data["data"])
panda.rename(columns={0:"fecha",1:"usd"},inplace=True)
panda.set_index("fecha",inplace=True)
panda.plot()
print(panda)
plt.show()

data2 = requests.get("https://mercados.ambito.com//dolarrava/cl/historico-general/21-07-2021/21-08-2021").text
data = json.loads(data2)
data = pd.DataFrame(data[1:],columns=data[0])
data.set_index("Fecha",inplace=True)
data["dolar"]=data["Referencia"].apply(lambda x:float(x.replace(",",".")))
print(data)
data["dolar"].plot()
plt.show()
