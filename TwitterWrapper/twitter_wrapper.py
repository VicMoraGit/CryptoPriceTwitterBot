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
        user_oauth_token(str): Bot account token
        user_oauth_token_secret(str): Bot account token secret

    You can find how to get the last two mentioned attributes in the README
    """

    def __init__(self,app_api_key:str, app_api_key_secret:str,
    user_oauth_token:str, user_oauth_token_secret:str) -> None:
        auth = tweepy.OAuth1UserHandler(app_api_key,app_api_key_secret,
        user_oauth_token,user_oauth_token_secret)
        self.tweepy_api = tweepy.API(auth)

    def post_tweet(self, message:str) -> bool:
        """Posts a tweet on a given account

        Args:
            message (str): Tweet message

        Returns:
            bool: Status
        """
        print(self.tweepy_api.update_status(message))
        
        