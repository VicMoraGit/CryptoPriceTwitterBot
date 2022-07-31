class Coin():
    """
        Coin class

        Attributes:
            symbol (str): Coin symbol
            interval (int): Price interva
            last_price (int): Last price registered
            token (str): Twitter account token
            secret (str): Twitter account token secret
    """
    def __init__(self, symbol:str, interval:int, last_price:int, token:str, secret:str):
   
        self.symbol = symbol
        self.interval = interval
        self.last_price = last_price
        self.token = token
        self.secret = secret
    
    def to_map(self):
        """
            Generates a map with the coin info
        """

        coin_map = {
            "symbol": self.symbol,
            "interval": self.interval,
            "lastPricePosted": self.last_price,
            "twitterAccount": {
                "oauthToken": self.token,
                "oauthTokenSecret": self.secret
            }
        }

        return coin_map