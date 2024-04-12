"""Mutating functions."""

__author__ = "730659778"

new_list = [1, 2, 3, 4, 5]


def manual_append(a: list[int], value: int) -> None:
    a.append(value)


def double(a: list[int]) -> None:
    x = 0
    while x < len(a):
        a[x] *= 2
        x += 1


manual_append(new_list, 7)
print(new_list)
double(new_list)
print(new_list)