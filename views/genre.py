from flask_restx import Resource, Namespace

from implemented import genre_service, genres_schema, genre_schema

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre), 200
