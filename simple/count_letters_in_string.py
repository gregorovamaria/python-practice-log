"""
The program asks user for entering a string (word, sentence) and then it counts 
how many uppercase and lowercase letters are present, and displays both counts.
"""

def case_counter(text: str) -> tuple[int, int]:
    """ Counts uppercase and lowercase letters in given string """

    upper_count = 0
    lower_count = 0

    # letters = [letter.strip() for letter in text if letter.strip() != ""]

    # for letter in letters:
    #     if letter.isupper(): upper_count += 1
    #     if letter.islower(): lower_count += 1

    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())

    return upper_count, lower_count


def main() -> None:
    """ Prompts user input and displays case counts. """

    user_input = input("Please enter a sentence: ").strip()

    if not user_input: 
        print(f'No sentence was given!')
        return

    upper_count, lower_count = case_counter(user_input)

    print(f'The number of uppercase letters is: {upper_count}')
    print(f'The number of lower letters is: {lower_count}')

if __name__ == "__main__":
    main()