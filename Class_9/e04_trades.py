import pandas as pd
import numpy as np


def make_trades(data, close='c', operacion='operacion', side='BOTH'):
    """
    A partir de un dataframe con los precios y las operaciones, genera un dataframe con los trades.

    El ultimo trade lo cierro con el ultimo valor del dataframe.

    side puede ser 'BOTH', 'long' o 'short'

    return un dataframe con los trades
    """

    df = data.copy()

    filtro_trades = pd.DataFrame()  # Genero un dataframe vacio

    # Precios open y close de los trades
    filtro_trades['price_open'] = df[close]  # Abro la posicion con el precio de cierre de la vela
    filtro_trades['price_close'] = df[close].shift(-1)  # Con el shift -1 me muevo una posicion hacia adelante

    # Side
    filtro_trades['side'] = df[operacion]  # Agrego el dato de si es long o short

    # Fechas inicio y fin de los trades
    filtro_trades['date_init'] = df.index  # Agrego la fecha de inicio del trade
    filtro_trades['date_fin'] = filtro_trades['date_init'].shift(-1)  # Agrego la fecha de fin del trade
    filtro_trades = filtro_trades.iloc[:-1]  # Borro el ultimo trade ya que no tiene fecha de fin

    # Borro el index asi quedan numerados los trades
    filtro_trades.index.name = 'date'  # Le pongo nombre al indice para poder resetearlo
    filtro_trades.reset_index(inplace=True)  # Reseteo el indice para poder borrarlo
    filtro_trades.drop(['date'], axis=1, inplace=True)  # Borro el indice

    # En caso que quiera ir solo long o short, lo puedo filtrar aca
    if side != 'BOTH':
        filtro_trades = filtro_trades.loc[filtro_trades['side'] == side]

    return filtro_trades


def make_results(trades, long='long'):

    if len(trades) < 5:
        return None

    df = trades.copy()  # no es necesario, pero por las dudas

    df['dias'] = df['date_fin'] - df['date_init']  # Calculo los dias que duro cada trade

    # Calculo el resultado de cada trade
    df['rdo'] = np.where(df['side'] == long, df['price_close'] / df['price_open'] - 1,
                         df['price_open'] / df['price_close'] - 1) * 100

    # Calculo el resultado acumulado. Cumprod multiplica todos los valores de la columna
    df['rdo_acu'] = ((df['rdo'] / 100 + 1).cumprod() - 1) * 100  # cumprod multiplica todos los valores de la columna

    # Agrupo por trades ganadores y perdedores
    count_operations = df['rdo'].groupby([df['rdo'] > 0]).count().to_dict()
    if True not in count_operations:  # Si no hay ganadores, pongo 0
        n_ganadores = 0
        n_perdedores = count_operations[False]

    else:
        n_ganadores = count_operations[True]
        n_perdedores = count_operations[False]

    # Calculo el porcentaje de ganadores y perdedores
    if n_ganadores == 0:
        per_n_ganadores = 0
        per_n_perdedores = 100

    else:
        per_n_ganadores = (n_ganadores / (n_perdedores + n_ganadores)) * 100
        per_n_perdedores = (n_perdedores / (n_perdedores + n_ganadores)) * 100

    # Calculo el resultado promedio de ganadores y perdedores
    per_operations = df['rdo'].groupby([df['rdo'] > 0]).mean().to_dict()
    if True not in per_operations:  # Si no hay ganadores, pongo 0
        per_ganadores = 0
        per_perdedores = per_operations[False]

    else:
        per_ganadores = per_operations[True]
        per_perdedores = per_operations[False]

    # Calculo el resultado acumulado
    last_data = df.iloc[-1].to_dict()   # Ultima fila del dataframe

    result = {}
    result['resultadodo_acumulado'] = last_data['rdo_acu']
    result['operaciones_totales'] = df.index[-1] + 1
    result['n_ganadores'] = n_ganadores
    result['n_perdedores'] = n_perdedores
    result['porcentaje_ganadores'] = per_n_ganadores
    result['porcentaje_perdedores'] = per_n_perdedores
    result['resultado_promedio_ganadores'] = per_ganadores
    result['resultado_promedio_perdedores'] = per_perdedores

    return result

