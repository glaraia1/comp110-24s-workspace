"""ex04 utils."""

__author__ = "730401354"

def all(list1: list[int], num: int) -> bool:
    """indicate whether or not list of ints are same as given int"""
    list_idx: int = 0 
    if len(list1) == 0:
        return False
    while list_idx < len(list1): # to go through each element
        if list1[list_idx] == num: # if first element is equal to int, check next element
            list_idx += 1
        else:
            return False    
    return True 
        
