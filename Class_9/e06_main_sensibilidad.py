from e01_data import download_data
import e02_indicadores as indicadores
from e03_operaciones import signals, operations
from e04_trades import make_trades, make_results
import config

import pandas as pd

import time


# Ahora las emas son una lista
def run(symbol, timeframe=config.TIMEFRAME, descargar_data=True,
        emas_slow=config.SENS_EMA_SLOW,
        emas_fast=config.SENS_EMA_FAST):

    start_time = time.time()

    # Resultados acumulados donde vamos a guardar los resultados de cada combinacion de indicadores
    resultados = []

    # - - - DESCARGA DE DATOS - - -
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

    # print(emas_fast, emas_slow)

    # - - - CALCULO DE INDICADORES - - -
    # Ahora los indicadores los calculamos dentro del for
    # Borro columnas que no voy a usar
    data.drop(['o', 'h', 'l', 'v', 'v_q', 'n'], axis=1, inplace=True)

    print(f'Calculando valores de rsi: {config.SENS_RSI} y emas: {emas_slow} y {emas_fast}')

    for rsi in config.SENS_RSI:
        # por cada valor de rsi, calculo el rsi y las emas
        data['rsi'] = indicadores.add_rsi(data, 'c', rsi)

        for ema_slow in emas_slow:

            data['ema_slow'] = indicadores.add_ema(data, 'c', ema_slow)

            for ema_fast in emas_fast:
                if ema_fast >= ema_slow:  # Si la ema_fast es mayor o igual a la ema_slow, no la calculo
                    continue

                # cuantas veces corre el codigo?

                # print(f'Calculando con ema slow: {ema_slow}, ema fast: {ema_fast}')
                print(f'Calculando con rsi: {rsi}, ema fast: {ema_fast}, ema slow: {ema_slow}')

                data['ema_fast'] = indicadores.add_ema(data, 'c', ema_fast)

                data.dropna(inplace=True)

                # - - - SEÑALES - - -
                data['signal'] = signals(data, 'ema_slow', 'ema_fast', 'rsi')

                # - - - OPERACIONES - - -
                operaciones = operations(data)

                # - - - TRADES - - -
                trades = make_trades(operaciones)

                # - - - RESULTADOS - - -
                resultado = make_results(trades)

                # Agrego los resultados a la lista
                resultado['indicadores'] = f'rsi: {rsi}, ema_slow: {ema_slow}, ema_fast: {ema_fast}'
                resultados.append(resultado)

    # - - - RESULTADOS ACUMULADOS - - -
    resultados = pd.DataFrame(resultados)

    # Ordeno los resultados por profit
    resultados.sort_values(by='resultadodo_acumulado', ascending=False, inplace=True)

    # print(resultados.head(20))

    print(f'Tiempo de ejecución: {time.time() - start_time} segundos')
    print(f'Cantidad de resultados: {len(resultados)}')

    resultados.to_pickle(f'resultados_{symbol}')  # Guardamos los datos en un archivo pickle


if __name__ == '__main__':
    # run('BTCUSDT', '1h', False)
    data = pd.read_pickle(f'resultados_BTCUSDT')
    print(data.head(20))

