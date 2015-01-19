from models.news_page import NewsPage
import json

try:
    np = NewsPage()
    np.fetch('http://www.bbc.co.uk/news/')
    print np.search()
except Exception:
    print json.dumps({'articles':[], 'success': False})