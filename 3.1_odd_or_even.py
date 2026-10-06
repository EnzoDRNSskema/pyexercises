"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: One integer N entered by the user.
# 2. Process: The program checks every number from 1 to N and determines if it is odd or even.
# 3. Out: One line for each number saying whether it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
# If N is 0, the program displays a message because there is nothing to check.
# If N is negative, the program displays a message because N must be positive.
# If N is greater than 100, the program displays a message and does not print all the lines.

# Your code below

n = int(input("Enter a positive number: "))

if n == 0:
    print("There is nothing to check.")
elif n < 0:
    print("Please enter a positive number.")
elif n > 100:
    print("The number is too large.")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

# Check:
# With 6, the program printed 3 odd numbers and 3 even numbers.
# With 0, it displayed that there is nothing to check.
# With a negative number, it asked for a positive number.
# With 5000, it displayed that the number is too large.