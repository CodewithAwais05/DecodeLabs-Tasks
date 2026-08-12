# ------------------------------------------------------
# Project 3: Random Password Generator
# DecodeLabs - Python Programming (Industrial Training Kit)
# ------------------------------------------------------
# Goal: Ask the user for a password length and generate a
# random, complex password using letters and numbers.
# ------------------------------------------------------

import string   # gives us ready-made character sets (letters, digits)
import secrets  # cryptographically secure random choice (not "random" module)

# Phase 1: Input - get the password length from the user
while True:
    length_input = input("Enter the desired password length (e.g., 8): ")

    try:
        length = int(length_input)
    except ValueError:
        print("Invalid input! Please enter a whole number.\n")
        continue

    if length <= 0:
        print("Length must be greater than 0.\n")
        continue

    break  # valid length received, move on

# Phase 2: Process - build the character pool and generate the password
# string.ascii_letters = a-z + A-Z
# string.digits        = 0-9
character_pool = string.ascii_letters + string.digits

# Using secrets.choice() instead of random.choice() because random
# is predictable (Mersenne Twister) and not safe for passwords.
password_characters = [secrets.choice(character_pool) for _ in range(length)]

# Using ''.join() instead of += in a loop, since strings are immutable
# in Python and += would create a new string object every single time.
password = ''.join(password_characters)

# Phase 3: Output - display the generated password
print("\nGenerated Password:", password)