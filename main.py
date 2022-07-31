"""
    This bot can manage multiple automated twitter price accounts

"""
#Standard imports

from math import floor

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


if __name__ == "__main__":


    #Set bot settings

    settings = Settings("config.example.json")

    IS_LOADED = settings.load()

    if not IS_LOADED:
        raise SettingsNotLoadedException()


    #Initialize wrappers

    tw = Twitter(settings.twitter_api_key,settings.twitter_api_key_secret)
    cmc = CMC(settings.cmc_api_key)


    #Iterate over every coin account

    for coin in settings.coins:

        #Price comparison

        currentPrice = round(cmc.get_coin_price(coin.symbol),2)
        currentPriceIntervalRounded = myfloor(currentPrice,coin.interval)

        lastPrice = coin.last_price
       
        #If price is less than last interval it checks if it reached the next lower interval
        #If price is higuer than last interval it checks if it reached 
        # the next higher interval (using floor we get rid of this)
        #And posts a tweet (after authenticating to twitter)
        if (lastPrice > currentPriceIntervalRounded and
        lastPrice-coin.interval >= currentPrice) or lastPrice < currentPriceIntervalRounded:
            is_bigger_than_last =lastPrice<currentPrice

            #Twitter authentication

            tw.auth(coin.token, coin.secret)
            #Posts tweet based on price info
            tw.post_tweet(currentPrice, is_bigger_than_last, coin.symbol)

            #Saves the new price in the personal settings
            coin.last_price = currentPriceIntervalRounded

            settings.save()
