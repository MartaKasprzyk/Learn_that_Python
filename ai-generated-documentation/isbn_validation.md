![Capgemini Logo](https://www.capgemini.com/wp-content/themes/capgemini2020/assets/images/logo.svg)

### Make it real.

---
## isbn_validation.py Documentation

**1. Overview:**

This Python script defines a `Book` class that encapsulates information about a book, including its title, author, and ISBN. The script includes a validation function (`check_isbn`) to ensure that provided ISBNs adhere to the correct format and checksum calculation. 

**2. Package/module name:** None (This is a standalone script)

**3. Class/file name:** isbn_validation.py

**4. Detailed Documentation:**

   - **Class: `Book`**
     - **Description:** Represents a book object with attributes for title, author, and ISBN. It includes an initializer (`__init__`) to set these attributes and validate the provided ISBN using the `check_isbn` function.
     - **Parameters:** 
       - `title`: (string) The title of the book.
       - `author`: (string) The author of the book.
       - `isbn`: (string) The ISBN to be validated and stored.

   - **Method: `__init__(self, title, author, isbn)`**
     - **Description:** Initializes a new `Book` object. 
     - **Parameters:**
       - `title`: (string) The title of the book.
       - `author`: (string) The author of the book.
       - `isbn`: (string) The ISBN to be validated and stored.
     - **Return Values:** None
     - **Important Logic:**
       1. Sets the `title` and `author` attributes.
       2. Calls the `check_isbn` function to validate the provided `isbn`.
         - If `check_isbn` returns `True`, sets the `isbn` attribute.
         - If `check_isbn` returns `False`, raises a `ValueError` with the message "Invalid ISBN".

   - **Method: `check_isbn(isbn)`** (Static Method)
     - **Description:** Validates an ISBN string. 
     - **Parameters:**
       - `isbn`: (string) The ISBN to be validated.
     - **Return Values:** `True` if the ISBN is valid, `False` otherwise.
     - **Important Logic:**
       1. Removes hyphens from the `isbn` string.
       2. Converts the `isbn` to a list of integers.
       3. Checks the length of the `isbn`:
         - If it's 10 digits:
           - Calculates the checksum using a weighted sum algorithm.
           - Compares the calculated checksum with the last digit of the `isbn`.
           - Returns `True` if they match, `False` otherwise.
         - If it's 13 digits:
           - Separates even and odd digits.
           - Calculates the checksum using a weighted sum algorithm for both sets.
           - Compares the calculated checksum with the last digit of the `isbn`.
           - Returns `True` if they match, `False` otherwise.

   - **Method: `__str__(self)`**
     - **Description:** Defines how a `Book` object is represented as a string.
     - **Parameters:** None
     - **Return Values:** A formatted string containing the book's title, author, and ISBN.
     - **Important Logic:** Returns a string with the book's information in a readable format.

**5. Pseudo Code:**



```
// Class: Book

  1. Constructor (__init__):
    - Set `title` and `author` attributes to provided values.
    - Call `check_isbn(isbn)` to validate ISBN.
      - If valid, set `isbn` attribute.
      - If invalid, raise ValueError("Invalid ISBN").

  2. Method: check_isbn(isbn):
    - Remove hyphens from `isbn`.
    - Convert `isbn` to a list of integers.
    - Check length of `isbn`:
      - If 10 digits:
        - Calculate checksum using weighted sum algorithm for each digit.
        - Compare calculated checksum with last digit of `isbn`.
        - Return True if they match, False otherwise.
      - If 13 digits:
        - Separate even and odd digits into lists.
        - Calculate checksum using weighted sum algorithm for even and odd digits separately.
        - Compare calculated checksum with last digit of `isbn`.
        - Return True if they match, False otherwise.

  3. Method: __str__():
    - Return a formatted string containing title, author, and ISBN.



// Main Program Flow
  1. Create a Book object with sample data.
  2. Print the book object using the __str__ method. 
```


**Dependencies and Libraries:**

* **None:** This script does not rely on any external libraries. It uses built-in Python functionalities for string manipulation, list operations, and mathematical calculations.



