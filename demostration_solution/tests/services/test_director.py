import pytest

from demostration_solution.service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)


    def test_get_one(self):
        director = self.director_service.get_one()
        assert director is not None