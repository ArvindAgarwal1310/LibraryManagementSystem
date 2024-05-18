# Global list to store books
from storage import Storage
from utility import utils

class book_management:
    """
        A class to manage book-related operations.

        Attributes:
            storage (Storage): An instance of the Storage class for database operations.

        Methods:
            __init__(): Initialize the BookManagement class.
            add_book(title, author, isbn): Add a new book to the database.
            list_books(): List all books from the database.
            modify_book(isbn, title="", availability="1"): Modify book details in the database.
            delete_book(isbn): Delete a book from the database.
            find_book(isbn): Find a book by ISBN.
    """

    def __init__(self):
        """
            Initialize the BookManagement class with a Storage instance.
        """
        self.storage=Storage(table="Books")

    def add_book(self,title, author, isbn):
        """
            Add a new book to the database.

            Args:
                title (str): The title of the book.
                author (str): The author of the book.
                isbn (str): The ISBN of the book.

            Returns:
                int: 1 if the book was added successfully, -1 if a conflict was found.
        """
        current_time = utils().get_current_time()
        unique_criteria={"isbn": isbn}
        value=self.storage.add_record(record={"title": title, "author": author, "isbn": isbn, "availability": "1", "timestamp": current_time},unique_criteria=unique_criteria)
        if (not value):
            return -1
        return 1

    def list_books(self):
        """
            List all books from the database.
            Returns:
                list: A list of all books in the database.
        """
        records=self.storage.get_records()
        return records

    def modify_book(self, isbn, title="", availability="1"):
        """
            Modify book details in the database.
            Args:
                isbn (str): The ISBN of the book to modify.
                title (str): The new title of the book (optional).
                availability (str): The new availability status of the book (optional).
        """
        current_time = utils().get_current_time()
        criteria = {"isbn": isbn}
        updates={"timestamp":current_time}
        if (title != ""):
            updates["title"] = title
        if (availability != None):
            updates["availability"] = availability
        self.storage.modify_records(criteria=criteria, updates=updates)

    def delete_book(self, isbn):
        """
            Delete a book from the database.

            Args:
                isbn (str): The ISBN of the book to delete.
        """
        criteria={"isbn" :isbn}
        return self.storage.delete_records(criteria=criteria)

    def find_book(self, isbn):
        """
            Find a book by ISBN.

            Args:
                isbn (str): The ISBN of the book to find.

            Returns:
                list: A list of records matching the ISBN criteria.
        """
        criteria={"isbn" :isbn}
        return self.storage.find_records_by_key(criteria=criteria)

