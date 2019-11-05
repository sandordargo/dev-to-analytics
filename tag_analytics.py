from tag import Tag


def get_tag_with_most_views(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.views)[0]


def get_tags_with_most_comments(tags):
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
