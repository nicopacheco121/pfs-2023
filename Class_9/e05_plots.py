import matplotlib.pyplot as plt
import pandas as pd

# plot close, ema and rsi
def plot_indicators(df, close, ema_fast, ema_slow, rsi):

    # use black background
    # plt.style.use('dark_background')

    fig, ax = plt.subplots(2, 1, figsize=(16, 9))  # 2 rows, 1 column (2 charts)

    ax[0].plot(df[close], label='Close')
    ax[0].plot(df[ema_fast], label='EMA Fast')
    ax[0].plot(df[ema_slow], label='EMA Slow')
    ax[0].legend()

    ax[1].plot(df[rsi], label='RSI')
    ax[1].axhline(30, color='red', linestyle='--')
    ax[1].axhline(70, color='red', linestyle='--')
    ax[1].legend()

    plt.show()


def plot_trades(data, close='c', operacion='operacion'):

    # use black background
    # plt.style.use('dark_background')

    df = data.copy()

    print(df)

    # En el dataframe teniamos las operaciones en columnas, ahora vamos a filtrar para obtener el precio y la fecha de inicio de cada operacion
    df['longs'] = (df[close] * 0.90).loc[df[operacion] == 'long']
    df['shorts'] = (df[close] * 1.10).loc[df[operacion] == 'short']

    # tamaño del grafico
    plt.figure(figsize=(20, 6))

    # grafico de precio
    plt.plot(data[close], color='black')

    # grafico de operaciones
    plt.plot(df.index, df.longs, '^', markersize=10, c='green')
    plt.plot(df.index, df.shorts, 'v', markersize=10, c='red')

    # grid
    plt.grid(which='major', axis='y', color='black', lw=1, alpha=0.15)

    # titulo
    plt.suptitle('Estrategia Cruce Medias', y=0.92)

    # guardar grafico
    plt.savefig('grafico_estrategia')

    plt.show()


