"""Test data cleanup functionality"""

from ..data_cleanup_assistent import (
    strip_whitespaces,
    normalize_case,
    remove_duplicates,
    sort_iterable,
)


def test_strip_whitespaces():
    """Check if leading and trailing whitespaces are removed from every item"""
    result = strip_whitespaces(["   clean string   ", "Bob   ", "  Eva"])
    assert result == ["clean string", "Bob", "Eva"]


def test_normalize_case():
    """Check if all names in the list are capitalized"""
    result = normalize_case(["bob", "eva", "oliver twist"])
    assert result == ["Bob", "Eva", "Oliver Twist"]


def test_remove_duplicates():
    """Check if there are no duplictes in the final list"""
    result = remove_duplicates(["Bob", "Bob", "bob", "eva", "Eva", "eva"])
    length = len(result)

    assert length == 4
    assert sorted(result) == ["Bob", "Eva", "bob", "eva"]


def test_sort_iterable():
    """Check if the final list of name is sorted alphabetically"""
    result = sort_iterable(["Bob", "Bob", "bob", "eva", "Eva", "eva"])
    assert result == ["Bob", "Eva", "bob", "eva"]
