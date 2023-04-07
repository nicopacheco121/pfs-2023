import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

plt.rcParams.update({'figure.autolayout': True})
print(plt.style.available)
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(12, 10))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

formatter = FuncFormatter(currency)
# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Now we'll move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])


plt.show()


# Librerías
import pandas as pd, numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

#Seteo de propiedades del gráfico
plt.rcParams['figure.figsize'] = [10,6]
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["font.size"] = 15
plt.rcParams["axes.labelweight"] = "bold"

#Importación de datos
tickers = ["AGG", "GLD", "QQQ", "SHY", "SPY", "TLT"]
start= dt.date.today()-dt.timedelta(days=10)
end= dt.date.today()
cartera = yf.download(tickers, start, end)["Adj Close"]
cartera.dropna(inplace=True)

# Creo DataFrame con variaciones diarias de cada ETF
yields = cartera.pct_change()

# Correlaciones
sns.heatmap(yields.corr(), cmap='coolwarm',
            annot=True, linewidths=.5)

plt.show()
# Definición de años y tasa libre de riesgo
años = (cartera.index[-1] - cartera.index[0]).days/365
print(f'los años de análisis son {round(años,1)} y van desde {cartera.index[0]} hasta {cartera.index[-1]}')
risk_free = 0.0214

# Bucle para calcular métricas de rendimiento y graficar
for ticker in tickers:
    yields2 = yields.copy()
    yields2["acum_ret"] = (1+yields2[ticker]).cumprod()-1
    print("\n"+ticker)
    print("retorno total ", round(yields2["acum_ret"][-1]*100,2), "%")
    retorno = ((1+yields2["acum_ret"][-1])**(1/años))-1
    print(f"Rerono anual (CAGR) {round(retorno*100,2)} %")

    volatilidad = yields2[ticker].std() * np.sqrt(252)
    print(f"Volatilidad anual {round(volatilidad*100,2)} %")

    sharpe = (retorno-risk_free)/volatilidad
    print(f'Sharpe ratio {round(sharpe,2)}')

    cartera2 = cartera.copy()
    cartera2["maximo"] = cartera2[ticker].cummax()
    cartera2["perdida"] = (cartera2[ticker] / cartera2["maximo"]) -1
    max_dd = cartera2["perdida"].min()
    print(f'Pérdida máxima {round(max_dd*100,2)} %')

    fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, figsize=(12,8))
    ax1.set(title=ticker)
    #print()
    ax1.plot(cartera2[ticker], c="k")
    ax1.grid(True)

    ax2.set(title="Bajas desde máximos")
    ax2.plot(cartera2["perdida"], c="k")
    ax2.fill_between(cartera2.index, cartera2["perdida"], 0,
                     color="k")
    fig.show()
    fig.savefig(f"{ticker}.pdf")