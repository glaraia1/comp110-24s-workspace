"""Ex01- Simple Battleship"""

__author__= "730401354"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

p1: int= int(input("Pick a secret boat location between 1 and 4: "))
p2: int= int(input("Guess a number between 1 and 4: "))

result: str 
boxes: str

if p1 > 4:
    print(f"Error! {p1} too high!")
elif p1 < 1:
    print(f"Error! {p1} too low!")

if p2 > 4:
    print(f"Error! {p2} too high!")
elif p2 < 1:
    print(f"Error! {p2} too low!")

#defining the result
if p2 == p1:
    result = RED_BOX
else:
    result = WHITE_BOX

#Building the blocks
if p2 == 1:
    print(f"{result}{BLUE_BOX * 3}")
elif p2 == 2:
    print(f"{BLUE_BOX}{result}{BLUE_BOX * 2}")
elif p2 == 3:
    print(f"{BLUE_BOX * 2}{result}{BLUE_BOX}")
elif p2 == 4:
    print(f"{BLUE_BOX * 3}{result}")

#Correct or incorrect
if p2 == p1:
    print(f"Correct! You hit the ship.")
else: 
    print(f"Incorrect! You missed the ship.")




