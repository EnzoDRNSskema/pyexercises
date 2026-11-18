
"""Exercise 7.0 - Collecting data and saving it"""

# 1. In: A campaign name, an advertising channel, and a budget in euros.
# 2. Process: I check the answers and add one new row to a CSV file.
#    If the file is new, I write the column names first.
#    If an answer is empty or the budget is invalid, I ask again.
# 3. Out, file name and columns: 7.0_campaigns.csv
#    Columns: campaign_name, channel, budget_eur.
# 4. Why these columns, and what this file is for:
#    I want to track marketing campaign budgets. With 200 rows,
#    I could compare budgets by channel and calculate the total spend.

# Your code below

import csv
from pathlib import Path

# Save the CSV in the same folder as this Python file.
file_path = Path(__file__).parent / "7.0_campaigns.csv"

# Ask for a campaign name.
campaign_name = input("Campaign name: ").strip()
while not campaign_name:
    print("Please enter a campaign name.")
    campaign_name = input("Campaign name: ").strip()

# Ask for an advertising channel.
channel = input("Advertising channel: ").strip()
while not channel:
    print("Please enter an advertising channel.")
    channel = input("Advertising channel: ").strip()

# Ask for a valid budget.
while True:
    answer = input("Budget in euros: ").strip()
    try:
        budget = float(answer)
        if not 0 <= budget < float("inf"):
            print("Please enter a valid positive or zero budget.")
            continue
        break
    except ValueError:
        print("Please enter a number.")

# Write the header only if the file is new or empty.
new_file = not file_path.exists() or file_path.stat().st_size == 0

with open(file_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if new_file:
        writer.writerow(["campaign_name", "channel", "budget_eur"])
    writer.writerow([campaign_name, channel, budget])

print("Campaign saved in", file_path.name)

# Check it yourself:
# I ran the program three times with different values.
# Result: 4 lines in the CSV = 1 header and 3 campaign entries.
