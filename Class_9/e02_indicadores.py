import pandas as pd
import numpy as np


def add_ema(df, column, k):
    """
    Calcula la media movil exponencial de un dataframe de precios con span = k

    :param df: dataframe con precios
    :param column: columna de precios
    :param k: periodo

    :return: serie de la media movil exponencial
    """
    if k == 0 or k == 1:
        return df[column]
    else:
        return df[column].ewm(span=k, adjust=False).mean()  # ewm = calculos ponderados exponencialmente


def add_rma(df, column, k):
    """
    Calcula la media movil exponencial de un dataframe de precios con alpha = 1/k

    :param df: dataframe con precios
    :param column: columna de precios
    :param k: periodo

    :return: serie de la media movil exponencial
    """
    if k == 0 or k == 1:
        return df[column]
    else:
        return df[column].ewm(alpha=1 / k, min_periods=k, adjust=False).mean()  # ewm = calculos ponderados exponencialmente


def add_rsi(data, column, k):

    """
    Calcula el RSI de un dataframe de precios

    # formula
    # RSI = 100 - 100 / (1 + RS)
    # RS = media movil de las subidas / media movil de las bajadas

    :param data: dataframe con precios
    :param column: columna de precios
    :param k: periodo

    :return: serie con el RSI
    """

    df = data.copy()  # hago una copia para no modificar el original

    df['delta'] = df[column].diff()  # calculo la diferencia entre el valor actual y el anterior

    df['up'] = np.where(df['delta'] > 0, df['delta'], 0)  # si delta es mayor a 0, delta, sino 0
    df['down'] = np.where(df['delta'] < 0, abs(df['delta']), 0)  # si delta es menor a 0, delta, sino 0

    df['roll_up'] = add_rma(df, 'up', k)  # calculo la media movil exponencial de up
    df['roll_down'] = add_rma(df, 'down', k)

    df['rs'] = df['roll_up'] / df['roll_down']
    df['rsi'] = 100.0 - (100.0 / (1.0 + df['rs']))

    return df['rsi']





