URL_SPOT = 'https://api.binance.com'
PATH_SPOT = '/api/v3/klines'
URL_PERP = 'https://fapi.binance.com'
PATH_PERP = '/fapi/v1/klines'

TIMEFRAME = '1h'

EMA_FAST = 50
EMA_SLOW = 100

SENS_EMA_FAST = list(range(20, 70, 5))
SENS_EMA_SLOW = list(range(50, 200, 5))
SENS_RSI = list(range(14, 90, 5))
