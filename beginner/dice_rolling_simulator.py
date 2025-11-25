"""Simulate rolling a six-sided die and print the result to the terminal."""

import random


def roll_dice() -> int:
    """Return a random integer between 1 and 6, inclusive."""
    return random.randint(1, 6)


def main() -> None:
    """Roll the die and print the result."""
    random_number = roll_dice()
    print(f"You've rolled a {random_number}!")


if __name__ == "__main__":
    main()
