# LibraryManagementSystem
The Library Management System is a Python-based application designed to manage the operations of a library efficiently. It provides functionalities for adding, modifying, and deleting books, managing user information, and handling book check-out and check-in processes.

Documentation and usage: https://mango-fish-bf0.notion.site/Library-Management-System-Arvind-Agarwal-86fbf36937e4445f9f78ade13dd9f556?pvs=4
# Library Management System-Arvind Agarwal

## Introduction

The Library Management System is a Python-based application designed to manage the operations of a library efficiently. It provides functionalities for adding, modifying, and deleting books, managing user information, and handling book check-out and check-in processes.

## Purpose

The purpose of this application is to streamline the management of library resources and improve the overall user experience for both librarians and patrons. By automating various tasks such as book management, user registration, and order processing, the system aims to optimize library operations and enhance accessibility to library services.

## Features

- **Book Management**: Add, list, modify, search, and delete books from the library inventory.
- **User Management**: Add, list, modify, search and delete user information including user ID and name.
- **Checkout and Check-in**: Facilitate the process of checking out and checking in books for library users.
- **Data Persistence**: Utilize file-based database storage -JSON to store and retrieve library data.
- **Timestamp Tracking**: Record timestamps for various operations to track the history of changes.
- **Command-Line Interface**: Interact with the system through a user-friendly command-line interface.

## Usage Instructions

1. **Installation**:
    - Clone the repository: `git clone https://github.com/ArvindAgarwal1310/LibraryManagementSystem.git`
    - Navigate to the project directory: `cd [library-management-system](https://github.com/ArvindAgarwal1310/LibraryManagementSystem)`
2. **Running the Application**:
    - Execute the main script: `python main.py`
    - Follow the on-screen prompts to perform various library operations.
3. **Usage Example**:
    - To add a new book:
        
        ```
        1. Books Operations
        1. Add Book
        Enter title: <book-title>
        Enter author: <author-name>
        Enter ISBN: <ISBN>
        ```
        

## Database Schema

The database schema consists of two main tables: `Books` and `Users`. Below is the schema for each table:

### Books Table

| Column | Type | Description |
| --- | --- | --- |
| title | String | Title of the book |
| author | String | Author of the book |
| isbn | String | ISBN (International Standard Book Number) of the book |
| availability | String | Availability status of the book (0 for unavailable, 1 for available) |
| timestamp | String | Timestamp of the last update |

```jsx
Output
+---------------------+-------------+------------+---------------+---------------------+
| title               | author      |       isbn |   availabilty | timestamp           |
+=====================+=============+============+===============+=====================+
| Pride And Prejudice | Jane Austen |        101 |             0 | 2024-05-18 18:45:47 |
+---------------------+-------------+------------+---------------+---------------------+
| Harry Porter        | JK Rowling  |        123 |             1 | 2024-05-18 18:45:04 |
+---------------------+-------------+------------+---------------+---------------------+
| Test Book           | Test Author |     212528 |             1 | 2024-05-18 19:12:05 |
+---------------------+-------------+------------+---------------+---------------------+
| Modified Title      | Test Author |        103 |              0| 2024-05-18 19:23:55 |
+---------------------+-------------+------------+---------------+---------------------+
```

### Users Table

| Column | Type | Description |
| --- | --- | --- |
| name | String | Name of the user |
| user_id | String | Unique identifier for the user |
| timestamp | String | Timestamp of the last update |

```jsx
RESULT:

+----------------+-----------+---------------------+
| name           |   user_id | timestamp           |
+================+===========+=====================+
| Arvind Agarwal |      9618 | 2024-05-18 16:08:28 |
+----------------+-----------+---------------------+
```

### Orders Table

| Column | Type | Description |
| --- | --- | --- |
| isbn | String | ISBN (International Standard Book Number) of the book |
| user_id | String | Unique identifier for the user |

```jsx

+-----------+--------+
|   user_id |   isbn |
+===========+========+
|      9618 |    101 |
+-----------+--------+
|      9618 |    103 |
+-----------+--------+
```

## Class Overview

### Storage

- **Purpose**: Handles database operations for storing and retrieving library data.

### BookManagement

- **Purpose**: Manages book-related operations such as adding, listing, modifying, and deleting books.

### UserManagement

- **Purpose**: Manages user-related operations such as adding, listing, modifying, and deleting user information.

### CheckoutManagement

- **Purpose**: Manages book check-out and check-in operations for library users based on availability of specified book.

### Utils

- **Purpose**: Provides utility functions such as obtaining the current time, creating command flow.

## Testing

Unit testing is done on the appication:
https://github.com/ArvindAgarwal1310/LibraryManagementSystem/blob/main/Unit_test.py

```jsx
Testing started at 19:29 ...
Launching unittests with arguments python -m unittest C:/Users/aagar/ReStructured_LibraryManagementSystem/unit_test.py in C:\Users\aagar\ReStructured_LibraryManagementSystem

Ran 9 tests in 0.068s

OK

Process finished with exit code 0

```
