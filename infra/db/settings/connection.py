from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """ class that setting connection to database """
    
    def __init__(self) -> None:
        self.__connection_string = 'postgresql+psycopg2://{}:{}@localhost:5432/{}'.format(
            'postgres',
            'renan123123',
            'shipay_db'
        )
        self.__engine = self.create_engine()
        self.session = None


    def create_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()