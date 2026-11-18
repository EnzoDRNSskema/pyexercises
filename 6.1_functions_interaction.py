"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of marketing campaign budgets.
# 2. Process, function by function:
# calculate_total() adds all budgets together.
# calculate_average() calculates the average budget.
# find_highest() finds the highest budget.
# summarize_budgets() uses the three previous functions together.
# 3. Out: The total, average, and highest budget.
# 4. The question my fourth function answers:
# It answers: what are the main budget indicators for this list?
# Splitting the work into three functions makes each calculation easier to test separately.

# Your code below

def calculate_total(budgets):
    return sum(budgets)

def calculate_average(budgets):
    return sum(budgets) / len(budgets)

def find_highest(budgets):
    return max(budgets)

def summarize_budgets(budgets):
    total = calculate_total(budgets)
    average = calculate_average(budgets)
    highest = find_highest(budgets)

    return total, average, highest

# Individual tests
print("Test total:", calculate_total([100, 200, 300]))
print("Test average:", calculate_average([100, 200, 300]))
print("Test highest:", find_highest([100, 200, 300]))

budgets = [1200, 950, 1500, 1100, 800, 1750, 1300, 1000]

total, average, highest = summarize_budgets(budgets)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)

# Check:
# calculate_total([100, 200, 300]) should return 600.
# calculate_average([100, 200, 300]) should return 200.
# find_highest([100, 200, 300]) should return 300.