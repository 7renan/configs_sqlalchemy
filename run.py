from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from infra.db.settings.connection import DBConnectionHandler


# models
from infra.db.entities.filme import Filmes

# repositories
from infra.db.repositories.filme_repository import FilmesRepository

filmes_repo = FilmesRepository()

filmes = filmes_repo.get_filmes()

print(type(filmes[0]))

    