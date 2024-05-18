import random
import unittest
from unittest.mock import patch
from io import StringIO
from book import book_management
from user import user_management
from check import checkout_management
from utility import utils
from storage import Storage
"""
Run this file to test the application, it involved all the unit tests
"""

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.storage = Storage(table="TestTable")
        self.book_management = book_management()
        self.user_management = user_management()
        self.checkout_management = checkout_management()
        self.utils = utils()
        self.book_isbn=str(random.randint(199,2000))
        self.user_id = str(random.randint(199, 2000))

    def test_add_book(self):
        book_title = "Test Book"
        book_author = "Test Author"
        book_isbn = self.book_isbn
        result = self.book_management.add_book(book_title, book_author, book_isbn)
        self.assertEqual(result, 1)  # Check if book is added successfully

    def test_list_books(self):
        books = self.book_management.list_books()
        self.assertIsInstance(books, list)  # Check if list_books returns a list

    def test_modify_book(self):
        book_isbn = self.book_isbn
        self.book_management.add_book("Test Book", "Test Author", book_isbn)
        self.book_management.modify_book(book_isbn, title="Modified Title")
        modified_book = self.book_management.find_book(book_isbn)
        self.assertEqual(modified_book[0]["title"], "Modified Title")  # Check if book title is modified

    def test_find_book(self):
        book_isbn =self.book_isbn
        self.book_management.add_book("Test Book", "Test Author", book_isbn)
        found_book = self.book_management.find_book(book_isbn)
        self.assertEqual(found_book[0]["isbn"], book_isbn)  # Check if correct book is found

    def test_checkout_book(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.checkout_management.checkout_book(self.user_id, self.book_isbn)
            output=self.checkout_management.user_specific_possessions(self.book_isbn)
            self.assertIsInstance(output, list) # Check if book checkout works for available book

    def test_checkin_book(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.checkout_management.chechkin_book(self.user_id, self.book_isbn)
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")  # Check if book check-in works for user ID or ISBN

    def test_user_specific_possessions(self):
        user_possessions = self.checkout_management.user_specific_possessions(self.user_id)
        self.assertIsInstance(user_possessions, list)  # Check if user's possessions are returned as a list

    def test_get_current_time(self):
        current_time = self.utils.get_current_time()
        self.assertIsInstance(current_time, str)  # Check if current time is returned as a string

    def test_delete_book(self):
        book_isbn =self.book_isbn
        self.book_management.add_book("Test Book", "Test Author", book_isbn)
        book_initial=self.book_management.list_books()
        self.book_management.delete_book(book_isbn)
        books = self.book_management.list_books()
        self.assertEqual(len(books)<len(book_initial), 1)  # Check if book is deleted

if __name__ == "__main__":
    unittest.main()
