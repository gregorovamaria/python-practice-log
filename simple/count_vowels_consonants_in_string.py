"""Count vowels and consonants in given string and displays results."""

VOWELS = frozenset("aeiou")

def count_vowels(sentence: str) -> int:
    """Return number of vowels in given string."""
    return sum(1 for char in sentence.lower() if char in VOWELS)

def count_consonants(sentence: str) -> int:
    """Return number of consonants in given string"""
    # return sum(1 for char in sentence.lower() if char in "bcdfghjklmnpqrstvwxyz")     # alternative 1
    return sum(1 for char in sentence.lower() if char.isalpha() and char not in VOWELS) # alternative 2


# def count_letters(sentence: str) -> tuple[int, int]:                # alternative 2 to about functions 
#     """Counts vowels and consonants for given string."""            # count_vowels() and count_consonants()
#     cnt_vowels = 0
#     cnt_consonants = 0

#     for char in sentence.lower():
#         if char.isalpha():
#             if char in VOWELS:
#                 cnt_vowels += 1
#             else:
#                 cnt_consonants += 1

#     return cnt_vowels, cnt_consonants


def main() -> None:
    sentence = 'How many vowels and consonants are in this sentence?'
    vowels = count_vowels(sentence)
    consonants = count_consonants(sentence)
    # vowels, consonants = count_letters(sentence)

    print(f'The number of vowels in the string is: {vowels}.')
    print(f'The number of consonants in the string is: {consonants}.')


if __name__ == "__main__":
    main()

