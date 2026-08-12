# ------------------------------------------------------
# Project 2: Expense Tracker
# DecodeLabs - Python Programming (Industrial Training Kit)
# ------------------------------------------------------
# Goal: Keep asking the user for expenses and keep adding
# them up until they type "quit". Then show the total spent.
# ------------------------------------------------------

# This is our "accumulator" - it stores the running total.
# It MUST be created outside the loop, otherwise it would
# reset to 0 every single time (that's the "amnesia" bug).
total = 0

print("=== Welcome to the Expense Tracker ===")
print("Enter your expenses one by one.")
print("Type 'quit' when you are done.\n")

# The "Logic Skeleton" - keeps running until we break out of it
while True:
    user_input = input("Enter an expense amount (or 'quit' to stop): ")

    # Sentinel value check - this is our "kill switch"
    if user_input == "quit":
        break

    # Defensive coding - make sure the input is actually a number
    try:
        expense = int(user_input)
    except ValueError:
        print("Invalid Data")
        continue

    # The Accumulator Pattern: total = total + new_expense
    total = total + expense

# Final Output - the "Display" phase
print("Total Spent:", total)