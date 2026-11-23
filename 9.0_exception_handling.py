"""Exercise 9.0 — Surviving what you did not expect

1. What goes in?
The user enters a value that should be a number.

2. What happens to it?
The program tries to convert the input to a float.
Then it divides 100 by this number.

3. What comes out?
The program shows the result if the input is valid.
If something goes wrong, it shows a clear error message and keeps running.

4. Which two different failures can happen here, and should they produce the same message?
The user can enter zero, which causes a division by zero error.
The user can also enter text or an empty line, which causes a conversion error.
They should not have the same message because the problems are different.
"""

# Catching each error separately is better because the user gets a precise message
# and knows exactly what they need to fix.

attempts = 0
max_attempts = 4

# Keep asking until the user gives a valid number or reaches the attempt limit.
while attempts < max_attempts:
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        result = 100 / number

    except ValueError:
        print("Please enter a valid number.")
        attempts += 1
        continue

    except ZeroDivisionError:
        print("Zero is not allowed because division by zero is impossible.")
        attempts += 1
        continue

    print("Result:", result)
    break

# Stop cleanly if all attempts were invalid.
if attempts == max_attempts:
    print("Too many invalid attempts. Program ended safely.")

# Check it yourself:
# Normal number, for example 4: the program prints Result: 25.0.
# Zero: the program shows the division by zero message and asks again.
# "abc": the program shows the invalid number message and asks again.
# Empty line: the program shows the invalid number message and asks again.
# None of these tests crash the program.