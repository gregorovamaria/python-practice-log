"""
Reads a list of a names from a text file, randomly selects one, 
and diplaye it in the terminal.
"""

import sys
from pathlib import Path
import random

def read_file(file_path: Path | str) -> list[str]:
    """Returns list of names read from given txt files."""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return [name.strip() for name in file if name.strip()]
    

def pick_random_name(names: list[str]) -> str:
    """Return a randomly choosen name from a non-empty list."""
    if not names:
        raise ValueError("Cannot select a name from an empty list.")
    return random.choice(names)



def main() -> None:
    """Reads file with names and randomly pick one, which is displayed."""
    file_path = r"names.txt"

    try:
        names = read_file(file_path)
        name = pick_random_name(names)
        print(f'Randomly selected name: {name}.')
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'.", file=sys.stderr)
        sys.exit(1)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":
    main()