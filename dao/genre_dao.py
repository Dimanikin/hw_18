from .model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = self.session.query(Genre).all()
        return genres

    def get_one(self, gid):
        genre = self.session.query(Genre).get(gid).all()
        return genre
