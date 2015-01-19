import urllib2

class WebPageMixIn(object):
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
        
        
