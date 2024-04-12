"""Some functions for my garden plan."""

__author__: str = "730659778"


def add_by_kind(input_dict: dict[str, list[str]], add_type: str, add_plant: str) -> None:
    """Adds a plant to the dictionary with the type and plant."""
    if type in input_dict:
        input_dict[type].append(add_plant)
    else:
        input_dict[type] = [add_plant]


def add_by_date(input_dict: dict[str, list[str]], date: str, plant: str) -> None:
    """Adds a plant in chronological order."""
    if date in input_dict:
        input_dict[date].append(plant)
        input_dict[date].sort()
    else:
        input_dict[date] = [plant]


def lookup_by_kind_and_date(input_dict_kind: dict[str, list[str]], input_dict_date: dict[str, list[str]], kind: str, date: str) -> str:
    """Finds the kind of plant for each date."""
    plants = []

    if kind in input_dict_kind and date in input_dict_date:
        plants = [plant for plant in input_dict_kind[kind] if plant in input_dict_date[date]]

    if plants:
        return f"{kind}s to plant in {date}: {plants}"
    else:
        return f"No {kind}s to plant in {date}."