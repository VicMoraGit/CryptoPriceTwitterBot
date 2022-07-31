class Coin():
    def __init__(self, symbol:str, interval:int, last_price:int, token:str, secret:str):
        self.symbol = symbol
        self.interval = interval
        self.last_price = last_price
        self.token = token
        self.secret = secret