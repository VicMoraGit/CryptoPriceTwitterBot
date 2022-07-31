"""
    Wraps Twitter's API to be used as an Object.

"""
#packages imports
import tweepy

class Twitter():
    """
    Twitter Object that eases Twitter API usage

    Attributes:
        app_api_key (str): You can find this API Key in your twitter developer portal
        app_api_key_secret (str): You can find this API Key in your twitter developer portal
       
    You can find how to get the last two mentioned attributes in the README
    """

    def __init__(self,app_api_key:str, app_api_key_secret:str) -> None:
        self.app_api_key = app_api_key
        self.app_api_key_secret = app_api_key_secret
        self.tweepy_api = None

    def auth(self,user_oauth_token:str, user_oauth_token_secret:str):
        """Authenticates bot account into tweepy

        Args:
             user_oauth_token(str): Bot account token
            user_oauth_token_secret(str): Bot account token secret
        """
        
        auth = tweepy.OAuth1UserHandler(self.app_api_key,self.app_api_key_secret,
        user_oauth_token,user_oauth_token_secret)
        
        self.tweepy_api = tweepy.API(auth)
        
    def post_tweet(self, price:int, is_bigger_than_last:bool, coin_symbol:str
    ) -> bool:
        """Posts a tweet on a given account

        Args:
            message (str): Tweet message

        Returns:
            bool: Status
        """

        if is_bigger_than_last:
            message = f"${coin_symbol} has rised to ${str(price)}📈"
        else:
            message = f"${coin_symbol} has fallen to ${str(price)}📉"

        print(self.tweepy_api.update_status(message))
        
        