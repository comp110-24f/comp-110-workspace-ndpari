"wordle exercise"
__author__ = "730767392"


def input_guess(secret_word_len: int) -> str:
    "have user input a word that matches the intended length"
    input_word: str = input("Enter a " + str(secret_word_len) + " character word: ")
    while (
        len(input_word) != secret_word_len
    ):  # only when it's not equal does it print this
        input_word = input(
            "That wasn't " + str(secret_word_len) + " chars! Try again: "
        )
    return input_word  # store to local memory


def contains_char(secret_word: str, char_guess: str) -> bool:
    "check if a character matches a word"
    assert len(char_guess) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False
    # add false at the end because adding it as an else within the while
    # meant that it would do nothing when it finished checking the word


def emojified(guess: str, secret_word: str) -> str:
    "print emojis corresponding to if letters are correct in a guessed word"
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0  # start index
    emojis: str = (
        ""  # need to add to the string so it doesn't just vertically print boxes
    )
    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            emojis += GREEN_BOX  # add to string
        elif contains_char(
            secret_word, guess[idx]
        ):  # making sure parameters are in correct order
            emojis += YELLOW_BOX
        elif not (
            contains_char(secret_word, guess[idx])
        ):  # setting to = False did not work which I kept just trying in different ways
            emojis += WHITE_BOX
        idx += 1  # add to index, has to add no matter what outcome of ifs is
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # set counter to 1 took me tooooo long to realize
    while turns <= 6:
        print("=== Turn " + str(turns) + "/6 ===")
        user_guess = input_guess(
            len(secret)
        )  # use the length of the secret word to indicate the length the word should be
        print(emojified(user_guess, secret))
        if user_guess == secret:
            print("You won in " + str(turns) + "/6 turns!")
            break  # otherwise it keeps going through turns
        turns += 1
    if turns > 6:  # made a seperate section because it wouldn't work inside the while
        # which makes sense upon further thought lol)
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
