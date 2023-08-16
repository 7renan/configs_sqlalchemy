from sqlalchemy import text
from infra.db.settings.connection import DBConnectionHandler


with DBConnectionHandler() as db:
    session = db.session
    response = session.execute(text('SELECT * FROM roles'))
    print(response.all())

    