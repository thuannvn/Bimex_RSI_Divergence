import ccxt
import time
bitmex = ccxt.bitmex()


# params:
symbol = 'XBTUSD'
timeframe = '1m'
since = None
limit = 100
params = {'partial': False, 'reverse':True}  # ←-------------  here you go


#markets = bitmex.load_markets()
#print(bitmex.id)
#print(markets)

while True:
    # the call:
    candles = bitmex.fetch_ohlcv(symbol, timeframe, since, limit, params)
    print('{}: O: {} H: {} L:{} C:{}'.format(
        bitmex.iso8601(candles[0][0]),
        candles[0][1],
        candles[0][2],
        candles[0][3],
        candles[0][4]))
    time.sleep(30)

