from flask_restx import Resource, Namespace

from implemented import director_service, directors_schema, director_schema

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_by_id(did)
        return director_schema.dump(director), 200
