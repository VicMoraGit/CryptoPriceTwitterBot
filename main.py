"""
    This bot can manage multiple automated twitter price accounts

"""
#Exceptions
from custom_exceptions import SettingsNotLoadedException

#Settings
from settings import Settings

#Wrappers imports

from TwitterWrapper.twitter_wrapper import Twitter
from CoinMarketCapWrapper.CMCWrapper import CMC
if __name__ == "__main__":


    #Set bot settings

    settings = Settings("")

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
        currentPriceIntervalRounded = myround(currentPrice,coin.interval)

        lastPrice = coin.last_price
        if lastPrice != currentPriceIntervalRounded:
            tw.post_tweet(message)



def myround(x, base):
    return base * round(x/base)