"""List Utility Functions."""

__author__: str = "730659778"


def all(nums: list[int], compare: int) -> bool:
    """Iterates through the list and compares each entry to the given integer."""
    if len(nums) == 0:
        return False
    index: int = 0
    while index < len(nums):
        if nums[index] != compare:
            return False
        index += 1
    return True


def max(nums2: list[int]) -> int:
    """Returns the largest value in a list."""
    if len(nums2) == 0:
        raise ValueError("max() arg is an empty list")
    
    maximum = nums2[0]
    index = 1

    while index < len(nums2):
        if nums2[index] > maximum:
            maximum = nums2[index]
        index += 1

    return maximum

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """If they are all equal it returns true else false."""
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1

    return True


def extend(listone: list[int], listtwo: list[int]) -> None:
    """This one appends each item in listtwo to listone."""
    index = 0
    length = len(listtwo)

    while index < length:
        listone.append(listtwo[index])
        index += 1