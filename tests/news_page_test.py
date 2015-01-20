import unittest, bs4

from config import FILE_DIR
from models import NewsPage


class NewsPageTest(unittest.TestCase):
    
    np = None

    def setUp(self):
        self.np = NewsPage()

    def test_load_links(self):
        # mock the fetch
        self.np.html = open(FILE_DIR + 'bbcnews_dummy.html', 'r')
        self.np.load_links()
        
        self.assertTrue(isinstance(self.np.links, bs4.element.Tag))

if __name__ == '__main__':
    unittest.main()
