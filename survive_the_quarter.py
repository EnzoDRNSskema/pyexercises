# Enzo DERNOIS - Group B
# Feature chosen: Difficulty.
# I chose it because the starting budget changes the strategy while keeping the same game rules.

# 1. What goes in:
# scenarios_B.csv uses ; as separator.
# It contains Num, Situation, and for A, B and C: the choice text, money change,
# buzz/reputation change and reaction.
# Money and reputation changes are written as positive or negative integers.

# 2. What happens:
# The program loads the scenarios.
# It asks for the player's name and difficulty.
# It shuffles the scenarios and plays up to 10 days.
# Each day it displays A, B and C and asks until the choice is valid.
# It applies the money and reputation changes and stores the move in history.
# The game stops immediately if budget or reputation reaches 0 or less.

# 3. What comes out:
# The player sees the budget, reputation, situations, choices and feedback.
# At the end the player sees if they are fired or their final title.
# The program also shows the best and worst move.
# results.csv stores name, budget, reputation, title and date.

# 4. What could go wrong:
# A wrong A/B/C choice: the program asks again.
# Reputation above 100: the program limits it to 100.
# Budget or reputation at 0 or below: the game stops immediately.
# Missing or invalid scenarios_B.csv: the program prints an error and stops cleanly.

import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_B.csv"
RESULT_FILE = "results.csv"


# Load the Group B scenarios and create tuples for the three choices.
def load_scenarios(filename):
    scenarios = []

    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            options = {}

            for letter in ("A", "B", "C"):
                options[letter] = (
                    row[f"{letter}_Choice"],
                    int(row[f"{letter}_Money"]),
                    int(row[f"{letter}_Buzz"]),
                    row[f"{letter}_Reaction"],
                )

            scenario = {
                "num": int(row["Num"]),
                "situation": row["Situation"],
                "options": options,
            }

            scenarios.append(scenario)

    return scenarios


# Keep asking until the player gives an accepted answer.
def ask_valid_choice(prompt, allowed):
    while True:
        answer = input(prompt).strip().lower()

        if answer in allowed:
            return answer

        print("Please type " + ", ".join(value.upper() for value in allowed) + ".")


# My extra feature lets the player choose the starting difficulty.
def choose_starting_budget():
    difficulty = ask_valid_choice(
        "Difficulty - easy or hard: ",
        ("easy", "hard")
    )

    if difficulty == "easy":
        return 15000

    return 6000


# Apply one choice and return the two new gauges as a tuple.
def apply_choice(budget, reputation, option):
    choice_text, budget_change, reputation_change, feedback = option

    budget += budget_change
    reputation += reputation_change

    if reputation > 100:
        reputation = 100

    return budget, reputation


# Convert the final score into the correct title.
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score <= 119:
        return "Growth Hacker"
    elif score <= 139:
        return "CMO Material"
    else:
        return "Viral Legend"


# Save one finished game in results.csv.
def save_result(name, budget, reputation, title):
    file_exists = True

    try:
        with open(RESULT_FILE, "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        file_exists = False

    with open(RESULT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "name",
                "budget",
                "reputation",
                "title",
                "date"
            ])

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            date.today().isoformat()
        ])


# Run one complete game.
def play_game():
    name = input("Player name: ").strip()

    if name == "":
        name = "Anonymous"

    budget = choose_starting_budget()
    reputation = 50

    try:
        scenarios = load_scenarios(SCENARIO_FILE)

    except (FileNotFoundError, KeyError, ValueError) as error:
        print("Could not load scenarios_B.csv:", error)
        return

    if len(scenarios) < 10:
        print("Not enough scenarios to play 10 days.")
        return

    random.shuffle(scenarios)

    history = []
    fired_reason = None

    # Play ten random scenarios unless one gauge reaches zero first.
    for day, scenario in enumerate(scenarios[:10], start=1):

        print()
        print("--- Day", day, "---")
        print(
            "[Budget:",
            budget,
            "EUR | Reputation:",
            str(reputation) + "/100]"
        )

        print(scenario["situation"])

        for letter in ("A", "B", "C"):
            print(
                letter + ":",
                scenario["options"][letter][0]
            )

        choice = ask_valid_choice(
            "Your choice (A, B or C): ",
            ("a", "b", "c")
        ).upper()

        option = scenario["options"][choice]

        choice_text = option[0]
        budget_change = option[1]
        reputation_change = option[2]
        feedback = option[3]

        budget, reputation = apply_choice(
            budget,
            reputation,
            option
        )

        print(feedback)

        print(
            "Budget",
            f"{budget_change:+d}",
            "EUR, Reputation",
            f"{reputation_change:+d}"
        )

        # One tuple is stored for each played day.
        history.append(
            (
                reputation_change,
                day,
                choice_text
            )
        )

        # Stop immediately if one gauge reaches zero.
        if budget <= 0 or reputation <= 0:

            if budget <= 0 and reputation <= 0:
                fired_reason = "budget and reputation reached 0 or less"

            elif budget <= 0:
                fired_reason = "budget reached 0 or less"

            else:
                fired_reason = "reputation reached 0 or less"

            break

    print()
    print("==============================")

    # Display the correct ending.
    if fired_reason is not None:
        title = "Fired"

        print("You are fired:", fired_reason)
        print(
            "Budget:",
            budget,
            "EUR, reputation:",
            str(reputation) + "/100"
        )

    else:
        score = reputation + budget // 200
        title = get_title(score)

        print("Quarter survived!")
        print(
            "Budget left:",
            budget,
            "EUR, reputation:",
            str(reputation) + "/100"
        )
        print("Final score:", score)
        print(name + ", your title:", title)

    # Tuple comparison finds the biggest and smallest reputation impacts.
    best_move = max(history)
    worst_move = min(history)

    print(
        "Best move: day",
        best_move[1],
        '"' + best_move[2] + '"',
        "(" + f"{best_move[0]:+d}" + ")"
    )

    print(
        "Worst move: day",
        worst_move[1],
        '"' + worst_move[2] + '"',
        "(" + f"{worst_move[0]:+d}" + ")"
    )

    save_result(
        name,
        budget,
        reputation,
        title
    )

    print("Saved in results.csv")


# Start the game.
if __name__ == "__main__":
    play_game()