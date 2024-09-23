"""Exercise 01, Tea Party: Plan a tea party based on number of guests."""

__author__ = "730767392"


def main_planner(guests: int) -> None:
    """Main function to tie everything together"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    # cannot concenate string with int/float
    # had to convert to string first then print
    # tried printing then converting to string and that just didn't work
    print("Tea Bags: " + str((tea_bags(people=guests))))
    print(
        "Treats: " + str(treats(people=guests))
    )  # the three lines until here are pretty much the same bless
    print(
        "Cost: $"
        + str(
            (cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)))
            # realized assignment required that there were different names for parameters in cost and the other functions so had to call them + keyword argument as part of parameters
        )
    )


def tea_bags(people: int) -> int:
    """Determine the number of teabags needed based on guests"""
    return people * 2  # simple multiplication tbh


def treats(people: int) -> int:
    """Determine the number of treats needed based on teabags"""
    return int(tea_bags(people=people) * 1.5)  # keyword argument with multiplication


def cost(tea_count: int, treat_count: int) -> float:
    """Determine the cost based on the number of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75  # multiplication!!


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
