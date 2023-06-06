from e01_data import download_data
import e02_indicadores as indicadores
from e03_operaciones import signals, operations
from e04_trades import make_trades, make_results
import e05_plots as plots

import config
import pandas as pd


def run(symbol, timeframe=config.TIMEFRAME, descargar_data=True):

    # - - - DESCARGA DE DATOS - - -
    # (Ver solo el get_data_binance)
    if descargar_data:
        data, bad_request = download_data(symbol, timeframe, '2020-01-01', '2023-06-03', api='PERPETUOS')
        print('bad_request: ', bad_request)

        # Procesamos los datos a float y datetime
        data = data.astype(float)
        data.index = pd.to_datetime(data.index, unit='ms')
        print(data)

        data.to_pickle(f'data_{symbol}')  # Guardamos los datos en un archivo pickle

    else:
        data = pd.read_pickle(f'data_{symbol}')

    # - - - CALCULO DE INDICADORES - - -
    # (Ver el calculo de indicadores)
    data['ema_slow'] = indicadores.add_ema(data, 'c', config.EMA_SLOW)
    data['ema_fast'] = indicadores.add_ema(data, 'c', config.EMA_FAST)
    data['rsi'] = indicadores.add_rsi(data, 'c', 14)
    # Borro columnas que no voy a usar
    data.drop(['o', 'h', 'l', 'v', 'v_q', 'n'], axis=1, inplace=True)
    data.dropna(inplace=True)

    # Plot de indicadores
    # (ver la funcion)
    # plots.plot_indicators(data.iloc[-1000:], 'c', 'ema_slow', 'ema_fast', 'rsi')

    # - - - SEÑALES - - -
    data['signal'] = signals(data, 'ema_slow', 'ema_fast', 'rsi')
    # print(data.info())
    # data.to_excel('data.xlsx')

    # - - - OPERACIONES - - -
    operaciones = operations(data)
    # print(operaciones)

    # - - - TRADES - - -
    trades = make_trades(operaciones)
    # print(trades)

    # Plot de los trades
    # plots.plot_trades(data)

    # - - - RESULTADOS - - -
    resultado = make_results(trades)
    print(resultado)


if __name__ == '__main__':
    run('ETHUSDT', descargar_data=True)

