from datetime import datetime

class utils:
    """
       A class to handle utility operations.

       Methods:
           get_current_time(): Get the current time.
           main_menu(): Display the main menu.
           books_operations(): Display book operations menu.
           user_operations(): Display user operations menu.
           order_operations(): Display order operations menu.
    """
    def __init__(self):
        pass
    def get_current_time(self):
        """
        Get the current time.

        Returns:
            str: The current time in the format HH:MM:SS.
        """
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    def main_menu(self):
        """
            Display the main menu.
            Returns:
                str: The user's choice from the main menu.
        """
        print("\nLibrary Management System\n")
        print("1. Books Operations")
        print("2. User Operations")
        print("3. Order Operation: Check-out/Check-in")
        print("4. Exit\n\n")
        choice = input("Enter choice: ")
        return choice

    def Books_operations(self):
        """
            Display book operations menu.

            Returns:
                str: The user's choice from the book operations menu.
        """
        print("\nBooks Operations")
        print("1. Add Book")
        print("2. List Books")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Update Book")
        print("0: Main Menu")
        choice = input("Enter choice: ")
        return choice

    def User_operations(self):
        """
            Display user operations menu.
            Returns:
                str: The user's choice from the user operations menu.
        """
        print("\nUser Operations")
        print("1. Add User")
        print("2. List Users")
        print("3. Delete User")
        print("4. Search User")
        print("5. Update User Name")
        print("6. Check Book Possessions of user")
        print("0: Main Menu")
        choice = input("Enter choice: ")
        return choice

    def Order_operations(self):
        """
            Display order operations menu.
            Returns:
                str: The user's choice from the order operations menu.
        """
        print("\nBooks Operations")
        print("1. Check-out Book")
        print("2. Check-in Book")
        print("0: Main Menu")
        choice = input("Enter choice: ")
        return choice