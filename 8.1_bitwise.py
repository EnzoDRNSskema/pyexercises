"""Exercise 8.1 — Bitwise operators (bonus, not graded)

1. What goes in?
Three permissions represented by bits: view, edit and publish.

2. What happens to it?
The program combines permissions with bitwise OR.
It checks if a permission is present with bitwise AND.
Then it adds one permission and removes another one.

3. What comes out?
The program displays the permission values in decimal and binary at each step.

4. What are your permissions about?
My permissions are about a marketing campaign:
view the campaign, edit the campaign and publish the campaign.
"""

# Each permission uses one bit.
VIEW = 1       # 001
EDIT = 2       # 010
PUBLISH = 4    # 100

# Start with permission to view and edit the campaign.
permissions = VIEW | EDIT

print("Initial permissions")
print("Decimal:", permissions)
print("Binary :", format(permissions, "03b"))

# Check if publish permission is already present.
has_publish = permissions & PUBLISH

print()
print("Publish permission present:", bool(has_publish))

# Add publish permission.
permissions = permissions | PUBLISH

print()
print("After adding publish")
print("Decimal:", permissions)
print("Binary :", format(permissions, "03b"))

# Remove edit permission.
permissions = permissions & ~EDIT

print()
print("After removing edit")
print("Decimal:", permissions)
print("Binary :", format(permissions, "03b"))

# Check it yourself:
# Initial permissions should be 011.
# After adding publish, it should be 111.
# After removing edit, it should be 101.
# I checked the binary values and they match my prediction.