import article_fetcher
import article_analytics
import tag_analytics
from tag import Tag
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="This tool analyzes the popularity of your DEV.to posts")
    parser.add_argument('--api-key', action="store", dest="api_key", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    api_key = parse_arguments().api_key
    articles = article_fetcher.get_articles_from_dev(api_key)
    print("Article analytics")
    print("=================")
    print("Number of your articles: {}".format(len(articles)))
    print("Number of your views: {}".format(article_analytics.get_total_views(articles)))
    print("Number of reactions received: {}".format(article_analytics.get_total_reactions(articles)))
    print("Number of comments received: {}".format(article_analytics.get_total_comments(articles)))
    print("")
    print("Percentage of all views of your most viewed article: {:.2f}%".format(
        article_analytics.get_part_of_most_viewed_article_out_of_total_views(articles) * 100))
    print("Percentage of all reactions of your article with most reactions: {:.2f}%".format(
        article_analytics.get_part_of_article_with_most_reactions_out_of_total_reaction(articles) * 100))
    print("Percentage of all comments of your article with most comments: {:.2f}%".format(
        article_analytics.get_part_of_article_with_most_comments_out_of_total_reaction(articles) * 100))
    print("")
    print("Percentage of articles giving the {}% of all views: {:.2f}%".format(80,
                                                                               article_analytics.get_ratio_of_articles_giving_top_n_percent_of_views(
                                                                                   articles,
                                                                                   80) * 100))
    print("Percentage of articles giving the {}% of all views: {:.2f}%".format(95,
                                                                               article_analytics.get_ratio_of_articles_giving_top_n_percent_of_views(
                                                                                   articles,
                                                                                   95) * 100))
    print("Percentage of articles giving the {}% of all reactions: {:.2f}%".format(80,
                                                                                   article_analytics.get_ration_of_articles_giving_top_n_percent_of_reactions(
                                                                                       articles,
                                                                                       80) * 100))
    print("Percentage of articles giving the {}% of all reactions: {:.2f}%".format(95,
                                                                                   article_analytics.get_ration_of_articles_giving_top_n_percent_of_reactions(
                                                                                       articles,
                                                                                       95) * 100))
    print("Percentage of articles giving the {}% of all comments: {:.2f}%".format(80,
                                                                                  article_analytics.get_ratio_of_articles_giving_top_n_percent_of_comments(
                                                                                      articles,
                                                                                      80) * 100))
    print("Percentage of articles giving the {}% of all comments: {:.2f}%".format(95,
                                                                                  article_analytics.get_ratio_of_articles_giving_top_n_percent_of_comments(
                                                                                      articles,
                                                                                      95) * 100))

    tags = []
    for article in articles:
        for tagName in article.tags:
            tagFound = False
            tagToUse = None
            for tag in tags:
                if tag.name == tagName:
                    tagFound = True
                    tagToUse = tag

            if not tagFound:
                newTag = Tag(tagName)
                tagToUse = newTag
                tags.append(newTag)
            tagToUse.register_article(article)

    print("")
    print("")
    print("Tag analytics")
    print("=================")
    print("Your most viewed tag is: {} ({} views)".format(tag_analytics.get_tag_with_most_views(tags).name, tag_analytics.get_tag_with_most_views(tags).views))
    print("Your tag with the most reactions is: {} ({} reactions)".format(tag_analytics.get_tags_with_most_comments(tags).name, tag_analytics.get_tag_with_most_reactions(tags).reactions))
    print("Your tag with most comments is: {} ({} comments)".format(tag_analytics.get_tag_with_most_reactions(tags).name, tag_analytics.get_tags_with_most_comments(tags).comments))
    print("")
    print("Your tag with highest views per article ratio is: {} ({} views / article)".format(tag_analytics.get_most_views_per_article_tag(tags).name, tag_analytics.get_most_views_per_article_tag(tags).get_views_per_article()))
    print("Your tag with highest reactions per article ratio is: {} ({} reactions / article)".format(tag_analytics.get_most_reactions_per_article_tag(tags).name, tag_analytics.get_most_reactions_per_article_tag(tags).get_reactions_per_article()))
    print("Your tag with highest comments per article ratio is: {} ({} comments / article)".format(tag_analytics.get_most_comments_per_article_tag(tags).name, tag_analytics.get_most_comments_per_article_tag(tags).get_comments_per_article()))
