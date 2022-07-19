import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)


    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0


    def test_create(self):
        movie_d = {'name': 'new_name'}
        new_movie = self.movie_service.create(movie_d)
        assert new_movie.id is not None

    def test_update(self):
        res = self.movie_service.update(21)
        assert res

    def test_delete(self):
        res = self.movie_service.delete(21)
        assert res