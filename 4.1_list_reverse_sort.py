"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original list of marketing campaign budgets from exercise 4.0.
# 2. Process: The program creates different ordered versions of the list without changing the original.
# 3. Out: Four different orders of the budgets and the original list at the end.
# 4. My four orders, and which ones modify the original:
# Original order: the list stays unchanged.
# Ascending order: sorted() creates a new list.
# Descending order: sorted(..., reverse=True) creates a new list.
# Reversed order: slicing [::-1] creates a new list.
# None of these methods modify the original list.

# Your code below

budgets = [1200, 950, 1500, 1100, 800, 1750, 1300, 1000]

print("Original:", budgets)
print("Ascending:", sorted(budgets))
print("Descending:", sorted(budgets, reverse=True))
print("Reversed:", budgets[::-1])

print("Original at the end:", budgets)

# Check:
# The last line is the same as the original list from exercise 4.0.
# This proves that the original list was not modified.