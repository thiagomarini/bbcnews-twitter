import re

from bs4 import BeautifulSoup

from config import FILE_DIR
from models.webpage_mixin import WebPageMixIn
from models.twitter import Twitter


class Article(WebPageMixIn):
    
    title = ''
    story = ''
    blacklisted_words = []
    most_used_word = ''
    tweets = None
    
    def __init__(self, title):
        self.title = title
        
    def load_story(self):
        """
        Extracts all the <p> tags on the 
        story-body div
        """
        soup = BeautifulSoup(self.html)
        body = soup.find(class_="story-body")
        
        for p in body.find_all('p'):
            self.story += p.text.lower()
            
    def load_blacklisted_words(self):
        """
        Loads blacklisted words from txt file that
        should be excluded from the count of most used words
        in the article
        """
        with open(FILE_DIR + 'blacklisted_words.txt') as file:
            for line in file:
                self.blacklisted_words.append(line.rstrip())# remove line breaks
                
    def clean_story(self):
        """
        Removes all the blacklisted words from the story
        using regex with the word boundery \b
        """
        
        pattern = re.compile("\\b(" + '|'.join(self.blacklisted_words) + ")\\W", re.I)
        self.story = pattern.sub("", self.story)
        
        for w in self.blacklisted_words:
            self.story = re.sub(r'\b' + w + r'\b', '', self.story)
        # trim and remove double space
        self.story = self.story.replace('  ', ' ').strip()
        
    def most_common_word(self):
        """Finds the most used word in the story"""
        lst = self.story.split(' ')
        self.most_used_word = max(set(lst), key=lst.count)
        
    def load_related_tweets(self):
        """
        Searches for the most used word in the
        article as twitter hashtag
        """
        t = Twitter() # this class is a singleton
        self.tweets = t.search(self.most_used_word)
        
    def load(self, url):
        """
        Groups all the tested methods in one
        """
        self.fetch(url)
        self.load_blacklisted_words()
        self.load_story()
        self.clean_story()
        self.most_common_word()
        self.load_related_tweets()
                
        
        
