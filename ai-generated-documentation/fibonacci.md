![Capgemini Logo](https://www.capgemini.com/wp-content/themes/capgemini2020/assets/images/logo.svg)

### Make it real.

---
## fibonacci.py Documentation

**1. Overview:**

This Python script calculates the nth Fibonacci number using both recursive and iterative approaches. The user inputs a number 'n', and the script outputs the corresponding Fibonacci number calculated by both methods. 

**2. Package/module name:** None (This is a standalone script)

**3. Class/file name:** fibonacci.py

**4. Detailed Documentation:**

   - **Function: `fib_recursive(n)`**
     - **Description:** Calculates the nth Fibonacci number using a recursive approach.
     - **Parameters:** 
       - `n`: An integer representing the desired position in the Fibonacci sequence.
     - **Return Values:** 
       - The nth Fibonacci number as an integer. If the input is invalid, it returns an error message.
     - **Important Logic:**
       1.  **Error Handling:** Uses a `try...except` block to catch potential `ValueError` exceptions that might occur if the user inputs non-integer values. 
       2. **Base Cases:** Handles the base cases for n = 0 and n = 1, returning n directly.
       3. **Recursive Step:** For n > 1, it recursively calls itself with `n-1` and `n-2`, calculates the sum of the results, and returns the sum as the nth Fibonacci number.

   - **Function: `fib_iterative(n)`**
     - **Description:** Calculates the nth Fibonacci number using an iterative approach.
     - **Parameters:** 
       - `n`: An integer representing the desired position in the Fibonacci sequence.
     - **Return Values:** 
       - The nth Fibonacci number as an integer. If the input is invalid, it returns an error message.
     - **Important Logic:**
       1.  **Error Handling:** Uses a `try...except` block to catch potential `ValueError` exceptions that might occur if the user inputs non-integer values. 
       2. **Initialization:** Initializes variables `a` and `b` with the first two Fibonacci numbers (0 and 1).
       3. **Iteration:** Iterates from 0 to n-2 using a `for` loop. In each iteration:
         - Calculates the next Fibonacci number (`result`) as the sum of `a` and `b`.
         - Updates `a` to the value of `b`, and `b` to the calculated `result`.
       4. **Return:** After the loop completes, returns the final value of `b`, which represents the nth Fibonacci number.

   - **Variable: `num`**
     - **Description:** Stores the user's input as a string.


**5. Pseudo Code:**

```
// Function: fib_recursive(n)
  1. Check if input 'n' is an integer >= 0.
    - If not, return "Incorrect input. Input must be an integer >= 0."
  2. If n = 0 or n = 1, return n.
  3. Otherwise:
    - Calculate fib_recursive(n - 1) and fib_recursive(n - 2).
    - Return the sum of the two results.

// Function: fib_iterative(n)
  1. Check if input 'n' is an integer >= 0.
    - If not, return "Incorrect input. Input must be an integer >= 0."
  2. If n = 0 or n = 1, return n.
  3. Otherwise:
    - Initialize variables a = 0 and b = 1.
    - Iterate from i = 0 to n - 2:
      - Calculate result = a + b.
      - Update a = b and b = result.
    - Return b (the nth Fibonacci number).

// Main Program Flow
  1. Prompt the user to enter 'n'.
  2. Store the user's input in variable 'num'.
  3. Call fib_recursive(num) and print the result.
  4. Call fib_iterative(num) and print the result.



```

**Dependencies and Libraries:**

* **None:** This script does not rely on any external libraries or modules beyond Python's standard library. 


