"""Normalize a list of names and print them sorted A–Z."""

from collections.abc import Iterable


def strip_whitespaces(lst: Iterable[str]) -> list[str]:
    """Remove leading and trailing blanks from every list item."""
    return [item.strip() for item in lst]


def normalize_case(lst: Iterable[str]) -> list[str]:
    """Capitalize every item in the list."""
    return [item.title() for item in lst]


def remove_duplicates(lst: Iterable[str]) -> list[str]:
    """Return unique values."""
    return list(set(lst))


def sort_iterable(lst: Iterable[str]) -> list[str]:
    """Sort items in list alphabetically."""
    seen: set[str] = set()
    unique: list[str] = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    return sorted(unique)


def clean_names(lst: Iterable[str]) -> list[str]:
    """Clean up a given list of strings."""
    stripped = strip_whitespaces(lst)
    normalized = normalize_case(stripped)
    unique = remove_duplicates(normalized)
    sorted_lst = sort_iterable(unique)

    return sorted_lst


def main() -> None:
    """Print sorted result to terminal."""

    messy_names = [
        "  alice ",
        "Bob",
        " charlie",
        "Alice",
        "BOB ",
        "eve  ",
        " Eve",
        "eve",
    ]

    cleaned_names = clean_names(messy_names)
    print(cleaned_names)


if __name__ == "__main__":
    main()
