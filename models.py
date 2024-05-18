class model:
    """
       A class to handle model-related operations.

       Methods:
           table_print(data): Print data in a table format.

       """
    def __init__(self):
        pass

    def table_print(self,data):
        """
            Print data in a table format.
            Args:
                data (list of dict): The data to print in tabular form.
         """
        from tabulate import tabulate
        # Format data for tabulate
        table_data = [[value for value in record.values()] for record in data]
        headers = data[0].keys()  # Assuming all dictionaries have the same keys

        # Print table
        print("\n\nRESULT:\n")
        print(tabulate(table_data, headers, tablefmt='grid'))