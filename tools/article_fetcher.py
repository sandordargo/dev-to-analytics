import http.client
import json
from models import article


def get_articles_from_dev(api_key):
    connection = http.client.HTTPSConnection("dev.to")
    articles = []

    current_page = 1
    while current_page == 1 or len(articles_on_page) > 0:
        json_reply = get_json_data_from_page(connection, current_page, api_key)
        articles_on_page = extract_articles_from_json(json_reply)
        articles += articles_on_page
        current_page += 1
    return articles


def extract_articles_from_json(json_data):
    return [article.Article(article_as_json['title'],
                            article_as_json["page_views_count"],
                            article_as_json['positive_reactions_count'],
                            article_as_json['comments_count'],
                            article_as_json["published_timestamp"],
                            article_as_json["tag_list"])
            for article_as_json in json_data]


def get_json_data_from_page(connecion, page_index, api_key):
    connecion.request("GET", "/api/articles/me?page={}".format(page_index), headers={"api-key": api_key}, )
    response = connecion.getresponse()
    return json.loads(response.read().decode("utf-8"))
