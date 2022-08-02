"""
    This bot can manage multiple automated twitter price accounts

"""
#Standard imports

from math import floor, ceil

#Exceptions
from custom_exceptions import SettingsNotLoadedException

#Settings
from settings import Settings

#Wrappers imports

from TwitterWrapper.twitter_wrapper import Twitter
from CoinMarketCapWrapper.CMCWrapper import CMC

def myfloor(num:float, base:int):
    """floors a number using a specific base

    Args:
        num (float): floating number
        base (int): base

    Returns:
        _type_: _description_
    """
    return base * floor(num/base)

def myceil(num:float, base:int):
    """ceils a number using a specific base

    Args:
        num (float): floating number
        base (int): base

    Returns:
        _type_: _description_
    """
    return base * ceil(num/base)

def get_coin_symbols(coins):
    """returns all the coin symbols in a list

    Args:
        coins (_type_): coins of the configuration files

    Returns:
        list: coin symbols
    """
    symbols=[]
    for _coin in coins:
        symbols.append(_coin.symbol)
    return symbols


if __name__ == "__main__":


    #Set bot settings

    settings = Settings("config.example.json")

    IS_LOADED = settings.load()

    if not IS_LOADED:
        raise SettingsNotLoadedException()


    #Initialize wrappers

    tw = Twitter(settings.twitter_api_key,settings.twitter_api_key_secret)
    cmc = CMC(settings.cmc_api_key)

    #Get price for each crypto on the settings file
    coin_symbols = get_coin_symbols(settings.coins)
    price_dict = cmc.get_coins_price(coin_symbols)

    #Iterate over every coin account

    for coin in settings.coins:

        #Price comparison
        last_interval_price = coin.last_price
        current_price = round(price_dict[coin.symbol],2)
        price_has_changed = False


        #Checks if price is lower than the next lower interval e.g:
        # - current price -> 1607.43
        # - last price interval -> 1650
        # - next interval -> 1600
        # NOT REACHED, NO POST
        # If it reached it, ceil the current price to get the last price interval.
        

        
        if current_price < last_interval_price-coin.interval:
            current_price_interval_rounded = myceil(current_price,coin.interval)
            price_has_changed = True
            
        #Checks if price is lower than the next lower interval e.g:
        # - current price -> 1607.43
        # - last price interval -> 1650
        # - next interval -> 1600
        # NOT REACHED, NO POST
        # If it reached it, ceil the current price to get the last price interval.

        if current_price > last_interval_price+coin.interval:
            current_price_interval_rounded = myfloor(current_price,coin.interval)
            price_has_changed = True
       
        #Posts a tweet if price changed(after authenticating to twitter)
       
        if price_has_changed:
            is_bigger_than_last = current_price > last_interval_price

            #Twitter authentication

            tw.auth(coin.token, coin.secret)
            #Posts tweet based on price info
            tw.post_tweet(current_price, is_bigger_than_last, coin.symbol)

            #Saves the new price in the personal settings
            coin.last_price = current_price_interval_rounded

            settings.save()
