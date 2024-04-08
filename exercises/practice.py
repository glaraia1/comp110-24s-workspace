"""for key in new_dict:
    if key == key:
        raise KeyError("cannot repeat values")"""

"""def invert(dict1: dict[str, str]) -> dict[str, str]:
    Returns a dictionary that inverts the keys and values.
    new_dict: dict[str, str] = {}
    dict1: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    idx: int = 1
    for key in range(0, len(dict1)):
        new_dict[dict1[key]] = key
        if key == key[idx]:  # check if first key is repeated, then move to next
            raise KeyError("Keys cannot be repeated")
        else:
            idx += 1
    return new_dict
invert({'a': 'z', 'b' : 'y', 'c': 'x'})"""

def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """Dictionary of letters and the list of words that belong to that letter."""
    alphabetized_dict: dict[str, list[str]] = {}
    for word in given_list:
        word.lower()
        if word[0] in alphabetized_dict:
            alphabetized_dict[key] += word
        else:
            key = word[0]
    return alphabetized_dict    