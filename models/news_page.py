import json

from bs4 import BeautifulSoup

from models.article import Article
from models.webpage_mixin import WebPageMixIn


class NewsPage(WebPageMixIn):
    
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
            
            
        
        
        
