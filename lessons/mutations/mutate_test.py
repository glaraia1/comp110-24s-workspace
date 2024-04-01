"""Tests my mutating functions."""

from lessons.mutations.mutating_functions import remove_first, get_first, get_and_remove_first

def test_remove_first_use_case() -> None:
    """Test basic use case for remove_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    remove_first(t)
    assert t == ["rainy", "sunny"]

def test_get_first_use_case() -> None:
    """Test basic use case for get_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    return_value: str = get_first(t)
    assert t == ["cloudy", "rainy", "sunny"]  #testing that it is not mutating input
    assert return_value == "cloudy"  #testing that it is returning the first element


def test_get_and_remove_use_case() -> None:
    """Test basic use case for get_and_remove_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    return_value: str = get_and_remove_first(t)
    assert t == ["rainy", "sunny"]
    assert return_value == "cloudy"  
