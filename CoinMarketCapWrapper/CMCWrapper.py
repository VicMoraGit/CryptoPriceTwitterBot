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

    def get_coin_price(self, coin_symbol:str):
        """Returns price of a given coin

        Args:
            coin_symbol (str): Coin symbol, e.g. ETH,BTC,BNB...

        Returns:
            _type_: _description_
        """
        headers = {"X-CMC_PRO_API_KEY":self.api_key}

        url = "https://pro-api.coinmarketcap.com/"
        endpoint = "v2/cryptocurrency/quotes/latest"
        query = f"?symbol={coin_symbol}"
        complete_url = url+endpoint+query

        response = get(complete_url,headers=headers)
        price = response.json()["data"][coin_symbol][0]["quote"]["USD"]["price"]
        
        return price