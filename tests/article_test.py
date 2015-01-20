import unittest, mock

from config import FILE_DIR
from models import Article


class ArticleTest(unittest.TestCase):
    """
    Unit tests for the articles methods
    """
    
    a = None

    def setUp(self):
        self.a = Article('Dummy title')

    def test_load_story(self):
        # mock the fetch with a local file
        self.a.html = open(FILE_DIR + 'article_dummy.html', 'r')
        self.a.load_story()
        
        self.assertTrue(self.a.story)
    
    @mock.patch('models.blwp')
    def test_clean_story(self, mock_blwp):
        
        mock_blwp.get_words.return_value = ['gaga', 'afterwards', 'wa']
        self.a.story = 'afterwards you win';
        self.a.clean_story()
        
        mock_blwp.get_words.assert_called_with()
        self.assertEquals(self.a.story, 'you win')
    
    def test_most_used_word(self):
        # mock story text
        self.a.story = 'afterwards you win and win';
        self.a.most_common_word()
         
        self.assertEquals(self.a.most_used_word, 'win')
        
    @mock.patch('models.twitter')
    def test_load_related_tweets(self, mock_twitter):
        
        mock_twitter.search.return_value = ['t1', 't2', 't3']
        
        self.a.most_used_word = 'hashtag'
        self.a.load_related_tweets()
        
        mock_twitter.search.assert_called_with('hashtag')
        self.assertEquals(len(self.a.tweets), 3)

if __name__ == '__main__':
    unittest.main()
