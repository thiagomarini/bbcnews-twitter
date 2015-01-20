import unittest

from services import BlacklistedWordsProvider


class BlacklistedWordsProviderTest(unittest.TestCase):

        
    def test_load_blacklisted_words(self):

        blwp = BlacklistedWordsProvider()
        
        self.assertEquals(len(blwp.get_words()), 674)

if __name__ == '__main__':
    unittest.main()
