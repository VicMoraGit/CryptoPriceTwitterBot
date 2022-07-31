"""
    Wrapper for CoinMarketCap API
"""

class CMC():
    
    def __init__(self,api_key:str):
        self.api_key = api_key
