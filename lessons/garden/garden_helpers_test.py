"""Test my garden functions."""

__author__: str = "730569778"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_edge_case() -> None:
    """Tests the edge case of an empty dictionary."""
    garden_dict = {}
    add_by_kind(garden_dict, "flower", "rose")
    assert garden_dict == {"flower": ["rose"]}


def test_add_by_kind_use_case() -> None:
    """Tests adding a plant to an existing kind."""
    garden_dict = {"flower": ["marigold", "zinnia"]}
    add_by_kind(garden_dict, "flower", "daisy")
    assert garden_dict == {"flower": ["daisy", "marigold", "zinnia"]}


def test_add_by_date_edge_case():
    """Tests the edge case of an empty dictionary."""
    garden_dict = {}
    add_by_date(garden_dict, "April", "tulip")
    assert garden_dict == {"April": ["tulip"]}


def test_add_by_date_use_case():
    """Tests the use case of adding a marigold to the "April" date."""
    garden_dict = {"April": ["marigold"]}
    add_by_date(garden_dict, "April", "daisy")
    assert garden_dict == {"April": ["daisy", "marigold"]}


def test_lookup_by_kind_and_date_use_case():
    """Tests if the correct output is given and first element is removed."""
    dict_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    dict_date = {"April": ["marigold"]}
    result = lookup_by_kind_and_date(dict_kind, dict_date, "flower", "April")
    assert result == "flowers to plant in April: ['marigold']"
    

def test_lookup_by_kind_and_date_edge_case():
    """Tests an empty dictionary as an edge case."""
    test_kind = {}
    test_date = {}
    result = lookup_by_kind_and_date(test_kind, test_date, "flower", "April")
    assert result == "No flowers to plant in April."