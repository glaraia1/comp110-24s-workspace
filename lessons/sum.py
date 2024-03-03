"""Summing the elements of a list using different loops."""

__author__ = "730401354"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all elements."""
    list_idx: float = 0
    list_sum: float = 0
    while list_idx < len(vals):
        list_sum += vals[list_idx]
        list_idx += 1
    return list_sum 
print(w_sum([1.1, 0.9, 1.0]))


def f_sum(vals: list[float]) -> float:
    """Returns sum of all elements."""
    list_sum: float = 0
    for elem in vals:
        list_sum += elem
    return list_sum


print(f_sum([1.1, 0.9, 1.0]))


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of all elements."""
    list_sum: float = 0
    for index in range(0,len(vals)):
        list_sum += vals[index]
    return list_sum


print(f_range_sum([1.1, 0.9, 1.0]))