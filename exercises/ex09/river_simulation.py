"""Simulate the river."""

__author__: str = "730659778"

from exercises.ex09.river import River

my_river = River(10, 2)


while my_river.day <= 7:
    my_river.one_river_week()
    print(my_river.view_river)
    