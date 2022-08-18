import requests
import numpy as np
import pandas as pd
from binance.spot import Spot


#spot_prices = {}

def binance_spot_price(symbol: str) -> float:
    client = Spot()
    ohlc_data = (client.klines(symbol, "1m", limit=1))
    binance_close_price = round(float(ohlc_data[0][4]), 3)
    return binance_close_price

def huobi_spot_price(symbol: str) -> float:
    # "https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol=btcusdt"
    ohlc_data = requests.get(f'https://api.huobi.pro/market/history/kline?period=1min&size=1&symbol={symbol}').json()
    houbi_close_price = round(float(ohlc_data['data'][0]['close']), 3)
    return houbi_close_price

def kucoin_spot_price(symbol: str) -> float:
    # 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT'
    ohlc_data = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}').json()
    kucoin_close_price = round(float(ohlc_data['data']['price']), 3)
    return kucoin_close_price

def kraken_spot_price(symbol: str) -> float:
    # 'https://api.kraken.com/0/public/OHLC?pair=XBTUSDT&interval=1'
    ohlc_data = requests.get(f'https://api.kraken.com/0/public/OHLC?pair={symbol}&interval=1').json()
    kraken_close_price = round(float(ohlc_data['result'][symbol][-1][4]), 3)
    return kraken_close_price

def yobit_spot_price(symbol: str) -> float:
    # 'https://yobit.net/api/3/ticker/btc_usdt'
    ohlc_data = requests.get(f'https://yobit.net/api/3/ticker/{symbol}').json()
    youbit_close_price = round(float(ohlc_data[symbol]['last']), 3)
    #buy_price = round(float(ohlc_data[symbol]['buy']), 3)
    #sell_price = round(float(ohlc_data[symbol]['sell']), 3)
    #spot_prices['yobit'] = {'buy': buy_price, 'sell': sell_price}
    #print(spot_prices)
    return youbit_close_price

def okx_spot_price(symbol: str) -> float:
    # 'https://www.okx.com/api/v5/market/index-tickers?instId=BTC-USDT'
    ohlc_data = requests.get(f'https://www.okx.com/api/v5/market/index-tickers?instId={symbol}').json()
    okx_close_price = round(float(ohlc_data['data'][0]['idxPx']), 3)
    # buy_asks_prices = requests.get(f'https://www.okx.com/api/v5/market/books?instId={symbol}').json()
    # sell_price = round(float(buy_asks_prices['data'][0]['asks'][0][0]), 3)
    # buy_price = round(float(buy_asks_prices['data'][0]['bids'][0][0]), 3)
    # print(buy_price)
    # print(sell_price)
    return okx_close_price

def ftx_spot_price(symbol: str) -> float:
    # 'https://ftx.com/api/markets/BTC/USDT'
    ohlc_data = requests.get(f'https://ftx.com/api/markets/{symbol}').json()
    ftx_close_price = round(float(ohlc_data['result']['last']), 3)
    # buy_price = round(float(ohlc_data['result']['bid']), 3)
    # sell_price = round(float(ohlc_data['result']['ask']), 3)
    # print(buy_price)
    # print(sell_price)
    return ftx_close_price

def bybit_spot_price(symbol: str) -> float:
    # 'https://api-testnet.bybit.com/v2/public/tickers?symbol=BTCUSDT'
    ohlc_data = requests.get(f'https://api-testnet.bybit.com/v2/public/tickers?symbol={symbol}').json()
    bybit_close_price = round(float(ohlc_data['result'][0]['last_price']), 3)
    #buy_price = round(float(ohlc_data['result'][0]['bid_price']), 3)
    #sell_price = round(float(ohlc_data['result'][0]['ask_price']), 3)
    # print(f'bid-{buy_price}')
    # print(f'ask-{sell_price}')
    return bybit_close_price

def bittrex_spot_price(symbol: str) -> float:
    # 'https://api.bittrex.com/v3/markets/btc-usdt/ticker'
    ohlc_data = requests.get(f'https://api.bittrex.com/v3/markets/{symbol}/ticker').json()
    bittrex_close_price = round(float(ohlc_data['lastTradeRate']), 3)
    # buy_price = round(float(ohlc_data['bidRate']), 3)
    # sell_price = round(float(ohlc_data['askRate']), 3)
    # print(f'bid-{buy_price}')
    # print(f'ask-{sell_price}')
    return bittrex_close_price

def phemex_spot_price(symbol: str) -> float:
    # 'https://api.phemex.com/md/trade?symbol=sBTCUSDT'
    ohlc_data = requests.get(f'https://api.phemex.com/md/trade?symbol={symbol}').json()
    phemex_close_price = round(float(ohlc_data['result']['trades'][0][2]), 3) / 100000000
    # bid_asks_prices = requests.get(f'https://api.phemex.com/md/orderbook?symbol={symbol}').json()
    # buy_price = round(float(bid_asks_prices['result']['book']['bids'][0][0]), 3) / 100000000
    # sell_price = round(float(bid_asks_prices['result']['book']['asks'][0][0]), 3) / 100000000
    # print(f'bid-{buy_price}')
    # print(f'ask-{sell_price}')
    return phemex_close_price
#https://github.com/phemex/phemex-api-docs/blob/master/Public-Spot-API-en.md#productinfo - symbols

def gemini_spot_price(symbol: str) -> float:
    # 'https://api.gemini.com/v1/pubticker/btcusd'
    ohlc_data = requests.get(f'https://api.gemini.com/v1/pubticker/{symbol}').json()
    gemini_close_price = round(float(ohlc_data['last']), 3)
    # buy_price = round(float(ohlc_data['bid']), 3)
    # sell_price = round(float(ohlc_data['ask']), 3)
    # print(f'bid-{buy_price}')
    # print(f'ask-{sell_price}')
    return gemini_close_price

def deribit_spot_price(symbol: str) -> float:
    # 'https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-PERPETUAL'
    ohlc_data = requests.get(f'https://www.deribit.com/api/v2/public/ticker?instrument_name={symbol}').json()
    deribit_close_price = round(float(ohlc_data['result']['last_price']), 3)
    # buy_price = round(float(ohlc_data['result']['best_bid_price']), 3)
    # sell_price = round(float(ohlc_data['result']['best_ask_price']), 3)
    # print(f'bid-{buy_price}')
    # print(f'ask-{sell_price}')
    return deribit_close_price


print('-----------BINANCE-----------')
print(binance_spot_price('BTCUSDT'))
print(binance_spot_price('ETHUSDT'))
print(binance_spot_price('LTCUSDT'))


print('-----------HUOBI-----------')
print(huobi_spot_price('BTCUSDT'.lower()))
print(huobi_spot_price('ETHUSDT'.lower()))
print(huobi_spot_price('LTCUSDT'.lower()))


print('-----------KUCOIN-----------')
print(kucoin_spot_price('BTC-USDT'))
print(kucoin_spot_price('ETH-USDT'))
print(kucoin_spot_price('LTC-USDT'))


print('-----------KRAKEN-----------')
print(kraken_spot_price('XBTUSDT'))
print(kraken_spot_price('ETHUSDT'))
print(kraken_spot_price('LTCUSDT'))


print('-----------YOBIT-----------')
print(yobit_spot_price('btc_usdt'))
print(yobit_spot_price('eth_usdt'))
print(yobit_spot_price('ltc_usdt'))


print('-----------OKX-----------')
print(okx_spot_price('BTC-USDT'))
print(okx_spot_price('ETH-USDT'))
print(okx_spot_price('LTC-USDT'))


print('-----------FTX-----------')
print(ftx_spot_price('BTC/USDT'))
print(ftx_spot_price('ETH/USDT'))
print(ftx_spot_price('LTC/USDT'))


print('-----------BYBIT-----------')
print(bybit_spot_price('BTCUSDT'))
print(bybit_spot_price('ETHUSDT'))
print(bybit_spot_price('LTCUSDT'))


print('-----------BITTREX-----------')
print(bittrex_spot_price('btc-usdt'))
print(bittrex_spot_price('eth-usdt'))
print(bittrex_spot_price('ltc-usdt'))


print('-----------PHEMEX-----------')
print(phemex_spot_price('sBTCUSDT'))
print(phemex_spot_price('sETHUSDT'))
print(phemex_spot_price('sLTCUSDT'))


print('-----------GEMINI-----------')
print(gemini_spot_price('btcusd'))
print(gemini_spot_price('ethusd'))
print(gemini_spot_price('ltcusd'))


print('-----------DERIBIT-----------')
print(deribit_spot_price('BTC-PERPETUAL'))
print(deribit_spot_price('ETH-PERPETUAL'))
print(deribit_spot_price('LTC_USDC-PERPETUAL'))
