"""File to define Bear class."""


class Bear:
    """Makes a bear."""
    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Initializes."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Adds a day."""
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """Allows bear to eat."""
        self.hunger_score += num_fish
        return None