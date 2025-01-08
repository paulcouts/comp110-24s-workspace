"""File to define Fish class."""


class Fish:
    """Makes a fish."""
    
    age: int

    def __init__(self, age: int = 0):
        """Initializes."""
        self.age = age
        return None
    
    def one_day(self):
        """Makes one day."""
        self.age += 1
        return None