"""Defining a simple recursive function f."""

__author__: str = "730659778"


def f(n: int, k: int) -> int:
    """N as zero will always b zero, recursiveness is defined by k added to n-1(k)."""
    if n == 0:
        return n * k   # equals zero
    else:
        return k + f(n - 1, k)