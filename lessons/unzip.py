"""Splitting a dictionary into two lists."""

__author__: str = "730659778"


def get_keys(one: dict[str, int]) -> list[str]:
    """Gets the keys."""
    if len(one) == 0:
        return []
    else:
        return list(one.keys())
    

def get_values(two: dict[str, int]) -> list[int]:
    """Gets the values."""
    if len(two) == 0:
        return []
    else:
        return list(two.values())