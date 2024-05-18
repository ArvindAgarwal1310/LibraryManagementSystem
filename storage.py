import json
import os


class Storage:
    """
        A class to handle file-based JSON database operations.

        Attributes:
            DB_FILE (str): The path to the JSON database file.
            database (dict): The database loaded from the JSON file.
            table (str): The name of the table in the database.
        """
    # File-based database-JSON
    def __init__(self, table):
        """
                Initialize the Storage class with the specified table.

                Args:
                    table (str): The name of the table in the database.
                """
        self.DB_FILE = 'database.json'
        self.database = self.load_database()
        self.table=table

    def load_database(self):
        """
                Load the database from the JSON file.

                Returns:
                    dict: The database loaded from the JSON file.
                """
        if os.path.exists(self.DB_FILE):
            with open(self.DB_FILE, 'r') as file:
                return json.load(file)
        return {}

    def save_database(self, db):
        """
            Save the given database to the JSON file.

            Args:
                db (dict): The database to save.
        """
        with open(self.DB_FILE, 'w') as file:
            json.dump(db, file, indent=4)

    def add_record(self, record, unique_criteria):
        """
        Add a record to the table if it meets the unique criteria.

        Args:
            record (dict): The record to add.
            unique_criteria (dict): The criteria to ensure uniqueness.

        Returns:
            bool: True if the record was added, False if a conflict was found.
        """
        db = self.database
        if self.table not in db:
            db[self.table] = []

        # Check for uniqueness
        for existing_record in db[self.table]:
            if all(existing_record.get(k) == v for k, v in unique_criteria.items()):
                print("\n\nConflict found: A record with the same Primary key value already exists.\nTry a different ID")
                return False

        db[self.table].append(record)
        self.save_database(db)
        return True

    def get_records(self):
        """
                Get all records from the table.

                Returns:
                    list: A list of all records in the table.
                """
        db = self.database
        return db.get(self.table, [])

    def find_records_by_key(self, criteria):
        """
        Find records in a table where the key matches the value.

        Args:
            table (str): The name of the table to search in.
            key (str): The key to match.
            value (str/int/float): The value to match.

        Returns:
            list: A list of records that match the criteria.
        """
        db = self.database
        if self.table in db:
            def matches_criteria(record):
                return all(record.get(k) == v for k, v in criteria.items())

            return [record for record in db[self.table] if matches_criteria(record)]
        return []

    def modify_records(self, criteria, updates):
        """
        Modify records in a table that match the given criteria.

        Args:
            table (str): The name of the table to update records in.
            criteria (dict): A dictionary where keys are field names and values are the values to match.
            updates (dict): A dictionary of updates to apply to matching records.

        Returns:
            int: The number of records that were updated.
        """
        db = self.database
        if self.table not in db:
            return 0

        updated_count = 0

        for record in db[self.table]:
            if all(record.get(k) == v for k, v in criteria.items()):
                for key, value in updates.items():
                    record[key] = value
                updated_count += 1

        self.save_database(db)
        return updated_count

    def delete_records(self, criteria):
        """
        Delete records in a table that match the given criteria.

        Args:
            table (str): The name of the table to delete records from.
            criteria (dict): A dictionary where keys are field names and values are the values to match.

        Returns:
            int: The number of records that were deleted.
        """
        db = self.database
        if self.table not in db:
            return 0

        original_count = len(db[self.table])
        db[self.table] = [record for record in db[self.table] if not all(record.get(k) == v for k, v in criteria.items())]
        deleted_count = original_count - len(db[self.table])

        self.save_database(db)
        return deleted_count

