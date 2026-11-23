"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

1. What goes in?
The user enters three pieces of information:
a name, a phone number and an email address.

2. What happens to it?
The program checks each value with a regular expression.
It only continues if all three values match the rules.

3. What comes out?
If all values are valid, they are saved in contact.txt.
Otherwise, the program shows which value is invalid.

4. What are your three fields, and what makes a value acceptable for each?
Name:
I accept only letters, with at least 2 characters.

Phone number:
I accept exactly 10 digits, with no spaces or symbols.

Email:
I accept text before @, then a domain name, then a dot and at least two letters.
"""

import re

# This pattern means:
# ^ and $ = the whole value must follow the rule
# [A-Za-z] = only letters are accepted
# {2,} = at least two letters
name_pattern = r"^[A-Za-z]{2,}$"

# This pattern means:
# \d = one digit
# {10} = exactly ten digits
phone_pattern = r"^\d{10}$"

# This pattern means:
# [A-Za-z0-9._-]+ = one or more accepted characters before @
# @ = the email must contain @
# [A-Za-z0-9.-]+ = the domain name
# \. = a real dot
# [A-Za-z]{2,} = at least two letters at the end
email_pattern = r"^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

# Ask the user for the three values.
name = input("Name: ").strip()
phone = input("Phone number: ").strip()
email = input("Email: ").strip()

# Check each value separately.
name_valid = re.fullmatch(name_pattern, name) is not None
phone_valid = re.fullmatch(phone_pattern, phone) is not None
email_valid = re.fullmatch(email_pattern, email) is not None

# Save the information only when all three values are valid.
if name_valid and phone_valid and email_valid:
    with open("contact.txt", "w", encoding="utf-8") as file:
        file.write("Name: " + name + "\n")
        file.write("Phone: " + phone + "\n")
        file.write("Email: " + email + "\n")

    print("All information is valid.")
    print("Saved in contact.txt.")

else:
    if not name_valid:
        print("Invalid name.")

    if not phone_valid:
        print("Invalid phone number.")

    if not email_valid:
        print("Invalid email.")

# Check it yourself:
# Name:
# Enzo -> pass
# E1 -> fail
# A -> fail
#
# Phone:
# 0612345678 -> pass
# 061234567 -> fail
# 06 12 34 56 78 -> fail
#
# Email:
# enzo.test@gmail.com -> pass
# enzogmail.com -> fail
# enzo@gmail -> fail
#
# I tested the nine values and the results matched my predictions.