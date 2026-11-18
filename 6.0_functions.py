"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of marketing campaign budgets.
# 2. Process: The function adds all the budgets together.
# 3. Out: The total budget as a number.
# 4. My function name, and why return rather than print:
# My function is called calculate_total_budget because the name clearly says what it does.
# I use return because the result can be reused later in the program, while print only displays it.

# Your code below

def calculate_total_budget(budgets):
    return sum(budgets)

budgets_1 = [1200, 950, 1500, 1100, 800, 1750, 1300, 1000]
budgets_2 = [500, 700, 900]
budgets_3 = [2000, 2500, 3000]

print("Total 1:", calculate_total_budget(budgets_1))
print("Total 2:", calculate_total_budget(budgets_2))
print("Total 3:", calculate_total_budget(budgets_3))

empty_result = calculate_total_budget([])
print("Empty list result:", empty_result)

# Check:
# An empty list returns 0 because sum([]) is 0.
# I think this behaviour is acceptable because a list with no budgets has a total of 0.