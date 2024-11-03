from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from contextlib import contextmanager
from helper.model import Base, Book, Schedule, Subject, Todo
from helper.logger import logger


class Database():

    def __init__(self):
        self.engine = create_engine('sqlite:///./db/database.db', echo=True)
        logger.info('Engine Created')
        self.session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        

    @contextmanager
    def get_session(self):
        """Creates and return a new session instance"""
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error("An error occurred while adding the user: %s", e)
            raise
        finally:
            session.close()

    
    def execute_query(self, query):
        """Execute a raw SQL Query"""
        with self.engine.connect() as connection:
            result = connection.execute(query)
            return result.fetchall()
