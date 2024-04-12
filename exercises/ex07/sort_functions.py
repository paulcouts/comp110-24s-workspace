"""Functions that implement sorting algorithms."""

__author__ = "730659778"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx1: int = 0
    while idx1 < len(x) - 1:
        idx2: int = idx1 + 1
        current_element: int = x[idx2]
        for item in range(idx2 - 1, -1, -1):
            if current_element < x[item]:
                x[item + 1] = x[item]
                x[item] = current_element
            else:
                break
        idx1 += 1

    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx1: int = 0
    while idx1 < len(x):
        idx2: int = idx1
        unsorted: int = idx1 + 1
        while unsorted < len(x):
            if x[unsorted] < x[idx2]:
                idx2 = unsorted
            unsorted += 1
        temporary: int = x[idx1]
        x[idx1] = x[idx2]
        x[idx2] = temporary
        idx1 += 1
    return None
    