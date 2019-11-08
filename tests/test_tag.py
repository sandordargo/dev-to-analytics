import unittest
from models.article import Article
from models.tag import Tag


class TestTagAnalytics(unittest.TestCase):
    def setUp(self):
        self.tags = [Tag("tagname1"),
                     Tag("tagname2"),
                     Tag("tagname3")
                     ]

    def test_article_of_tag_is_registered(self):
        article = Article("article", 100, 10, 1, None, ["tagname1"])
        self.tags[0].register_article(article)
        self.assertEqual(self.tags[0].views, 100)
        self.assertEqual(self.tags[0].reactions, 10)
        self.assertEqual(self.tags[0].comments, 1)
        self.assertEqual(self.tags[0].articles, [article])

    def test_article_of_different_tag_is_not_registered(self):
        article = Article("article", 100, 10, 1, None, ["tagname0"])
        self.tags[0].register_article(article)
        self.assertEqual(self.tags[0].views, 0)
        self.assertEqual(self.tags[0].reactions, 0)
        self.assertEqual(self.tags[0].comments, 0)
        self.assertEqual(len(self.tags[0].articles), 0)
