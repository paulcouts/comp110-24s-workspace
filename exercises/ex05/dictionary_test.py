"""Testing the dictionaries..."""

__author__: str = "730659778"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

import pytest


def test_invert_use():
    """Tests use case with str dictionary."""
    test: dict[str, str] = {"one": "red", "two": "blue", "three": "orange"}
    result = invert(test)
    assert result == {"red": "one", "blue": "two", "orange": "three"}


def test_invert_use_two():
    """Tests use case with int instead of str."""
    test: dict[str, int] = {"one": 1, "two": 2}
    result = invert(test)
    assert result == {1: "one", 2: "two"}


def test_invert_edge():
    """Tests edge case with a repeat."""
    with pytest.raises(KeyError):
        test: dict[str, str] = {"one": "red", "two": "red"}
        invert(test)


def test_favorite_color_use():
    """Tests use case of one most common value."""
    test: dict[str, str] = {"1": "Blue", "2": "Blue", "3": "Red"}
    result = favorite_color(test)
    assert result == "Blue"


def test_favorite_color_use_two():
    """Tests the use case of no most common value."""
    test: dict[str, str] = {"1": "Blue", "2": "Green", "3": "Red"}
    result = favorite_color(test)
    assert result == "Blue"
    # This simply returns the first value in the dictionary rather than an error


def test_favorite_color_edge():
    """Tests the edge case of an empty dictionary."""
    test: dict[str, str] = {}
    result = favorite_color(test)
    assert result == "None"


def test_count_use():
    """Tests the use case of an element appearing twice."""
    test: list[str] = ["one", "one", "two", "three"]
    result = count(test)
    assert result == {'one': 2, 'two': 1, 'three': 1}


def test_count_use_two():
    """Tests the use case of a single string."""
    test: list[str] = ["one"]
    result = count(test)
    assert result == {'one': 1}


def test_count_edge():
    """Tests the edge case of non-alphanumeric characters."""
    test: list[str] = ["one", "@", "@", "!", "", "^"]
    result = count(test)
    assert result == {'one': 1, '@': 2, '!': 1, '': 1, '^': 1}


def test_alphabetizer_use():
    """Tests the use case of 3 words."""
    test: list[str] = ["one", "two", "three"]
    result = alphabetizer(test)
    assert result == {'o': ['one'], 't': ['three', 'two']}
    

def test_alphabetizer_use_two():
    """Tests the use case of numbers."""
    test: list[str] = ["1", "3", "5"]
    result = alphabetizer(test)
    assert result == {'1': '1', '3': '3', '5': '5'}


def test_alphabetizer_edge_():
    """Tests the edge case of non-alphanumeric starting character."""
    test: list[str] = ["!one", "$two", "hi"]
    result = alphabetizer(test)
    assert result == {'!': ['!one'], '$': ['$two'], 'h': ['hi']}


def test_update_attendance_use():
    """Tests the use case of an existing day."""
    test: dict[str, list[str]] = {"Monday": ["Akil", "Justin"]}
    day = "Monday"
    student = "Charles"
    update_attendance(test, day, student)
    assert test[day] == ["Akil", "Justin"]


def test_update_attendance_use_two():
    """Tests the use case of a new day."""
    test: dict[str, list[str]] = {"Monday": ["Akil", "Justin"]}
    day = "Tuesday"
    student = "Charles"
    update_attendance(test, day, student)
    assert test[day] == ["Charles"]


def test_update_attendance_edge():
    """Tests the edge case of an empty dict."""
    test = {}
    day = "Monday"
    student = "Akil"
    update_attendance(test, day, student)
    assert test[day] == ["Akil"]