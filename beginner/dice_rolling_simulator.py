"""Simulate rolling a six-sided die and print the result to the terminal."""

import random


def roll_dice():
    """Return a random integer between 1 and 6, inclusive."""
    return random.randrange(1, 7)


random_number = roll_dice()

# Print outcome of the rolling dice to terminal
print(f"You've rolled a {random_number}!")
