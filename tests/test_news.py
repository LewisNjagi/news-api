import unittest
from app.models import Source,Article

class SourceTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_source = Source("google-news","Google News","description")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

class ArticleTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_article = Article("description","https://news.google.com/__i/rss/rd/articles/CBMiK2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9anNiMFg0UzZuYlXSAQA?oc=5","2021-02-22T21:32:47Z","https://www.vanguardia.com/santander/guanenta/samuel-rodriguez-el-empresario-santandereano-mas-joven-del-pais-BN3429650")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))