"""ex02 one shot battleship"""

__author__= "730401354"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result: str

#guessing the row 
row_guess: int = int(input("Guess a row: "))
while row_guess > grid_size or row_guess < 1: #while guess is out of bounds
    try_again: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
    row_guess = try_again

#guessing the column 
column_guess: int = int(input("Guess a column: "))
while column_guess > grid_size or column_guess < 1: #while guess is out of bounds
    try_again2: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
    column_guess = try_again2

#defining the result
if row_guess == secret_row and column_guess == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX

#building the grid
row_idx: int = 1
while row_idx <= grid_size:
    single_row: str = ""
    column_idx: int = 1
    if row_guess == row_idx:
        while column_idx <= grid_size:
            if column_guess == column_idx:
                single_row += result
            else:
                single_row += BLUE_BOX
            column_idx += 1 
    else:
        while column_idx <= grid_size:
           single_row += BLUE_BOX
           column_idx += 1
    print(single_row)
    row_idx += 1
            

#hit or miss or close
if row_guess == secret_row and column_guess == secret_column:
    print(f"Hit!")
else:
    print (f"Miss!")