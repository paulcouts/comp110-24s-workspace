"""Dictionary practice."""

__author__: str = "730659778"


def invert(colors_input: dict[str, str]) -> dict[str, str]:
    """Takes the dictionary and switches the keys and values."""
    result: dict[str, str] = {}
    for key, value in colors_input.items():
        if value in result:
            raise KeyError("Uh-oh, we have a repeat!")
        result[value] = key

    return result


def favorite_color(colors_input: dict[str, str]) -> str:
    """Analyzes the values and returns which one is the most common."""
    color_amount: dict[str, int] = {}
    max_amount: int = 0
    popular: str = "None"
    for key, value in colors_input.items():
        if value in color_amount:
            color_amount[value] += 1
        else:
            color_amount[value] = 1

        if color_amount[value] > max_amount or (color_amount[value] == max_amount and value <= popular):
            popular = value
            max_amount = color_amount[value]
    return popular


def count(count_input: list[str]) -> dict[str, int]:
    """Takes a list of strings, makes the strings keys and counts how many times each string appears as a value."""
    result_dict: dict[str, int] = {}
    for item in count_input:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(alpha_input: list[str]) -> dict[str, list[str]]:
    """Puts the contents in alphabetical order with keys as letters."""
    result_dict: dict[str, list[str]] = {}

    for value in alpha_input:
        key = value[0].lower()
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]

    return result_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the original dictionary."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]