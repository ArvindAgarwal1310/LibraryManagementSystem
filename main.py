# This is a deliberately poorly implemented main script for a Library Management System.
#I have implemented OOPs development and the application is functional now
from book import book_management
from user import user_management
from check import checkout_management
from utility import utils
from models import model

class Library:
    """
       A class to manage the Library operations.

       Attributes:
           utility_obj (Utils): An instance of the Utils class for utility operations.
           model (Model): An instance of the Model class for table printing.

       Methods:
           book_request_handler(book_choice): Handle book-related user requests.
           user_request_handler(user_choice): Handle user-related user requests.
           order_request_handler(order_choice): Handle order-related user requests.
           main(): Main function to run the Library Management System.
    """
    def __init__(self):
        """
            Initialize the Library class with instances of utility classes.
        """
        self.utility_obj= utils()
        self.model=model()

    def book_request_handler(self, book_choice):
        """
            Handle book-related user requests.

            Args:
                book_choice (str): The choice made by the user for book-related operations.
        """
        book_management_obj= book_management()
        if book_choice == '0':
            self.utility_obj.main_menu()
        if book_choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            response=book_management_obj.add_book(title, author, isbn)
            if(response!=-1):
                print("\n\nBOOK ADDED.\n")
        elif book_choice=='2':
            data = book_management_obj.list_books()
            if len(data)<1:
                print("\n\nNO BOOKS AVAIlABLE.")
                return 1
            self.model.table_print(data=data)
        elif book_choice == '3':
            isbn=input("Enter isbn : ")
            response=book_management_obj.delete_book(isbn=isbn)
            if(response<1):
                print("\n\nNo Book Found.\n")
                return 1
            print("\nBook Deleted Successfully")
        elif book_choice == '4':
            isbn = input("Enter isbn : ")
            data = book_management_obj.find_book(isbn=isbn)
            if(len(data)<1):
                print("\n\nNO BOOK FOUND.")
                return 1
            self.model.table_print(data=data)
        elif book_choice == '5':
            isbn = input("Enter isbn : ")
            title= input("Enter title: ")
            book_management_obj.modify_book(isbn=isbn,title=title)


    def user_request_handler(self, user_choice):
        """
            Handle user-related user requests.

            Args:
                user_choice (str): The choice made by the user for user-related operations.
        """
        user_management_obj = user_management()
        if user_choice=='0':
            self.utility_obj.main_menu()
        if user_choice == '1':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            response=user_management_obj.add_user(name=name, user_id=user_id)
            if(response!=-1):
                print("\n\nUSER ADDED.\n")
        elif user_choice=='2':
            data = user_management_obj.all_users()
            if len(data)<1:
                print("\n\nNO USER REGISTERED")
                return 1
            self.model.table_print(data=data)
        elif user_choice == '3':
            user_id=input("user id: ")
            user_management_obj.delete_user(user_id=user_id)
        elif user_choice == '4':
            user_id=input("user id: ")
            data = user_management_obj.find_user(user_id=user_id)
            if(len(data)<1):
                print("\n\nNO USER REGISTERED.\n")
                return 1
            self.model.table_print(data=data)
        elif user_choice=='5':
            user_id = input("user id: ")
            name = input("Enter new Name: ")
            user_management_obj.modify_user(user_id=user_id,name=name)
        elif user_choice=='6':
            user_id=input("Enter User_id: ")
            data = user_management_obj.book_possessions(user_id=user_id)
            if (len(data) < 1):
                print("\n\nUSER HAS NO BOOK WITH THEM.\n")
                return 1
            self.model.table_print(data=data)


    def order_request_handler(self, order_choice):
        """
            Handle order-related user requests.
            Args:
                order_choice (str): The choice made by the user for order-related operations.
        """
        checkout_management_obj=checkout_management()
        if order_choice == '0':
            self.utility_obj.main_menu()
        if order_choice == '1':
            user_id= input("Enter user_id: ")
            isbn = input("Enter ISBN: ")
            print(checkout_management_obj.checkout_book(user_id=user_id,isbn=isbn))
        elif order_choice=='2':
            user_id = input("Enter user_id: ")
            isbn = input("Enter ISBN: ")
            print(checkout_management_obj.chechkin_book(user_id=user_id,isbn=isbn))

    def main(self):
        """
            Main function to run the Library Management System.
        """
        while True:
            choice = self.utility_obj.main_menu()
            if choice == '1':
                book_choice=self.utility_obj.Books_operations()
                self.book_request_handler(book_choice=book_choice)
            elif choice == '2':
                user_choice=self.utility_obj.User_operations()
                self.user_request_handler(user_choice=user_choice)
            elif choice == '3':
                order_choice=self.utility_obj.Order_operations()
                self.order_request_handler(order_choice=order_choice)
            elif choice == '4':
                print("Exiting.\n\n")
                print("Thanks for visiting our Library.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    Library=Library()
    Library.main()
