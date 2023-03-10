from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service, movie_schema, movie_schema

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):

        data = {
                'director_id': request.args.get('director_id'),
                'genre_id': request.args.get('genre_id'),
                'year': request.args.get('year'),
            }

        all_movie = movie_service.filters(data)

        return movie_schema.dump(all_movie), 200

    def post(self):
        data = request.json
        new_movie = movie_service.add_movie(data)
        return '', 200, {'location': f'/movie/{new_movie.id}'}

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.update(data)

        return 'updated', 204

    def delete(self, mid):
        movie_service.del_movie(mid)
        return 'deleted', 204

