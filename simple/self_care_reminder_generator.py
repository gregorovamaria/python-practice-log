"""Suggest a random self-care activity and print it to the terminal."""

import random


INTRO_TEXT = "Hello, here is your self-care suggestion for today:"

SELF_CARE_ACTIVITIES = [
    "Take a short walk in nature. 🌿",
    "Drink a big glass of water. 💧",
    "Do some deep breathing for 5 minutes. 🧘‍♂️",
    "Listen to your favorite music. 🎵",
    "Write down three things you're grateful for. ✨",
    "Read a chapter from a book you love. 📚",
    "Stretch your body gently. 🤸‍♀️",
    "Spend a few minutes with a pet or a loved one. 🐾",
    "Watch the sunset or sunrise. 🌅",
]


def choose_self_care_activity(activities: list[str]) -> str:
    """Return a randomly selected self-care activity from the given list."""
    if not activities:
        raise ValueError("The activities list must not be empty.")
    return random.choice(activities)


def main() -> None:
    """Select and print a self-care suggestion."""
    suggested_activity = choose_self_care_activity(SELF_CARE_ACTIVITIES)
    print(f"{INTRO_TEXT}\n{suggested_activity}")


if __name__ == "__main__":
    main()
