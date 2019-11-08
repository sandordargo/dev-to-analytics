def analyse(articles):
    print("Article analytics")
    print("=================")
    print("Number of your articles: {}".format(len(articles)))
    print("Number of your views: {}".format(get_total_views(articles)))
    print("Number of reactions received: {}".format(get_total_reactions(articles)))
    print("Number of comments received: {}".format(get_total_comments(articles)))
    print("")
    print("Percentage of all views of your most viewed article: {:.2f}%".format(
        get_part_of_most_viewed_article_out_of_total_views(articles) * 100))
    print("Percentage of all reactions of your article with most reactions: {:.2f}%".format(
        get_part_of_article_with_most_reactions_out_of_total_reaction(articles) * 100))
    print("Percentage of all comments of your article with most comments: {:.2f}%".format(
        get_part_of_article_with_most_comments_out_of_total_reaction(articles) * 100))
    print("")
    print("Percentage of articles giving the {}% of all views: {:.2f}%".format(80,
                                                                               get_ratio_of_articles_giving_top_n_percent_of_views(
                                                                                   articles,
                                                                                   80) * 100))
    print("Percentage of articles giving the {}% of all views: {:.2f}%".format(95,
                                                                               get_ratio_of_articles_giving_top_n_percent_of_views(
                                                                                   articles,
                                                                                   95) * 100))
    print("Percentage of articles giving the {}% of all reactions: {:.2f}%".format(80,
                                                                                   get_ration_of_articles_giving_top_n_percent_of_reactions(
                                                                                       articles,
                                                                                       80) * 100))
    print("Percentage of articles giving the {}% of all reactions: {:.2f}%".format(95,
                                                                                   get_ration_of_articles_giving_top_n_percent_of_reactions(
                                                                                       articles,
                                                                                       95) * 100))
    print("Percentage of articles giving the {}% of all comments: {:.2f}%".format(80,
                                                                                  get_ratio_of_articles_giving_top_n_percent_of_comments(
                                                                                      articles,
                                                                                      80) * 100))
    print("Percentage of articles giving the {}% of all comments: {:.2f}%".format(95,
                                                                                  get_ratio_of_articles_giving_top_n_percent_of_comments(
                                                                                      articles,
                                                                                      95) * 100))
    print("")
    print("")


def get_total_views(articles):
    return sum(article.views for article in articles)


def get_total_reactions(articles):
    return sum(article.reactions for article in articles)


def get_total_comments(articles):
    return sum(article.comments for article in articles)


def get_top_n_views(articles, top_n):
    articles.sort(key=lambda article: article.views, reverse=True)
    return articles[:top_n]


def get_top_n_comments(articles, top_n):
    articles.sort(key=lambda article: article.comments, reverse=True)
    return articles[:top_n]


def get_top_n_reactions(articles, top_n):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    return articles[:top_n]


def get_ratio_of_articles_giving_top_n_percent_of_views(articles, top_n):
    articles.sort(key=lambda article: article.views, reverse=True)
    return get_ratio_of_articles_giving_top_n_percent_of(get_total_views, articles, top_n)


def get_ratio_of_articles_giving_top_n_percent_of_comments(articles, top_n):
    articles.sort(key=lambda article: article.comments, reverse=True)
    return get_ratio_of_articles_giving_top_n_percent_of(get_total_comments, articles, top_n)


def get_ration_of_articles_giving_top_n_percent_of_reactions(articles, top_n):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    return get_ratio_of_articles_giving_top_n_percent_of(get_total_reactions, articles, top_n)


def get_ratio_of_articles_giving_top_n_percent_of(function, articles, top_n):
    total = function(articles)
    number_of_articles = 1
    current_ratio = function(articles[:number_of_articles]) / total
    while current_ratio < top_n / 100:
        number_of_articles += 1
        current_ratio = function(articles[:number_of_articles]) / total
    return number_of_articles / len(articles)


def get_part_of_most_viewed_article_out_of_total_views(articles):
    articles.sort(key=lambda article: article.views, reverse=True)
    return articles[0].views / get_total_views(articles)


def get_part_of_article_with_most_reactions_out_of_total_reaction(articles):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    return articles[0].reactions / get_total_reactions(articles)


def get_part_of_article_with_most_comments_out_of_total_reaction(articles):
    articles.sort(key=lambda article: article.comments, reverse=True)
    return articles[0].comments / get_total_comments(articles)
