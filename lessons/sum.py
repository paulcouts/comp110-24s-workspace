"""Summing the elements of a list using different loops."""

__author__: str = "730659778"


def w_sum(vals: list[float]) -> float:
    """Adds up all the values in the list."""
    answer: float = 0.0
    index: int = 0

    while index < len(vals):
        answer += vals[index]
        index += 1
    return answer


def f_sum(vals: list[float]) -> float:
    """Adds the same stuff using a for loop."""
    answer: float = 0.0

    for num in vals:
        answer += num
    return answer


def f_range_sum(vals: list[float]) -> float:
    """Adds the same things but iterates using for in range."""
    answer: float = 0.0

    for num in range(len(vals)):
        answer += vals[num]
    return answer