'''
Created on 20 Jan 2015

@author: Thiago Marini
'''
import re, json, urllib2

from bs4 import BeautifulSoup

from services import blwp, twitter


class WebPage(object):
    """
    Provides the fecth method to 
    other classes
    """
    
    html = None
        
    def fetch(self, url):
        """ Fetches the webpage html"""
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        self.html = response.read()
        if not self.html:
            raise Exception('Unable to fetch the webpage HTML')

class NewsPage(WebPage):
    
    url = ''
    content = ''
    articles = []
    links = None
    json_string = ''
        
    def load_links(self):
        """
        Finds and loads the links for most shared 
        articles in the most-popular table
        """
        soup = BeautifulSoup(self.html)
        self.links = soup.find(id="most-popular").ol
        
        
    def load_articles(self):
        """
        Populates the articles list
        """
        for link in self.links.find_all('a'):
            a = Article(link.text)
            a.load(link.get('href'))
            self.articles.append(a)
            
    def json_dumps(self):
        """
        Prepares the articles for the output json string
        """
        r = {}
        r['success'] = True
        r['articles'] = []
        for a in self.articles:
            dic = {}
            dic['title'] = a.title
            dic['most_used_word'] = a.most_used_word
            dic['tweets'] = a.tweets
            r['articles'].append(dic)
        self.json_string = json.dumps(r)
    
    def search(self):
        """
        Groups all the tested methods in one
        """
        self.load_links()
        self.load_articles()
        self.json_dumps()
        return self.json_string

class Article(WebPage):
    
    title = ''
    story = ''
    most_used_word = ''
    tweets = None
    blwp = None
    
    def __init__(self, title):
        self.title = title
        
    def load_story(self):
        """
        Extracts all the <p> tags from the 
        story-body div
        """
        soup = BeautifulSoup(self.html)
        body = soup.find(class_="story-body")
        
        for p in body.find_all('p'):
            self.story += p.text.lower()
            
        if not self.story:
            raise RuntimeError("Unable to get article's story: " + self.title)
                
    def clean_story(self):
        """
        Removes all the blacklisted words from the story
        using regex with the word boundery \b
        """
        str_pattern = "\\b(" + '|'.join(blwp.get_words()) + ")\\W"
        pattern = re.compile(str_pattern, re.I)
        self.story = pattern.sub('', self.story)
        
        # trim and remove double space
        self.story = self.story.replace('  ', ' ').strip()
        
    def most_common_word(self):
        """
        Finds the most used word in the story
        """
        lst = self.story.split(' ')
        self.most_used_word = max(set(lst), key=lst.count)
        
    def load_related_tweets(self):
        """
        Searches for the most used word in the
        article as twitter hashtag
        """
        self.tweets = twitter.search(self.most_used_word)
        
    def load(self, url):
        """
        Groups all the tested methods in one
        """
        self.fetch(url)
        self.load_story()
        self.clean_story()
        self.most_common_word()
        self.load_related_tweets()