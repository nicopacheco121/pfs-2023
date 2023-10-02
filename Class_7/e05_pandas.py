'''documentacion https://pandas.pydata.org/docs/reference/frame.html'''
import pandas
import pandas as pd

"""
Con pandas es una libreria creada para el analisis de datos

En lo relativo a los archivos podremos:
    - Leer bases de datos
    - Leer archivos de excel
    - Leer archivos de google sheets
    - Scraping de tablas de paginas web
    
    - Crear bases de datos
    - Crear archivos de excel
    - Crear archivos de google sheets
    
    - entre otros
    
Pandas tiene 2 estructuras de datos:
    - Series (es una columna uni-dimensional)
    - DataFrames  (es una tabla bi-dimensional con filas y columnas) Podemos tener tambien multi index y multi columnas
"""

# # pandas show more rows
# pd.set_option('display.max_rows', 100)

# GENERAMOS Y MANIPULAMOS PANDAS
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)  # creo un dataframe a partir de un diccionario. El index lo genera automaticamente
print(purchases)

# Genero un dataframe a partir de un diccionario y le agrego el index
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)

# Acceder a la informacion
# Con .loc accedemos a la informacion por el nombre del index y el nombre de la columna

print(purchases.loc['June', 'apples'])  # accedo a la informacion de la fila June y la columna apples
# Dentro de los corchetes primero va el nombre del index y luego el nombre de la columna
# Estos indices y columnas pueden ser rangos tambien
print(purchases.loc['June':, 'apples'])

# Con .iloc accedemos a la informacion por el numero de fila y el numero de columna
print(purchases.iloc[0, 0])

# Podemos acceder a una columna / columnas en particular
print(purchases["apples"])
print(purchases.apples)

# LEEMOS ARCHIVOS
path = "../Exams/dodic_order_book.csv"  # con los .. subo un nivel en la carpeta
ordenes = pd.read_csv(path, index_col=0)  # index_col=0 le digo que la primer columna es el index
print(ordenes)

'''
.head() outputs the first five rows of your DataFrame by default, but we could also pass a number as well: movies_df.head(10) would output the top ten rows, for example.

To see the last five rows use .tail(). tail() also accepts a number, and in this case we printing the bottom two rows.:'''

# INFORMACION Y MANIPULACION DE DATAFRAMES
print(ordenes.head())  # imprimo las primeras 5 filas, le puedo pasar un numero como parametro
print(ordenes.tail())  # imprimo las ultimas 5 filas, le puedo pasar un numero como parametro
print(ordenes.info())  # imprimo informacion del df

print(ordenes.shape)  # cantidad de registros y columnas

print(ordenes.columns)  # imprimo las columnas

print(ordenes.isnull())  # me devuelve un df con True si es null y False si no lo es

# Cambio el nombre de las columnas
newordenes = ordenes.rename(columns={'server_ts': "timestamp"})  # genero un nuevo df, no modifico el original
print(newordenes.columns)
print(ordenes.columns)

# Si quiero modificar el df original
ordenes.rename(columns={'server_ts': "timestamp"}, inplace=True)  # modifico el df original
print(ordenes.columns)




'''
How to work with missing values
When exploring data, you’ll most likely encounter missing or null values, which are essentially placeholders for non-existent values. Most commonly you'll see Python's None or NumPy's np.nan, each of which are handled differently in some situations.

There are two options in dealing with nulls:

Get rid of rows or columns with nulls
Replace nulls with non-null values, a technique known as imputation
Let's calculate to total number of nulls in each column of our dataset. The first step is to check which cells in our DataFrame are null:
'''

# Operaciones entre columnas

print(ordenes['size']*ordenes['price'])  # multiplico las columnas size y price
ordenes['nocional'] = ordenes['size'] * ordenes['price']  # creo una nueva columna con el resultado de la operacion
ordenes["letras"] = ordenes['symbol'].str.slice(0, 3)  # creo una nueva columna con las primeras 3 letras del symbol
print(ordenes)
print(ordenes['price'].std())  # desviacion estandar de la columna price

print(ordenes[['price', 'size']].describe())  # describe me da un resumen de la columna
# * Para trabajar con 2 columnas o mas tengo que pasarle una lista de columnas

# Filtro
print(ordenes[(ordenes['account'] == 1225) | (ordenes['account'] == 1001)])  # filtro por 2 cuentas con el operador or |

print(ordenes[(ordenes['account'].isin([1225, 1001]))])  # filtro por 2 cuentas con el metodo isin

# Manipulo datos con funciones de agregacion
print(ordenes.groupby('account').count())  # agrupo por cuenta y cuento la cantidad de registros por cuenta
print(ordenes.groupby('account')["price"].sum())  # agrupo por cuenta y sumo la columna price
print(ordenes.price.value_counts())  # cuento la cantidad de veces que se repite cada valor de la columna price

print(ordenes.account.value_counts())  # cuento la cantidad de veces que se repite cada valor de la columna account

print(ordenes.groupby("account").price.sum())  # agrupo por cuenta y sumo la columna price
print(ordenes.groupby("account").price.max())  # agrupo por cuenta y me quedo con el maximo de la columna price


# GRAFICOS CON MATPLOTLIB
import matplotlib.pyplot as plt
ordenes.price[(ordenes['price'] >= 18)].plot()
plt.show()


# TRAEMOS DATA CON YFINANCE
import yfinance

from datetime import date
from datetime import timedelta
day = date.today()-timedelta(days=100)  # le resto 100 dias a la fecha de hoy
ggal = yfinance.download(["GGAL"],start=day)  # obtengo los datos de ggal desde la fecha que le pase hasta hoy
# ggal = yfinance.download(["GGAL","YPF"],start=day)

ggal["Close"].plot()  # grafico la columna close
plt.show()  # muestro el grafico

ggal.to_excel("ggal.xlsx")  # guardo el df en un excel

