"""File to define River class."""

__author__: str = "730659778"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Makes a river."""
    
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish(0))
        for x in range(0, num_bears):
            self.bears.append(Bear(0, 0))

    def check_ages(self):
        """Checks the ages."""
        fish_left: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                self.fish.append(fish)
        self.fish = fish_left

        bears_left: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                self.bears.append(bear)
        self.bears = bears_left
        return None

    def bears_eating(self):
        """Allows bears to eat."""
        for i in range(0, len(self.bears)):
            if len(self.fish) >= 5:
                self.bears[i].eat(3)
                self.remove_fish(3) 
        return None
    
    def check_hunger(self):
        """Checks the hunger score."""
        alive_bears: list[Bear] = []
        for i in range(0, len(self.bears)):
            if self.bears[i].hunger_score >= 0:
                alive_bears.append(self.bears[i])
        self.bears = alive_bears
        return None
        
    def repopulate_fish(self):
        """Repopulates fish."""
        num: int = (len(self.fish)) // 2 * 4
        for i in range(0, num):
            self.fish.append(Fish(0))
        return None
    
    def repopulate_bears(self):
        """Repopulates bears."""
        num: int = (len(self.bears) - 1) // 2
        for i in range(0, num + 1):
            self.bears.append(Bear(0, 0))
        return None
    
    def view_river(self):
        """Prints the river sim."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Slices the first item in the list."""
        self.fish = self.fish[amount:]

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
        """One week simulated."""
        for i in range(0, 7):
            self.one_river_day()
