"""
Ask user for input sentence as string, calculate the number of words in the 
sentence and identify the first longest word in the sentence.
Print the output to the terminal.
"""

def analyze_sentence(sentence: str) -> tuple[int, str]:
    """ Count words in sentence and find first longest word."""

    words = sentence.split(" ")
    word_count = len(words)

    if word_count == 1 and len(words[0]) == 0:
        return 0, ""

    # first_longest = [i for i in splitted_text if len(i) == max(len(i) for i in splitted_text)] 
    first_longest = max(words, key=len)

    return word_count, first_longest


def main() -> None:
    # Ask user for the input
    sentence = input("Enter a senctence: ").strip()

    # call the main function to do the calculation and lookup
    word_count, longest_word = analyze_sentence(sentence)

    if not word_count:
        print("No words entered!")
        return
    else:
        print(f'The number of words in the sentence is: {word_count}.')
        print(f'The longest word in the sentence is: {longest_word}')



if __name__ == "__main__":
    main()