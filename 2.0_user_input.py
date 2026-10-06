"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A client name and the number of employees.
# 2. Process: The program asks the user for both values and uses them in a sentence.
# 3. Out: A sentence showing the client name and the number of employees.
# 4. My two fields, and what I would do with them: I chose the client name and number of employees because they could be used in a business qualification form.


# Your code below
client_name = input("Enter the client name: ")
employees = int(input("Enter the number of employees: "))

next_year = employees + 1

print(client_name, "has", employees, "employees.")
print("If the company hires one more person, it will have", next_year, "employees.")

# Check:
# Empty line: the program accepted an empty client name.
# Space: the program accepted a space as text.
# Text instead of a number: the program gave an error because int() expects a number.