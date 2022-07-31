"""
    Bot settings class
"""

import json
from os import path
from CoinMarketCapWrapper.coin import Coin
class Settings:
    """
        Imports, store and exports bot settings
    """

    def __init__(self, config_file_path:str = None) -> None:
        self.is_first_run = None
        self.coins = []
        self.config_file_path = config_file_path
        
        self.twitter_api_key = None
        self.twitter_api_key_secret = None

    def save(self):
        """
            Saves settings on current configuration file path

        Returns:
            bool: Status of the operation
        """
        settings_dict ={
            "isFirstRun": self.is_first_run
        }

        try:
            self._save_file(settings_dict)
            return True
        except FileNotFoundError:
            return False

    def load(self) -> bool:

        """
            Loads all the config file parameters to the settings class

        Args:
            config_file_path (str): Configuration file path

        Returns:
            bool: Status of the operation
        """
        
        
        try:
            settings = self._config_file2json()
            self.is_first_run = settings["isFirstRun"]
            self.coins = self._get_coins_list(settings["coins"])
            self.twitter_api_key =  settings["APIKey"]
            self.twitter_api_key_secret = settings ["APIKeySecret"]
        
        except KeyError:

            print("Wrong configuration file format.")
            return False

        except FileNotFoundError:

            print("File does not exists")
            return False

        return True

    def _get_coins_list(self, json_coins:dict):
        coins = []

        for json_coin in json_coins:

            symbol = json_coin["symbol"]
            interval = json_coin["interval"]
            last_price = json_coin["lastPricePosted"]
            token = json_coin["twitterAccount"]["oauthToken"]
            secret = json_coin["twitterAccount"]["oauthTokenSecret"]


            coin = Coin(symbol, interval, last_price,token,secret)
            coins.append(coin)

        return coins


    def _config_file2json(self):

        settings = json.loads(self._read_file())
        return settings

    def _json2config_file(self,settings_dict):

        settings_str = json.dumps(settings_dict)
        return settings_str

    def _read_file(self):

        with open(file=self.config_file_path, mode="r", encoding="utf-8") as file:
            json_content = file.read()
            file.close()
        return json_content

    def _save_file(self, settings_dict):

        settings_str = self._json2config_file(settings_dict)

        if path.exists(self.config_file_path):

            with open(file=self.config_file_path, mode="w", encoding="utf-8") as file:
                file.write(settings_str)
                file.close()
        else:
            raise FileNotFoundError()
