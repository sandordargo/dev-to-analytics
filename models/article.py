class Article:

    def __init__(self, title, views, reactions, comments, creation_time=None, tags=None):
        self.title = title
        self.views = views
        self.reactions = reactions
        self.comments = comments
        self.creation_time = creation_time
        self.tags = tags or []

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        return self.title == other.title and \
               self.views == other.views and \
               self.reactions == other.reactions and \
               self.comments == other.comments and \
               self.creation_time == other.creation_time and \
               self.tags == other.tags

    def __repr__(self):
        return "Article(title={title}," \
               " views={views}," \
               " reactions={reactions}," \
               " comments={comments}," \
               " creation_time={creation_time}" \
               " tags={tags})\n".format(title=self.title,
                                        views=self.views,
                                        reactions=self.reactions,
                                        comments=self.comments,
                                        creation_time=self.creation_time,
                                        tags=self.tags)


