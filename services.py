'''
Created on 20 Jan 2015

@author: Thiago Marini
'''
from twython.api import Twython

from config import FILE_DIR


class BlacklistedWordsProvider:
    """Wraps the blacklisted_words.txt reading"""
    
    words = []
    
    def get_words(self):
        
        if len(self.words) > 0:
            return self.words
        
        with open(FILE_DIR + 'blacklisted_words.txt') as f:
            for line in f:
                self.words.append(line.rstrip())  # remove line breaks
                
        return self.words

blwp = BlacklistedWordsProvider()

class Twitter:
    """
    Encapsulates the Twython lib for
    isolation and maintainability
    """
    
    TWITTER_APP_KEY = '???'
    TWITTER_APP_KEY_SECRET = '???' 
    TWITTER_ACCESS_TOKEN = '???'
    TWITTER_ACCESS_TOKEN_SECRET = '???'
    
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
    
twitter = Twitter()
