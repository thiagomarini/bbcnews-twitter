'''
Created on 20 Jan 2015

@author: Thiago Marini
'''
import json

from models import NewsPage


try:
    np = NewsPage()
    np.fetch('http://www.bbc.co.uk/news/')
    print np.search()
except Exception:
    print json.dumps({'articles':[], 'success': False})