from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from infra.db.settings.connection import DBConnectionHandler


# models
from infra.db.entities.filme import Filmes


with DBConnectionHandler() as db:
    try:
        session = db.session
        filmes = session.query(Filmes).all()
        print(filmes)
    except SQLAlchemyError as e:
        print("deu ruim", e)

    