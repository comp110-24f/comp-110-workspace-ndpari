"""excercise 2, making something wordle-adjacent"""

__author__ = "730767392"


def input_word() -> str:
    """Take an input word that has five characters. If it does not have 5, print an error and exit the program."""
    five_char_word: str = input(
        "Enter a 5-character word: "
    )  # set variable values based on input
    if len(five_char_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exit after the error has been printed but before it is stored in local memory
    return five_char_word  # store to local memory


def input_letter() -> str:
    """Take an input that is one character. If it is not one character, print an error and exit the program."""
    single_letter: str = input(
        "Enter a single character: "
    )  # entire block is pretty much the same as above
    if len(single_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return single_letter


def contains_char(word: str, letter: str) -> None:
    """Identify if there are any occurences of a letter in a word. Print out where and how many"""

    print("Searching for " + letter + " in " + word)

    count_chars: int = 0  # set counter to identify if a letter occurs in a word

    if (
        word[0] == letter
    ):  # series of seperate ifs; tried using elifs then realized that those wouldn't be accessed if the previous statement was true </3
        print(letter + " found at index 0")
        count_chars += 1  # add to the counter so if it is true the count increases by 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count_chars += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count_chars += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count_chars += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count_chars += 1
    if (
        count_chars == 0
    ):  # seperating 0 and 1, everything else has the same thing printed out
        print("No instances of " + letter + " found in " + word)
    elif count_chars == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count_chars) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Combine and make callable all of the above functions."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
