"""ex04 utils."""

__author__ = "730401354"


def all(list1: list[int], num: int) -> bool:
    """Indicate whether or not list of ints are same as given int."""
    list_idx: int = 0 
    if len(list1) == 0:
        return False
    while list_idx < len(list1):  # to go through each element
        if list1[list_idx] == num:  # if first element is equal to int, check next element
            list_idx += 1
        else:
            return False    
    return True 


def max(list2: list[int]) -> int:
    """Returns largest in the list."""
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    
    list2_idx: int = 0
    largest = list2[0]  # initialize first element
    while list2_idx < len(list2):
        if list2[list2_idx] > largest:
            largest = list2[list2_idx]
        list2_idx += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Every element at every index is equal."""
    if len(list1) != len(list2):
        return False
     
    index: int = 0
    while len(list1) == len(list2) and index < len(list1):
        if list1[index] != list2[index]:
            return False
        else:
            index += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate and append."""
    idx: int = 0
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1