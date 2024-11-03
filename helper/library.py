from helper.model import Book
from helper.db import Database
from helper.logger import logger

class LibraryManager():

    def __init__(self):
        self.db = Database()
        pass

    def get_books(self):
        with self.db.get_session() as session:
            return session.query(Book).order_by(Book.title).all()
        
    def add_books(self, book_data:dict) -> bool:
        '''Add new book to library'''
        if not isinstance(book_data, dict):
            logger.error("Invalid data type for book_data; %s", type(book_data))

        # mencoba memasukan data book
        try:
            new_book = Book(**book_data)
        except Exception as e:
            logger.error("Invalid data type for book_data: %s", type(book_data))
            return False

        with self.db.get_session() as session:
            try:
                session.add(new_book)
                session.commit()
                logger.info('Adding new Book: %s', new_book)
                return True
            except Exception as e:
                session.rollback()
                logger.error("An error accured %s", e)
                return False
            
    def delete_book(self, book_id:int) -> bool:
        '''Deleting book from library'''
        with self.db.get_session() as session:
            try:
                session.query(Book).filter(Book.id == book_id).delete(synchronize_session='evaluate')
                logger.info('Success deleting books')
                return True
            except Exception as e:
                logger.error('An error occured: %s', e)
                return False
