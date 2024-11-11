"""File to define Bear class."""

__author__ = "730767392"


class Bear:
    """Make a new Bear class."""

    age: int  # define attributes
    hunger_score: int

    def __init__(self):
        """Iniitalize the class."""
        self.age: int = 0  # set initial value
        self.hunger_score: int = 0  # set initial vale
        return None

    def one_day(self) -> None:
        """Add age and hunger for every day."""
        self.age += 1  # add one every time this function is run
        self.hunger_score -= 1  # subtract one every time this function is run
        return None

    def eat(self, num_fish: int) -> None:
        """Change hunger based on how many fish are eaten."""
        self.hunger_score += num_fish
        return None
