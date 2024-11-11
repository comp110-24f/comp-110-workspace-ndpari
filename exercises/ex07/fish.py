"""File to define Fish class."""

__author__ = "730767392"


class Fish:
    """Make a new Fish class."""

    age: int  # define attribute

    def __init__(self):
        """Initialize the class."""
        self.age: int = 0  # set initial value
        return None

    def one_day(self) -> None:
        """Add age for every day."""
        self.age += 1  # increase value each time this function is called
        return None
