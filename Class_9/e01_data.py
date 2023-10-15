import pandas as pd
import requests
import time
import threading
import datetime as dt
from math import ceil
import numpy as np
from config import URL_PERP, URL_SPOT, PATH_PERP, PATH_SPOT, TIMEFRAME

# Solo para mostrar más columnas en pandas
pd.options.display.max_columns = 20


# PERPETUAL FUTURES HISTORICAL PRICES
def get_data_binance(symbol, interval, api='PERPETUOS', start_time=None, end_time=None, limit=1000):
    """

    (Ver la doc)
    https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

    :param symbol: BTCUSDT, ETHUSDT, etc
    :param interval: 1m, 1h, 1d, etc
    :param start_time: timestamp in ms  (el timestamp es el numero de segundos desde 1970)
    :param end_time: timestamp in ms
    :param limit: 1000
    :return:

    Ejemplo de perpetuos:
        [
          [
            1499040000000,      // Open time
            "0.01634790",       // Open
            "0.80000000",       // High
            "0.01575800",       // Low
            "0.01577100",       // Close
            "148976.11427815",  // Volume
            1499644799999,      // Close time
            "2434.19055334",    // Quote asset volume
            308,                // Number of trades
            "1756.87402397",    // Taker buy base asset volume
            "28.46694368",      // Taker buy quote asset volume
            "17928899.62484339" // Ignore.
          ]
        ]

    Ejemplo de spot:
        [
          [
            1499040000000,      // Kline open time
            "0.01634790",       // Open price
            "0.80000000",       // High price
            "0.01575800",       // Low price
            "0.01577100",       // Close price
            "148976.11427815",  // Volume
            1499644799999,      // Kline close time
            "2434.19055334",    // Quote asset volume
            308,                // Number of trades
            "1756.87402397",    // Taker buy base asset volume
            "28.46694368",      // Taker buy quote asset volume
            "0"                 // Unused field. Ignore.
          ]
        ]

    """

    url = URL_PERP + PATH_PERP if api == 'PERPETUOS' else URL_SPOT + PATH_SPOT

    if start_time:

        if end_time:
            params = {'symbol': symbol, 'interval': interval,
                      'startTime': start_time, 'endTime': end_time,
                      'limit': limit}
        else:
            params = {'symbol': symbol, 'interval': interval,
                      'startTime': start_time,
                      'limit': limit}

    else:
        params = {'symbol': symbol, 'interval': interval, 'limit': limit}

    r = requests.get(url, params=params)

    js = r.json()

    return js


def chunk_dates(timestamp_init, timestamp_fin, frequency, workers=20, limit=999):
    """
    :param workers: k of threads
    :param timestamp_init: timestamp
    :param timestamp_fin: timestamp
    :param frequency: 1s, 1m, 1h, etc
    :param limit: limit of data que da la api
    :return:
    """

    multiplier = 1

    if frequency == '1s':
        multiplier = 1000

    elif frequency == '1m':
        multiplier = 60000

    elif frequency == '1h':
        multiplier = 3600000

    elif frequency == '4h':
        multiplier = 14400000

    elif frequency == '8h':
        multiplier = 28800000

    elif frequency == '1d':
        multiplier = 86400000

    k_requests = ceil(((timestamp_fin - timestamp_init) / multiplier) / limit)

    step = multiplier * limit

    dates_init = [timestamp_init]
    timestamp_provisory = timestamp_init
    for i in range(k_requests):
        timestamp_provisory += step
        if timestamp_provisory > timestamp_fin:
            break

        else:
            dates_init.append((timestamp_provisory))

        list_for_workers = np.array_split(dates_init, workers)

    return list_for_workers


def work_list_binance(list_data):
    """
    :param list_data: of download data binance
    :return: df with time, o, h, l, c, v, v_q, n
    """

    df = pd.DataFrame(list_data)
    df.drop([6, 9, 10, 11], axis=1, inplace=True)
    df.columns = ['time', 'o', 'h', 'l', 'c', 'v', 'v_q', 'n']

    return df


def work_download(ticker, list_periods, api, frecuency, bad_request, df, limit):
    """
    Funcion para manejar la descarga del mismo ticker en varios intervalos

    :param api: SPOT o PERPETUOS
    :param ticker:
    :param list_periods:
    :param frecuency:
    :param bad_request:
    :param df:
    :param limit:
    :return:
    """

    df_provisory = []
    bad_request_provisorio = []

    for period in list_periods:
        # print(period)
        time.sleep(0.5)
        # print(threading.current_thread().name)

        result = get_data_binance(symbol=ticker, interval=frecuency, api=api, start_time=period)

        if not result:
            bad_request_provisorio.append(period)

        else:
            result = work_list_binance(result)

            df_provisory.append(result)

    bad_request.extend(bad_request_provisorio)
    df.extend(df_provisory)


def download_data(ticker, frequency, date_init: str, date_fin: str, api='SPOT', workers=20, limit=1000):
    """
    Funcion que toma el ticker y maneja hilos para la descarga de data

    :param date_fin:
    :param api: SPOT o PERPETUOS
    :param date_init: '2022-01-01'
    :param frequency: 1s, 1m, 1h, etc
    :param workers: k of threads
    :return:
    """

    timestamp_init = int(time.mktime(dt.datetime.strptime(date_init, "%Y-%m-%d").timetuple()) * 1000)
    timestamp_fin = int(time.mktime(dt.datetime.strptime(date_fin, "%Y-%m-%d").timetuple()) * 1000)

    list_for_workers = chunk_dates(timestamp_init=timestamp_init, timestamp_fin=timestamp_fin,
                                   frequency=frequency, workers=workers, limit=limit)  # Divido las fechas en k partes

    df = []
    bad_requests = []

    threads = []
    for i in list_for_workers:
        t = threading.Thread(target=work_download, args=(ticker, i, api, frequency, bad_requests, df, limit))  # Creo los threads
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    df = pd.concat(df, axis=0)  # Uno todos los dataframes

    df.drop_duplicates(subset='time', keep='first', inplace=True)  # Borro los duplicados
    df.set_index('time', inplace=True)  # Pongo el indice en el tiempo

    df.sort_index(inplace=True)  # Ordeno por tiempo

    return df, bad_requests


if __name__ == '__main__':
    symbol = 'BTCUSDT'
    interval = '1h'

    start_time = time.time()

    # data = download_data(symbol, interval, date_init='2015-01-01', date_fin='2023-10-13', api='SPOT')
    #
    data = get_data_binance(symbol=symbol, interval=interval)

    print(data)

    print("--- %s seconds ---" % (time.time() - start_time))