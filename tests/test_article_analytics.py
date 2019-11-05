import unittest
from article import Article
import article_analytics


class TestArticleAnalytics(unittest.TestCase):
    def setUp(self):
        self.articles = [Article("title1", 100, 10, 1, None),
                         Article("title2", 900, 90, 9, None),
                         Article("title3", 300, 30, 3, None),
                         Article("title4", 400, 40, 4, None),
                         Article("title5", 500, 50, 5, None),
                         Article("title6", 600, 60, 6, None),
                         Article("title7", 700, 70, 7, None),
                         Article("title8", 800, 80, 8, None),
                         Article("title9", 200, 20, 2, None),
                         Article("title10", 1000, 100, 10, None),
                         ]

    def test_total_views(self):
        self.assertEqual(5500, article_analytics.get_total_views(self.articles))

    def test_total_reactions(self):
        self.assertEqual(550, article_analytics.get_total_reactions(self.articles))

    def test_total_comments(self):
        self.assertEqual(55, article_analytics.get_total_comments(self.articles))

    def test_top_1_views(self):
        self.assertEqual([Article("title10", 1000, 100, 10, None)], article_analytics.get_top_n_views(self.articles, 1))

    def test_top_3_views(self):
        self.assertEqual([Article("title10", 1000, 100, 10, None),
                          Article("title2", 900, 90, 9, None),
                          Article("title8", 800, 80, 8, None),
                          ], article_analytics.get_top_n_views(self.articles, 3))

    def test_top_1_comments(self):
        self.assertEqual([Article("title10", 1000, 100, 10, None)], article_analytics.get_top_n_comments(self.articles, 1))

    def test_top_3_comments(self):
        self.assertEqual([Article("title10", 1000, 100, 10, None),
                          Article("title2", 900, 90, 9, None),
                          Article("title8", 800, 80, 8, None),
                          ], article_analytics.get_top_n_comments(self.articles, 3))

    def test_top_1_reactions(self):
        self.assertEqual([Article("title10", 1000, 100, 10, None)], article_analytics.get_top_n_reactions(self.articles, 1))

    def test_top_3_reactions(self):
        self.assertEqual([Article("title10", 1000, 100, 10, None),
                          Article("title2", 900, 90, 9, None),
                          Article("title8", 800, 80, 8, None),
                          ], article_analytics.get_top_n_reactions(self.articles, 3))

    def test_ratio_of_articles_giving_80_percent_views(self):
        self.assertEqual(0.6, article_analytics.get_ratio_of_articles_giving_top_n_percent_of_views(self.articles, 80))


    def test_ratio_of_articles_giving_80_percent_comments(self):
        self.assertEqual(0.6, article_analytics.get_ratio_of_articles_giving_top_n_percent_of_comments(self.articles, 80))


    def test_ratio_of_articles_giving_80_percent_reactions(self):
        self.assertEqual(0.6, article_analytics.get_ration_of_articles_giving_top_n_percent_of_reactions(self.articles, 80))
