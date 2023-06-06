import pandas as pd
import numpy as np


def signals(data, ema_fast, ema_slow, rsi):
    """
    Estrategia:
    LONG:
    - EMA rapida > EMA lenta
    - RSI < 50

    SHORT:
    - EMA rapida < EMA lenta
    - RSI > 50

    :param data: dataframe con precios
    :param ema_fast: columna con la ema rapida
    :param ema_slow: columna con la ema lenta
    :param rsi: columna con el rsi

    :return: serie con señal LONG o SHORT
    """

    df = data.copy()  # hago una copia para no modificar el original
    df['signal'] = None  # creo una columna vacia
    # print(df.info())  # vemos que signal es toda NaN

    # long
    df.loc[(df[ema_fast] > df[ema_slow]) & (df[rsi] < 50), 'signal'] = 'long'  # filtro con loc y asigno a signal

    # short
    df.loc[(df[ema_fast] < df[ema_slow]) & (df[rsi] > 50), 'signal'] = 'short'

    # print(df['signal'].value_counts())  # vemos cuantos long y short hay

    # fill None values con los valores hacia adelante
    df['signal'] = df['signal'].ffill()

    df.dropna(inplace=True)  # borro los NaN

    # df.to_excel('signals.xlsx')  # podemos ver el excel para ver como van quedando las señales

    return df['signal']


def operations(df, signal='signal', long='long', short='short'):
    """
    Genero las operaciones, basicamente tiene tiene que comenzar con un long o short y terminar con uno distinto.
    Cuando termina, se abre una nueva posicion.

    return un dataframe con las operaciones
    """

    df['operacion'] = np.where(
        (df[signal] == long) & (df[signal].shift() == short),
        long,
        np.where(
            (df[signal] == short) & (df[signal].shift() == long),
            short,
            ''))

    filtro_operaciones = df.loc[df['operacion'] != '']

    return filtro_operaciones
