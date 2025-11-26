"""Command-line dice roller.
Simulate rolling an N-sided die and print results via a simple CLI.

Supports:
- --count: number of rolls
- --sides: number of sides on the die (e.g. 6, 20)
- --summary: print all rolls on a single line
- --stats: show min, max, and average of the rolls
"""

import argparse
import random
from typing import Iterable


def roll_dice(sides: int) -> int:
    """Return a random integer between 1 and the given number of sides, inclusive."""
    return random.randint(1, sides)


def roll_many(count: int, sides: int) -> list[int]:
    """Return a list of dice rolls."""
    if count <= 0:
        raise ValueError("Count must be a positive number.")

    if sides <= 1:
        raise ValueError("Sides must be an integer greater than 1.")

    return [roll_dice(sides) for _ in range(count)]


def summarize_rolls(rolls: list[int]) -> tuple[int, int, float]:
    """Return (min, max, average) statistics for the given rolls."""
    if not rolls:
        raise ValueError("Error: At least two rolls are required for stats.")

    minimum = min(rolls)
    maximum = max(rolls)
    average = sum(rolls) / len(rolls)
    return minimum, maximum, average


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        prog="dice-cli",
        description="Roll an N-sided die a user-defined number of times.",
    )

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of dice rolls (default: 1).",
    )

    parser.add_argument(
        "-s",
        "--summary",
        action="store_true",
        help="Print all dice rolls on a single line.",
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show min, max, and average of the rolls.",
    )

    parser.add_argument(
        "--sides",
        type=int,
        default=6,
        help="Number of die sides (default: 6).",
    )

    parser.add_argument(
        "--seed", type=int, help="Optional random seed for reproducible rolls."
    )

    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> None:
    """Roll the die N times and print each result."""

    args = parse_args(argv)

    if args.seed is not None:
        random.seed(args.seed)

    try:
        rolls = roll_many(args.count, args.sides)
    except ValueError as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc

    if args.summary:
        print("Rolls:", ", ".join(map(str, rolls)))
    else:
        for roll in rolls:
            print(f"You've rolled a {roll}!")

    if args.stats and len(rolls) > 1:
        minimum, maximum, average = summarize_rolls(rolls)
        print(f"Stats -> min: {minimum}, max: {maximum}, avg: {average:.2f}")


if __name__ == "__main__":
    main()
