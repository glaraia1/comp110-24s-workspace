"""Testing ex05 Dictionaries Functions."""


__author__ = "730401354"


from exercises.ex05.ex05_dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_invert_use_case() -> None:
    """Check if the given dictionary keys and values are inverted."""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_use_case_2() -> None:
    """Check if the given dictionary key and value is inverted."""
    assert invert({'cat': 'apple'}) == {'apple': 'cat'}

def test_invert_edge_case() -> None:
    """Tests if an empty dictionary returns an empty dictionary."""
    assert invert({}) == {}

def test_favorite_colors_use_case() -> None:
    """Test if given a dictionary of names a color, the most frequent color appears."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"

def test_favorite_colors_use_case_tie() -> None:
    """Test if a given dictionary with a tie of the most frequent colors returns the color that appears first."""
    assert favorite_color({"Marc": "yellow", "Jon" : "yellow", "Ezri": "blue", "Kris": "blue"}) == "yellow"

def test_favorite_colors_edge_case_empty() -> None:
    """Test if a dictionary input with an empty entry still prints out the most frequent color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})
