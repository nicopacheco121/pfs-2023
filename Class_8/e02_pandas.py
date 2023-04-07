# import requests
# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# response = requests.get("https://apis.datos.gob.ar/series/api/series/?ids=168.1_T_CAMBIOR_D_0_0_26&limit=5000&format=json")
# data = json.loads(response.text)
# panda = pd.DataFrame(data["data"])
# panda.rename(columns={0:"Fecha",1:"usd"},inplace=True)
# panda.set_index("Fecha",inplace=True)
# panda.plot()
# print(panda)
# plt.show()
#
# data2 = requests.get("https://mercados.ambito.com//dolarrava/cl/historico-general/21-07-2021/21-11-2021").text
# data = json.loads(data2)
# data = pd.DataFrame(reversed(data[1:]),columns=data[0])
# data["Referencia"] = data.Referencia.apply(lambda x:float(x.replace(",",".")))
# print(data)
# data["Fecha"] = data.Fecha.apply(lambda x:f'{x.split("-")[2]}-{x.split("-")[1]}-{x.split("-")[0]}')
# data.set_index("Fecha",inplace=True)
# data.plot()
# plt.show()
#
# b = pd.merge(panda,data,left_index=True,right_index=True)
# b.plot()
# plt.show()
#
# import pandas as pd
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context
#
# result = pd.read_html("https://www.rofex.com.ar/cem/FyO.aspx",attrs={'id':'ctl00_ContentPlaceHolder1_gvFyO'},encoding='utf-8',header=0)
# print(result)
# print(result[0].describe())
# print(result[0].isnull())
# print(result[0][(result[0]['Tipo'] == 'Futuro')])

# import requests
# import pandas as pd
# import json
# key = ""
# url = "https://api.estadisticasbcra.com/usd"
# headers = {"Authorization": "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDk2MjUyMjAsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJtYXRpYXMucml2ZXJhQGdtYWlsLmNvbSJ9.ORX_d7HtLSAtnPbIuby41UuSP2E9KO8GUPhUltjuNnSQhLyw-jJyxYI9m2XxfSJ8xqpcSC2SzA1s3S3gRXinjA"}
# resposne = requests.get(url,headers=headers).text
# #print(resposne)
# df = pd.DataFrame(json.loads(resposne))
# print(df[df['d'] == '2021-08-20'])
#


import pandas as pd
import os.path as path
import os

print(path.abspath(path.curdir))
#p = pd.read_excel("../../Documents/matias/Tipo Comitentes.xlsx",sheet_name="Hoja1")
#print(p)

p2 = pd.read_excel("../../../Documents/matias/Base Fondos final 31.07.2021.xlsx",sheet_name="Base",header=[2,3])
p2.info()
print(p2[[("Comitente","Número"),("Fondo","Descripción"),("Cantidad","Cantidad")]])
data = p2.groupby([("Comitente","Número"),("Fondo","Descripción")])[[("Cantidad","Cantidad")]].sum()
print(data[(data[("Cantidad","Cantidad")]!=0)])
