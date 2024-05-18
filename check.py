from storage import Storage
from book import book_management

class checkout_management:
    """
        A class to manage book check-out/check-in operations.

        Attributes:
            storage (Storage): An instance of the Storage class for database operations.

        Methods:
            __init__(): Initialize the CheckoutManagement class.
            checkout_book(user_id, isbn): Checkout a book for a user.
            checkin_book(user_id, isbn): Check-in a book for a user.
            user_specific_possessions(user_id): Get book possessions of a user.
    """
    def __init__(self):
        """
            Initialize the CheckoutManagement class with a Storage instance.
        """
        self.storage=Storage(table="Orders")
    def checkout_book(self,user_id, isbn):
        """
            Checkout a book for a user.
            Args:
                user_id (str): The ID of the user.
                isbn (str): The ISBN of the book.
            Returns:
                str: Confirmation message of book check-out or unavailability message.
        """
        book_availability=book_management().find_book(isbn=isbn)[0]["availabilty"]
        if(book_availability=='0'):
            return("\nBook Unavailable.\n")
        self.storage.add_record(record={"user_id": user_id, "isbn": isbn},unique_criteria={"user_id": user_id, "isbn": isbn})
        book_management().modify_book(isbn=isbn,availabilty="0")
        return "\n\nBook Checked-Out\n"

    def chechkin_book(self, user_id, isbn):
        """
            Check-in a book for a user.
            Args:
                user_id (str): The ID of the user.
                isbn (str): The ISBN of the book.
            Returns:
                str: Confirmation message of book check-in or incorrect user ID/ISBN message.
        """
        deleted_count=(self.storage.delete_records(criteria={"user_id": user_id, "isbn": isbn}))
        if(deleted_count<1):
            return ("\n\nUser id or ISBN is incorrect\n")
        book_management().modify_book(isbn=isbn, availabilty="1")
        return "\n\nBook Checked-in Successfully\n"

    def user_specific_possessions(self, user_id):
        """
            Get book possessions of a user.
            Args:
                user_id (str): The ID of the user.
            Returns:
                list: A list of book possessions of the user.
        """
        return (self.storage.find_records_by_key(criteria={"user_id":user_id}))
