"""Appointing the points."""

from __future__ import annotations


class Point:
    """This class has the attributes x and y which will be scaled."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initializes x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales without mutation."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Scales by mutating."""
        return Point(self.x * factor, self.y * factor)
