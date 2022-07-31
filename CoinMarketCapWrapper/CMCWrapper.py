"""
    Wrapper for CoinMarketCap API
"""

#standard imports 

#package imports
from requests import get
class CMC():
    """
        CoinMarketCap API wrapper

        Attributes:
        - api_key = Your CMC API Key

    """
    
    def __init__(self,api_key:str):
        self.api_key = api_key

    def get_coins_price(self, coin_symbols:list):
        """Returns price of a given coin

        Args:
            coin_symbol (str): Coin symbol, e.g. ETH,BTC,BNB...

        Returns:
            _type_: _description_
        """
        price_dict = {}
        headers = {"X-CMC_PRO_API_KEY":self.api_key}

        url = "https://pro-api.coinmarketcap.com/"
        endpoint = "v2/cryptocurrency/quotes/latest"
        query = "?symbol="+",".join(coin_symbols)
        complete_url = url+endpoint+query
        print(complete_url)
        response = get(complete_url,headers=headers)
        print(response)
        coins = response.json()["data"]
        coin_symbols = list(coins.keys())

        for symbol in coin_symbols:
            price_dict[symbol] = coins[symbol][0]["quote"]["USD"]["price"]
        
        return price_dict