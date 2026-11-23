"""Exercise 8.0 — Operators (bonus, not graded)

1. What goes in?
Two strings: "Apple" and "apple".

2. What happens to it?
The program compares the two strings with comparison operators.
Then it combines some comparison results with and, or and not.

3. What comes out?
A readable table showing each comparison and its result.

4. Which two values did you pick, and which comparison result surprised you?
I picked "Apple" and "apple".
I was surprised that "Apple" < "apple" is True because capital letters are ordered before lowercase letters in Python.
"""

# My two values have the same letters but different capitalisation.
value1 = "Apple"
value2 = "apple"

# Store the comparison results so they can be reused.
equal = value1 == value2
not_equal = value1 != value2
less_than = value1 < value2
less_equal = value1 <= value2
greater_than = value1 > value2
greater_equal = value1 >= value2

# Display every comparison in a simple table.
print("Comparison table")
print("------------------------------")
print(value1, "==", value2, ":", equal)
print(value1, "!=", value2, ":", not_equal)
print(value1, "< ", value2, ":", less_than)
print(value1, "<=", value2, ":", less_equal)
print(value1, "> ", value2, ":", greater_than)
print(value1, ">=", value2, ":", greater_equal)

# Combine some of the comparison results with logical operators.
print()
print("Logical combinations")
print("------------------------------")
print("equal AND less_than:", equal and less_than)
print("not_equal AND less_than:", not_equal and less_than)
print("equal OR less_than:", equal or less_than)
print("greater_than OR greater_equal:", greater_than or greater_equal)
print("NOT equal:", not equal)

# Check it yourself:
# I predicted the comparison results before running the program.
# I got 5 out of 6 comparison results right.
# The result that surprised me was "Apple" < "apple".