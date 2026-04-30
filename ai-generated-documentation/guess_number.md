![Capgemini Logo](https://www.capgemini.com/wp-content/themes/capgemini2020/assets/images/logo.svg)

### Make it real.

---
## guess_number.py Documentation

**1. Overview:**

This Python script implements a simple number guessing game. The program generates a random number between 1 and 100 and prompts the user to guess it. The user receives feedback on whether their guess is too high, too low, or correct. The game continues until the user guesses the correct number.

**2. Package/module name:** None (This is a standalone script)

**3. Class/file name:** guess_number.py

**4. Detailed Documentation:**

   - **Function: `guess()`**
     - **Description:** This function handles the core logic of the guessing game. It generates a random number, prompts the user for guesses, and provides feedback until the correct number is guessed.
     - **Parameters:** None
     - **Return Values:** Returns a string "You win!" when the user guesses correctly.
     - **Important Logic:**
       1.  **Initialization:** Sets `guessed` to `False`, indicating that the game hasn't ended yet. Generates a random integer `x` between 1 and 100 using `random.randint(1, 100)`.
       2. **Guessing Loop:** Enters a `while` loop that continues until `guessed` becomes `True`.
         - **Input:** Prompts the user to enter their guess using `input("Guess the number: ")`.
         - **Error Handling:** Uses a `try...except` block to handle potential `ValueError` exceptions that might occur if the user enters non-integer input. If an error occurs, it prints "Please input integer only!".
         - **Type Check:** Checks if the input `n` is an integer using `type(n) is not int`. If not, it prints "It's not a number!" and continues to the next iteration of the loop.
         - **Comparison:** Compares the user's guess `n` with the random number `x`:
           - If `n < x`, prints "Too small!".
           - If `n > x`, prints "Too big!".
           - If `n == x`, sets `guessed` to `True`, indicating a correct guess, and returns the string "You win!".

   - **Variable: `x`**
     - **Description:** Stores the randomly generated number between 1 and 100.


**5. Pseudo Code:**

```
// Function: guess()

  1. Initialize variable 'guessed' to False.
  2. Generate a random integer 'x' between 1 and 100.
  3. While 'guessed' is False:
    - Prompt the user to enter their guess as 'n'.
    - Check if 'n' is an integer:
      - If not, print "Please input integer only!" and continue to the next iteration.
    - Compare 'n' with 'x':
      - If 'n' is less than 'x', print "Too small!".
      - If 'n' is greater than 'x', print "Too big!".
      - If 'n' equals 'x':
        - Set 'guessed' to True.
        - Return the string "You win!".

// Main Program Flow
  1. Call the function 'guess()'.
  2. Print the returned string from the 'guess()' function.



```


**Dependencies and Libraries:**

* **random:** This module is used for generating random numbers. Equivalent libraries in other languages include:
    - Java: `java.util.Random`
    - C++: `<random>` header
    - Python: `random` (already included)




