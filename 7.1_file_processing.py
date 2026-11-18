
"""Exercise 7.1 - Loading, cleaning and saving names"""

# What is wrong with names.txt:
# - Some names are in lowercase, like "grace hopper".
# - Some names have uppercase letters, like "ada LOVELACE".
# - Some lines are empty.
# - Some lines have extra spaces before the names.
# - "GUIDO van rossum" has three words instead of two.
# - The names are not sorted by last name.

# 1. In: The file names.txt with names written in different ways.
# 2. Process, problem by problem:
#    I remove empty lines.
#    I remove extra spaces using split() and join().
#    I use title() to correct capital letters.
#    I keep all the words of the last name.
#    I sort the names alphabetically by last name.
# 3. Out: A new file called 7.1_clean_names.txt.
# 4. How I decide which word is the last name:
#    The first word is the first name.
#    All the other words are the last name.
#    For example, "Guido Van Rossum" has "Van Rossum" as last name.

# Your code below

from pathlib import Path

# Find the input and output files.
folder = Path(__file__).parent
input_file = folder / "names.txt"
output_file = folder / "7.1_clean_names.txt"

# Read the original file.
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Clean the names and remove empty lines.
names = []

for line in lines:
    words = line.split()

    if words:
        clean_name = " ".join(words).title()
        names.append(clean_name)

# Sort the names by last name.
names.sort(key=lambda name: " ".join(name.split()[1:]).lower())

# Save the results in a new file.
with open(output_file, "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

# Show the results in the terminal.
print("Original lines:", len(lines))
print("Clean names:", len(names))
print("First name in sorted list:", names[0])
print("Last name in sorted list:", names[-1])

# Check it yourself:
# The original file has 10 lines, including 2 empty lines.
# The new file has 8 lines because I removed the empty lines.
# First in the sorted list: Margaret Hamilton.
# Last in the sorted list: Guido Van Rossum.
