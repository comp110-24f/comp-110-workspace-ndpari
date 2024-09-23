"""challenge question 2, identifying a secret number"""

__author__ = "730767392"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x > secret:
        print("Your guess was too high! The secret number is " + str(secret))

    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))

    else:
        print("You got it!")


if __name__ == "__main__":
    guess_a_number()
