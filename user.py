from storage import Storage
from utility import utils
from check import checkout_management

class user_management:
    """
        A class to manage user-related operations.

        Attributes:
            storage (Storage): An instance of the Storage class for database operations.

        Methods:
            __init__(): Initialize the UserManagement class.
            add_user(name, user_id): Add a new user to the database.
            modify_user(name, user_id): Modify user details in the database.
            delete_user(user_id, name): Delete a user from the database.
            find_user(user_id): Find a user by user ID.
            all_users(): Get all users from the database.
            book_possessions(user_id): Get book possessions of a user.
        """
    def __init__(self):
        """
            Initialize the UserManagement class with a Storage instance.
        """
        self.storage = Storage(table="Users")

    def add_user(self, name, user_id):
        """
            Add a new user to the database.

            Args:
                name (str): The name of the user.
                user_id (str/int): The ID of the user.

            Returns:
                int: 1 if the user was added successfully, -1 if a conflict was found.
        """
        current_time=utils().get_current_time()
        unique_criteria={"user_id":user_id}
        value=self.storage.add_record(record={"name": name, "user_id": user_id, "timestamp":current_time},unique_criteria=unique_criteria)
        if(not value):
            return -1
        return 1
    def modify_user(self, name, user_id):
        """
            Modify user details in the database.

            Args:
                name (str): The new name of the user.
                user_id (str/int): The ID of the user.
        """
        current_time = utils().get_current_time()
        criteria={"user_id":user_id}
        updates={"name":name , "timestamp":current_time}
        self.storage.modify_records(criteria=criteria,updates=updates)

    def delete_user(self, user_id, name):
        """
            Delete a user from the database.
            Args:
                user_id (str/int): The ID of the user.
                name (str): The name of the user (optional).
        """
        criteria = {}
        if(user_id!=None):
            criteria["user_id"]=user_id
        if(name!=None):
            criteria["name"]=name
        self.storage.delete_records(criteria=criteria)

    def find_user(self, user_id):
        """
            Find a user by user ID.

            Args:
                user_id (str/int): The ID of the user to find.

            Returns:
                list: A list of records matching the user ID criteria.
        """
        criteria = {"user_id":user_id}
        return self.storage.find_records_by_key(criteria=criteria)

    def all_users(self):
        """
            Get all users from the database.
            Returns:
                list: A list of all users in the database.
        """
        return self.storage.get_records()

    def book_possessions(self,user_id):
        """
            Get book possessions of a user.
            Args:
                user_id (str/int): The ID of the user.
            Returns:
                list: A list of book possessions of the user.
        """
        return checkout_management().user_specific_possessions(user_id=user_id)


