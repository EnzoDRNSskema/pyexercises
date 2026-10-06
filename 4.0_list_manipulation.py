"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of monthly marketing campaign budgets.
# 2. Process: The program displays the list, one selected budget, a sorted version, and calculates the total budget.
# 3. Out: The original list, one budget, the sorted list, and the total budget.
# 4. What my list is about, and what I computed from it:
# My list contains monthly campaign budgets in euros.
# I computed the total because it is useful to know the overall marketing spend.

# Your code below

budgets = [1200, 950, 1500, 1100, 800, 1750, 1300, 1000]

print("Full list:", budgets)
print("One budget:", budgets[2])
print("Sorted list:", sorted(budgets))

total = sum(budgets)
print("Total budget:", total)

check_total = sum(budgets[:3])
print("Check first three budgets:", check_total)

# Check:
# 1200 + 950 + 1500 = 3650 by hand.
# Python also gives 3650 for the first three budgets.