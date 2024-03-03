"""Splitting a dictionary into two lists."""

__author__: "730401354"

def get_keys(dict1: dict[str, int]) -> list[str]:
    """Produce a list of all the keys in the input dictionary."""
    list1: list[str] = []
    for key in dict1:
        if len(dict1) == 0:
            return list1
        else:
            list1.append(key)
    return list1

def get_values(dict2: dict[str, int]) -> list[int]:
    list2: list[int] = []
    for key in dict2:
        if len(dict2) == 0:
            return list2
        else:
            list2.append(dict2[key])
    return list2