![Capgemini Logo](https://www.capgemini.com/wp-content/themes/capgemini2020/assets/images/logo.svg)

### Make it real.

---
## dice_roll.py Documentation

**1. Overview:**

This Python script simulates rolling multiple dice with customizable parameters. The user inputs a string representing the desired dice roll, following a specific format (e.g., "2D6+5"). The script then parses this input, determines the number of dice to roll, the type of dice, and any modifications to apply. Finally, it generates random dice rolls, applies the modifications, and prints the total result.

**2. Package/module name:** None (This is a standalone script)

**3. Class/file name:** dice_roll.py

**4. Detailed Documentation:**

   - **Function: `dice_roll()`**
     - **Description:** This function handles the entire dice rolling process, from user input to result calculation and output.
     - **Parameters:** None
     - **Return Values:** None (Prints the result directly)
     - **Important Logic:**
       1. Prints instructions on how to format the dice code input.
       2. Prompts the user for their dice code using `input()`.
       3. Converts the input to uppercase using `.upper()` for case-insensitive processing.
       4. Splits the input string by "D" using `.split("D")` to separate the number of rolls, dice type, and modification.
       5. Uses a `try...except` block to handle potential `ValueError` exceptions that might occur during parsing or calculation.
       6. Extracts the number of rolls (`x`), dice type (`y`), and modification (`z`) from the split string using conditional statements and string manipulation.
       7. Validates the input by checking if:
         - "D" is present in the code (for valid dice format).
         - `x` is greater than or equal to 1.
         - `y` is a valid dice type (3, 4, 6, 8, 10, 12, 20, 100).
       8. If any validation fails, prints an error message and exits the function.
       9. Generates a list of random dice rolls using `random.randint(1, y)` for each roll specified by `x`.
       10. Calculates the final result by summing the rolls and adding the modification (`z`).
       11. Prints the calculated result.

**5. Pseudo Code:**

```
// Function: dice_roll()

  1. Display instructions on how to format dice code input.
  2. Prompt user for dice code input.
  3. Convert input to uppercase.
  4. Split input string by "D".
  5. Try:
     - Check if "D" is present in the input (valid dice format).
     - Extract number of rolls (x), dice type (y), and modification (z) from split string.
     - Validate:
       - x >= 1
       - y is a valid dice type (3, 4, 6, 8, 10, 12, 20, 100).
     - If any validation fails, print error message and exit function.
     - Generate list of random dice rolls using `random.randint(1, y)` for each roll specified by x.
     - Calculate final result: sum of rolls + z.
     - Print the calculated result.
   6. Except ValueError:
     - Print "Invalid dice" error message.

```



**Dependencies and Libraries:**

* **random:** This Python library is used to generate random numbers for the dice rolls. Equivalent libraries in other languages include:
    * Java: `java.util.Random`
    * C++: `<random>` header
    * JavaScript: `Math.random()`


Let me know if you have any further questions or need more details about specific aspects of the code!