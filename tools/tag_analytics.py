from models.tag import Tag


def get_tags_from_articles(articles):
    tags = []
    for article in articles:
        for tag_name in article.tags:
            tag_found = False
            tag_to_use = None
            for tag in tags:
                if tag.name == tag_name:
                    tag_found = True
                    tag_to_use = tag

            if not tag_found:
                new_tag = Tag(tag_name)
                tag_to_use = new_tag
                tags.append(new_tag)
            tag_to_use.register_article(article)
    return tags


def analyze(tags):
    print("Tag analytics")
    print("=================")
    print("Your most viewed tag is: {} ({} views)".format(get_tag_with_most_views(tags).name,
                                                          get_tag_with_most_views(tags).views))
    print("Your tag with the most reactions is: {} ({} reactions)".format(
        get_tag_with_most_reactions(tags).name,
        get_tag_with_most_reactions(tags).reactions))
    print(
        "Your tag with most comments is: {} ({} comments)".format(get_tag_with_most_comments(tags).name,
                                                                  get_tag_with_most_comments(
                                                                      tags).comments))
    print("")
    print("Your tag with highest views per article ratio is: {} ({} views / article)".format(
        get_most_views_per_article_tag(tags).name,
        get_most_views_per_article_tag(tags).get_views_per_article()))
    print("Your tag with highest reactions per article ratio is: {} ({} reactions / article)".format(
        get_most_reactions_per_article_tag(tags).name,
        get_most_reactions_per_article_tag(tags).get_reactions_per_article()))
    print("Your tag with highest comments per article ratio is: {} ({} comments / article)".format(
        get_most_comments_per_article_tag(tags).name,
        get_most_comments_per_article_tag(tags).get_comments_per_article()))


def get_tag_with_most_views(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.views)[0]


def get_tag_with_most_comments(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.comments)[0]


def get_tag_with_most_reactions(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.reactions)[0]


def get_views_per_article_for_each_tag(tags):
    return {tag: tag.get_views_per_article() for tag in tags}


def get_reactions_per_article_for_each_tag(tags):
    return {tag: tag.reactions / len(tag.articles) for tag in tags}


def get_comments_per_article_for_each_tag(tags):
    return {tag: tag.comments / len(tag.articles) for tag in tags}


def get_most_views_per_article_tag(tags):
    return sorted(tags, key=Tag.get_views_per_article, reverse=True)[0]


def get_most_reactions_per_article_tag(tags):
    return sorted(tags, key=Tag.get_reactions_per_article, reverse=True)[0]


def get_most_comments_per_article_tag(tags):
    return sorted(tags, key=Tag.get_comments_per_article, reverse=True)[0]
