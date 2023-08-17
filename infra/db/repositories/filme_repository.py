from sqlalchemy.exc import SQLAlchemyError
from infra.db.settings.connection import DBConnectionHandler

# entitites
from infra.db.entities.filme import Filmes

class FilmesRepository:
    """ class repository filmes """

    def get_filmes(self):
        with DBConnectionHandler() as db:
          try:
             session = db.session
             filmes = session.query(Filmes).all()
             return filmes
          except SQLAlchemyError as e:
             print(e)