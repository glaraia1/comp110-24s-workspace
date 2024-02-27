"""Demonstrate Basic list Syntax."""

# Initialize an empty list
grocery_list: list[str] = list() # <- list contructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

# add item to  a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list.append("eggs")
print(grocery_list2)

# indexing lists
print("Pring first element of string")
print(grocery_list[0])

#modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("Aftr change: ")
print(grocery_list)

#cannot replace letters in a str with same example from above
# example below is NOT possible to change cats to cars
"""x: str = "cats"
x[2] = "r" """

# You can have Duplicates
grocery_list.appennd("almond milk")
print("Add almond milk again: ")
print(grocery_list)

# Measuring length 
print("Length of list: ")
print(len(grocery_list))

# Removing an item... don't need to index with pop bc its an argument
grocery_list.pop(1)
print("After removing alomond milk: ")
print(grocery_list)

# Function name: display
# Parameter: list[str]
# Return nothing!
# Print out the list!
def display(example: list[str]) -> None:
    """Writing a function that prints the list"""
    print(example)

display(grocery_list)
#if i want to make a different list
display(["Alyssa", "Gabby", "Andrew"])

# what would happen if I set variale X equal to function?
x = display(["Alyssa", "Gabby", "Andrew"])
print(x)
# nothing will print because, set equal to function, and function returns nothing

# creat a list!
# Name: create
# Parameters: str and str
# RV: list[str]
# Put both parameters into list and return that list
def create(word1: str, word2: str) -> list[str]
    """when you create a list, the list is not the parameter types"""
    # Can create an empty list and add items or create a populated list like below
    my_list: list[str] = [word1, word2]
    return my_list

print(create("Hello", "world" ))
# or this is same as
x: list[str] = create("Hello", "world" )
print(x)