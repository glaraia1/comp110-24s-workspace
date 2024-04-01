"""Functions that either mutate a list or don't."""

def remove_first(input_list: list[str]) -> None:
    """Remove first element of input_list = mutating."""
    input_list.pop(0)


def get_first(input_list: list[str]) -> str:
    """Return first element of input_list without mutating."""
    return input_list[0]


def get_and_remove_first(input_list: list[str]) -> str:
    """Return first element AND remove it = mutating it."""
    elem: str = input_list[0]   #the element we want to return
    input_list.pop(0)  #now remove it
    return elem