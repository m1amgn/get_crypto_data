import requests

def binance_spot_price(symbol: str, limit: int) -> float:
      
    base_url = "https://api.binance.com/api/v3"
    endpoint = f"/depth"
    
    params = {
        "symbol": symbol,
        "limit": limit
    }
    
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["bids"]
        asks = data["asks"]
    else:
        print(f'Error retrieving order book data - {data}')
    
    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def huobi_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://api.huobi.pro"
    endpoint = f"/market/depth"
    
    params = {
        "symbol": symbol,
        "type": "step1",  # step0 for merged depth, step1 for precision depth
        "depth": limit
    }
    
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200 and data.get("status") == "ok":
        bids = data["tick"]["bids"]
        asks = data["tick"]["asks"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def kucoin_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://api.kucoin.com"
    endpoint = f"/api/v1/market/orderbook/level2_20"
    
    params = {
        "symbol": symbol,
        "limit": limit
    }
    
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["data"]["bids"]
        asks = data["data"]["asks"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
        
        
def kraken_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://api.kraken.com"
    endpoint = f"/0/public/Depth"
    
    params = {
        "pair": symbol,
        "count": limit
    }
    
    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if "result" in data:
        result = data["result"]
        bids = result[symbol]["bids"]
        asks = result[symbol]["asks"]
    else:
        print(f'Error retrieving order book data - {data}')
    
    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def yobit_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://yobit.net/api/3"
    endpoint = f"/depth/{symbol}"

    params = {
        "limit": limit
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()

    if response.status_code == 200:
        bids = data[symbol]["bids"]
        asks = data[symbol]["asks"]
    else:
        print(f'Error retrieving order book data - {data}')


    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def okx_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://www.okex.com/api/v5"
    endpoint = f"/market/books"

    params = {
        "instId": symbol,
        "sz": limit
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["data"][0]["bids"]
        asks = data["data"][0]["asks"]
    else:
        print(f'Error retrieving order book data - {data}')


    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def bybit_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://api-testnet.bybit.com/v5"
    endpoint = f"/market/orderbook"

    params = {
        "category": "spot",
        "symbol": symbol,
        "limit": limit
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["result"]["b"]
        asks = data["result"]["a"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def bittrex_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://api.bittrex.com/v3"
    endpoint = f"/markets/{symbol}/orderbook"

    params = {
        "depth": limit
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["bid"]
        asks = data["ask"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0]["rate"]), 3)
    bids_volumes = round(float(bids[0]["quantity"]), 3)
    min_asks_price = round(float(asks[0]["rate"]), 3)
    asks_volumes = round(float(asks[0]["quantity"]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
    
def phemex_spot_price(symbol: str) -> float:
    base_url = "https://api.phemex.com/md"
    endpoint = f"/orderbook"

    params = {
       "symbol": symbol
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()

    if response.status_code == 200:
        bids = data["result"]["book"]["asks"]
        asks = data["result"]["book"]["bids"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0] / 10000), 3)
    bids_volumes = round(float(bids[0][1] / 10000), 3)
    min_asks_price = round(float(asks[0][0] / 10000), 3)
    asks_volumes = round(float(asks[0][1] / 10000), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')
    
    
def gemini_spot_price(symbol: str) -> float:
    base_url = "https://api.gemini.com/v1"
    endpoint = f"/book/{symbol}"

    response = requests.get(base_url + endpoint)
    data = response.json()

    if response.status_code == 200:
        bids = data["bids"]
        asks = data["asks"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0]["price"]), 3)
    bids_volumes = round(float(bids[0]["amount"]), 3)
    min_asks_price = round(float(asks[0]["price"]), 3)
    asks_volumes = round(float(asks[0]["amount"]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')


def deribit_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://www.deribit.com/api/v2"
    endpoint = f"/public/get_order_book"

    params = {
        "instrument_name": symbol,
        "depth": limit
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["result"]["bids"]
        asks = data["result"]["asks"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f"Максимальная цена покупки {symbol} {max_bids_price} - объем {round(bids_volumes / max_bids_price, 3)} - сумма {bids_volumes}")
    print(f"Максимальная цена покупки {symbol} {min_asks_price} - объем {round(asks_volumes / min_asks_price, 3)} - сумма {asks_volumes}")
    
    
def gateio_spot_price(symbol: str) -> float:
    base_url = "https://api.gate.io/api2/1"
    endpoint = f"/orderBook/{symbol}"

    response = requests.get(base_url + endpoint)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["bids"]
        asks = data["asks"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')


def mexc_spot_price(symbol: str, limit: int) -> float:
    base_url = "https://api.mexc.com/api/v3"
    endpoint = f"/depth"

    params = {
    "symbol": symbol,
    "limit": limit
    }

    response = requests.get(base_url + endpoint, params=params)
    data = response.json()
    
    if response.status_code == 200:
        bids = data["bids"]
        asks = data["asks"]
    else:
        print(f'Error retrieving order book data - {data}')

    max_bids_price = round(float(bids[0][0]), 3)
    bids_volumes = round(float(bids[0][1]), 3)
    min_asks_price = round(float(asks[0][0]), 3)
    asks_volumes = round(float(asks[0][1]), 3)
    
    print(f'Максимальная цена покупки {symbol} {max_bids_price} - объем {bids_volumes} - сумма {round(max_bids_price * bids_volumes, 3)}')
    print(f'Минимальная цена продажи {symbol} {min_asks_price} - объем {asks_volumes} - сумма {round(min_asks_price * asks_volumes, 3)}')


print("-----------BINANCE-----------")
binance_spot_price("BTCUSDT", 1)
binance_spot_price("ETHUSDT", 1)
binance_spot_price("LTCUSDT", 1)
print()

print("-----------HUOBI-----------")
huobi_spot_price("BTCUSDT".lower(), 5)
huobi_spot_price("ETHUSDT".lower(), 5)
huobi_spot_price("LTCUSDT".lower(), 5)
print()

print("-----------KUCOIN-----------")
kucoin_spot_price("BTC-USDT", 1)
kucoin_spot_price("ETH-USDT", 1)
kucoin_spot_price("LTC-USDT", 1)
print()

print("-----------KRAKEN-----------")
kraken_spot_price("XBTUSDT", 1)
kraken_spot_price("ETHUSDT", 1)
kraken_spot_price("LTCUSDT", 1)
print()

print("-----------YOBIT-----------")
yobit_spot_price("btc_usdt", 5)
yobit_spot_price("eth_usdt", 5)
yobit_spot_price("ltc_usdt", 5)
print()

print("-----------OKX-----------")
okx_spot_price("BTC-USDT", 5)
okx_spot_price("ETH-USDT", 5)
okx_spot_price("LTC-USDT", 5)
print()

print("-----------BYBIT-----------")
bybit_spot_price("BTCUSDT", 1)
bybit_spot_price("ETHUSDT", 1)
bybit_spot_price("LTCUSDT", 1)
print()

print("-----------BITTREX-----------")
bittrex_spot_price("BTC-USDT", 1)
bittrex_spot_price("ETH-USDT", 1)
bittrex_spot_price("LTC-USDT", 1)
print()

print("-----------PHEMEX-----------")
phemex_spot_price("BTCUSD")
phemex_spot_price("ETHUSD")
phemex_spot_price("LTCUSD")
print()

print("-----------GEMINI-----------")
gemini_spot_price("btcusd")
gemini_spot_price("ethusd")
gemini_spot_price("ltcusd")
print()

print("-----------DERIBIT-----------")
deribit_spot_price("BTC-PERPETUAL", 5)
deribit_spot_price("ETH-PERPETUAL", 5)
deribit_spot_price("LTC_USDC-PERPETUAL", 5)
print()

print("-----------GATEIO-----------")
gateio_spot_price("btc_usdt")
gateio_spot_price("eth_usdt")
gateio_spot_price("ltc_usdt")
print()

print("-----------MEXC-----------")
mexc_spot_price("BTCUSDT", 5)  
mexc_spot_price("ETHUSDT", 5)  
mexc_spot_price("ETHUSDT", 5)  
print()
