from twython.api import Twython
from models.singleton import singleton

@singleton
class Twitter:
    """
    Encapsulates the Twython lib for
    isolation and maintainability
    """
    
    TWITTER_APP_KEY = '5UyB2zwASh2yLZDP2DEABlCyt'
    TWITTER_APP_KEY_SECRET = 'sjTypPTxKMBNnCY7kHrRcF1AVioDosBlmz0Ip53qHsGFQkCHfW' 
    TWITTER_ACCESS_TOKEN = '599422503-05X7E1NRAmaCPNIlSUo44hrLPFi35S5MY4RLVyWj'
    TWITTER_ACCESS_TOKEN_SECRET = '7kBTby7sLHD8zI5UyUDPcIhLzmoqYKzmW7pwRt3zAcfBx'
    
    tweets = None
    api = None
    
    def __init__(self):
        self.api = Twython(app_key=self.TWITTER_APP_KEY,
                           app_secret=self.TWITTER_APP_KEY_SECRET,
                           oauth_token=self.TWITTER_ACCESS_TOKEN,
                           oauth_token_secret=self.TWITTER_ACCESS_TOKEN_SECRET)
        
    def search(self, word):
        """ Looks up the word as Twitter hashtag"""
        
        search = self.api.search(q='#' + word, count=5)
        return search['statuses']
