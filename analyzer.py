from tools import article_analytics, tag_analytics, article_fetcher
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="This tool analyzes the popularity of your DEV.to posts")
    parser.add_argument('--api-key', action="store", dest="api_key", required=True)
    return parser.parse_args()


def analyze(api_key):
    articles = article_fetcher.get_articles_from_dev(api_key)
    article_analytics.analyse(articles)
    tags = tag_analytics.get_tags_from_articles(articles)
    tag_analytics.analyze(tags)


if __name__ == "__main__":
    api_key = parse_arguments().api_key
    analyze(api_key)
