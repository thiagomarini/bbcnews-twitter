import unittest

from config import FILE_DIR
from models.article import Article


class ArticleTest(unittest.TestCase):
    
    a = None

    def setUp(self):
        self.a = Article('Dummy title')

    def test_load_story(self):
        # mock the fetch with a local file
        self.a.html = open(FILE_DIR + 'article_dummy.html', 'r')
        self.a.load_story()
        
        self.assertTrue(self.a.story)
        
    def test_load_blacklisted_words(self):

        self.a.load_blacklisted_words()
        
        self.assertEquals(len(self.a.blacklisted_words), 674)
        
    def test_clean_story(self):
        # mock blaklisted words and story txt
        self.a.blacklisted_words = ['ab', 'aw', 'gaga']
        self.a.story = 'ab aw qw ladygaga';
        self.a.clean_story()
        
        self.assertEquals(self.a.story, 'qw ladygaga')

    def test_most_used_word(self):
        # mock blaklisted words
        self.a.story = 'ab aw qw ladygaga ab';
        self.a.most_common_word()
        
        self.assertEquals(self.a.most_used_word, 'ab')

if __name__ == '__main__':
    unittest.main()
