import requests
import json
import pandas as pd
import matplotlib.pyplot as plt


# // Cotizacion oficial idem anterior
response = requests.get("https://apis.datos.gob.ar/series/api/series/?ids=168.1_T_CAMBIOR_D_0_0_26&limit=5000&format=json")
data = json.loads(response.text)

df_oficial = pd.DataFrame(data["data"])
df_oficial.rename(columns={0: "Fecha", 1: "usd"},inplace=True)
df_oficial.set_index("Fecha", inplace=True)
df_oficial.index = pd.to_datetime(df_oficial.index)  # convierto el indice a datetime

print(df_oficial)
print(df_oficial.info())


# // Cotizacion ccl idem anterior
data2 = requests.get("https://mercados.ambito.com//dolarrava/cl/historico-general/21-07-2021/31-03-2023").text
data = json.loads(data2)

df_ccl = pd.DataFrame(data[1:], columns=data[0])
df_ccl.set_index("Fecha",inplace=True)
df_ccl.index = pd.to_datetime(df_ccl.index, format="%d/%m/%Y")  # convierto el indice a datetime
df_ccl["Referencia"] = df_ccl.Referencia.apply(lambda x: float(x.replace(",", ".")))  # reemplazo , por . y convierto a float

df_ccl.rename(columns={"Referencia": "ccl"}, inplace=True)  # renombro la columna Referencia a ccl

print(df_ccl)
print(df_ccl.info())


# // Junto el oficial con el ccl. Necesito que el indice sea el mismo para poder hacer el merge
df_merge = pd.merge(df_oficial, df_ccl, left_index=True, right_index=True)  # merge por indice, uso left_index y right_index
print(df_merge)
df_merge.plot()
plt.savefig("ccl.png")  # guardo el grafico
plt.show()
