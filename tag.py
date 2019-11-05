class Tag:

    def __init__(self, name, views=None, reactions=None, comments=None, articles=None):
        self.name = name
        self.views = views or 0
        self.reactions = reactions or 0
        self.comments = comments or 0
        self.articles = articles or []

    def get_views_per_article(self):
        return self.views / len(self.articles)

    def get_comments_per_article(self):
        return self.comments / len(self.articles)

    def get_reactions_per_article(self):
        return self.reactions / len(self.articles)

    def register_article(self, article):
        if self.name in article.tags:
            self.views += article.views
            self.comments += article.comments
            self.reactions += article.reactions
            self.articles.append(article)

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        return self.name == other.name and \
               self.views == other.views and \
               self.reactions == other.reactions and \
               self.comments == other.comments and \
               self.articles == other.articles

    def __hash__(self) -> int:
        return super().__hash__()

    def __repr__(self):
        return "Tag(name={name}," \
               " views={views}," \
               " reactions={reactions}," \
               " comments={comments}," \
               " articles={articles})".format(name=self.name,
                                              views=self.views,
                                              reactions=self.reactions,
                                              comments=self.comments,
                                              articles=self.articles)
