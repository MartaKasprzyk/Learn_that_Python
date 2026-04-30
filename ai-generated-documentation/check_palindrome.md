![Capgemini Logo](https://www.capgemini.com/wp-content/themes/capgemini2020/assets/images/logo.svg)

### Make it real.

---
## check_palindrome.py

**1. Overview:**

This Python script determines if a given text string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward. The script takes user input, processes it to remove spaces and convert it to lowercase, then compares the processed text with its reversed counterpart. Finally, it returns `True` if the text is a palindrome and `False` otherwise.

**2. Package/module name:** None (This is a standalone script)

**3. Class/file name:** check_palindrome.py

**4. Detailed Documentation:**

   - **Function: `check_palindrome()`**
     - **Description:** This function checks if the input text is a palindrome.
     - **Parameters:** 
       - None
     - **Return Values:** 
       - `True`: If the input text is a palindrome.
       - `False`: If the input text is not a palindrome.
     - **Important Logic:**
       1. Takes user input using `input("Enter your text: ")`.
       2. Converts the input to lowercase using `.lower()`.
       3. Removes spaces from the input using `.replace(" ", "")`.
       4. Reverses the processed text using slicing `[::-1]`.
       5. Compares the processed text with its reversed counterpart. If they are equal, it returns `True`; otherwise, it returns `False`.

**5. Pseudo Code:**

```
// Function: check_palindrome()

  1. Prompt user to enter text: "Enter your text: "
  2. Read user input and store it in variable 'text'.
  3. Convert 'text' to lowercase: 'text.lower()'.
  4. Remove spaces from 'text': 'text.replace(" ", "")'.
  5. Reverse the processed 'text': 'text[::-1]'.
  6. Compare the processed 'text' with its reversed counterpart.
     - If they are equal, return True (palindrome).
     - Otherwise, return False (not a palindrome). 
```



**Dependencies and Libraries:**

* This script relies on built-in Python libraries for input/output (`input()`, `print()`), string manipulation (`lower()`, `replace()`), and slicing (`[::-1]`). No external libraries are required.


Let me know if you have any other questions or need further clarification!