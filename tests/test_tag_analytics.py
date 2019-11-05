import unittest
from article import Article
from tag import Tag
import tag_analytics


class TestTag(unittest.TestCase):
    def setUp(self):
        self.mostViewedTag = Tag("tagname1", views=700, reactions=70, comments=7)
        self.mostCommentedTag = Tag("tagname2", views=500, reactions=50, comments=10)
        self.mostReactedTag = Tag("tagname3", views=600, reactions=100, comments=6)
        self.tags = [self.mostViewedTag,
                     self.mostCommentedTag,
                     self.mostReactedTag
                     ]

    def test_get_tag_with_most_views(self):
        self.assertEqual(self.mostViewedTag, tag_analytics.get_tag_with_most_views(self.tags))

    def test_get_tag_with_most_comments(self):
        self.assertEqual(self.mostCommentedTag, tag_analytics.get_tags_with_most_comments(self.tags))

    def test_get_tag_with_most_reactions(self):
        self.assertEqual(self.mostReactedTag, tag_analytics.get_tag_with_most_reactions(self.tags))

    def test_get_views_per_tag(self):
        tag = Tag("tagname1")
        tag.register_article(Article('t', 300, 0, 0, None, ["tagname1"]))
        tag.register_article(Article('t', 500, 0, 0, None, ["tagname1"]))

        self.assertEqual(
            {tag: 400},
            tag_analytics.get_views_per_article_for_each_tag([tag])
        )

    def test_get_reactions_per_tag(self):
        tag = Tag("tagname1")
        tag.register_article(Article('t', 0, 6, 0, None, ["tagname1"]))
        tag.register_article(Article('t', 0, 8, 0, None, ["tagname1"]))

        self.assertEqual(
            {tag: 7},
            tag_analytics.get_reactions_per_article_for_each_tag([tag])
        )

    def test_get_comments_per_tag(self):
        tag = Tag("tagname1")
        tag.register_article(Article('t', 0, 0, 0, None, ["tagname1"]))
        tag.register_article(Article('t', 0, 0, 2, None, ["tagname1"]))

        self.assertEqual(
            {tag: 1},
            tag_analytics.get_comments_per_article_for_each_tag([tag])
        )

    def test_get_most_views_per_article_tag(self):
        most_popular_tag = Tag("tagname1")
        most_popular_tag.register_article(Article('t', 300, 0, 0, None, ["tagname1"]))
        most_popular_tag.register_article(Article('t', 500, 0, 0, None, ["tagname1"]))

        other_tag = Tag("tagname2")
        other_tag.register_article(Article('t', 30, 0, 0, None, ["tagname2"]))
        other_tag.register_article(Article('t', 500, 0, 0, None, ["tagname2"]))

        self.assertEqual(
            most_popular_tag,
            tag_analytics.get_most_views_per_article_tag([most_popular_tag, other_tag])
        )

    def test_get_most_reactions_per_article_tag(self):
        most_popular_tag = Tag("tagname1")
        most_popular_tag.register_article(Article('t', 0, 6, 0, None, ["tagname1"]))
        most_popular_tag.register_article(Article('t', 0, 8, 0, None, ["tagname1"]))

        other_tag = Tag("tagname2")
        other_tag.register_article(Article('t', 0, 2, 0, None, ["tagname2"]))
        other_tag.register_article(Article('t', 0, 8, 0, None, ["tagname2"]))

        self.assertEqual(
            most_popular_tag,
            tag_analytics.get_most_reactions_per_article_tag([most_popular_tag, other_tag])
        )

    def test_get_most_comments_per_article_tag(self):
        most_popular_tag = Tag("tagname1")
        most_popular_tag.register_article(Article('t', 0, 0, 3, None, ["tagname1"]))
        most_popular_tag.register_article(Article('t', 0, 0, 3, None, ["tagname1"]))

        other_tag = Tag("tagname2")
        other_tag.register_article(Article('t', 0, 0, 3, None, ["tagname2"]))
        other_tag.register_article(Article('t', 0, 0, 1, None, ["tagname2"]))

        self.assertEqual(
            most_popular_tag,
            tag_analytics.get_most_comments_per_article_tag([most_popular_tag, other_tag])
        )
