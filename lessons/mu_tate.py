"""Mutating functions."""

__author__ = "730401354"


def manual_append(x: list[int], y: int) -> None:
    """Mutate input by appending."""
    x.append(y)


def double(z: list[int]) -> None:
    """Mutate input by multiplying every element in list 2."""
    list_idx: int = 0
    while list_idx <= len(z)-1:
        z[list_idx] *= 2
        list_idx += 1
    print(z)