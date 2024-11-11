"""File to define River class."""

__author__ = "730767392"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Make a new River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Check the age of the fish and bears and remove ones which are too old."""
        surviving_fish: list[Fish] = []  # create a new empty list
        for elem in self.fish:  # cycle through every fish in the list
            if not elem.age > 3:  # add elem to the new list if it is below 3 age
                surviving_fish.append(elem)
        self.fish = []
        for elem in surviving_fish:
            self.fish.append(elem)  # set the attribute list to the new list

        surviving_bears: list[Bear] = []  # same as above
        for elem in self.bears:
            if not elem.age > 5:
                surviving_bears.append(elem)
        self.bears = []
        for elem in surviving_bears:
            self.bears.append(elem)  # set the attribute list to the new list

        return None

    def bears_eating(self) -> None:
        """Have bears eat fish and remove fish from list."""
        for elem in self.bears:
            if len(self.fish) > 5:
                elem.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self) -> None:  # same as check ages
        """Remove bears if they are too hungry."""
        full_bears: list[Bear] = []
        for elem in self.bears:
            if not elem.hunger_score < 0:
                full_bears.append(elem)
        self.bears = []
        for elem in full_bears:
            self.bears.append(elem)  # set the attribute list to the new list
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove fish based on specified number."""
        for num in range(0, amount):  # remove the fish up to the amount specified
            self.fish.pop(num)
        return None

    def repopulate_fish(self) -> None:  # same as repopulate bears
        """Repopulate fish if there are 2."""
        for _ in range(0, (len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Repopulate bears if there are 2."""
        for _ in range(0, len(self.bears) // 2):  # using the same set-up as __init__
            # create a range based on the number of bears and add new bears
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """View the river formatting."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Have the river create a week."""
        for _ in range(0, 7):  # create a range so the following function occurs 7 times
            self.one_river_day()
        return None
