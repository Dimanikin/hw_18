from .model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = self.session.query(Director).all()
        return directors

    def get_one(self, gid):
        director = self.session.query(Director).get(gid).all()
        return director
