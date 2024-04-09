"""ex05 Dictionaries Utility Functions!"""


__author__ = "730401354"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that inverts the keys and values."""
    new_dict: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in new_dict:
            raise KeyError("Keys cannot be repeated")
        new_dict[dict1[key]] = key
    return new_dict
    
    
def favorite_color(name_color: dict[str, str]) -> str:
    """Returns most popular color."""
    track: dict[str, int] = {}
    score: int = 0
    winner: str = ""
    
    for key in name_color:
        if name_color[key] in track:
            track[name_color[key]] += 1
        else: 
            track[name_color[key]] = 1

    for key in track:
        if track[key] > score: 
            score = track[key]
            winner = key
    return winner


def count(value_list: list[str]) -> dict[str, int]:
    """Returns dictionary of the count of number of times the value appears in list."""
    dict_counts: dict[str, int] = {}
    for elem in value_list:
        if elem in dict_counts:
            dict_counts[elem] += 1
        else:
            dict_counts[elem] = 1
    return dict_counts


def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """Dictionary of letters and the list of words that belong to that letter."""
    alphabetized_dict: dict[str, list[str]] = {}
    
    for word in given_list:
        new_list: list[str] = []
        if word[0].lower() in alphabetized_dict:
            alphabetized_dict[0].lower().append(word)
        else:
            new_list.append(word)
            alphabetized_dict[word[0].lower()] = new_list
    return alphabetized_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates dictionary to contain days of the week and list of students who were in attendance."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = []
        attendance[day].append(student)