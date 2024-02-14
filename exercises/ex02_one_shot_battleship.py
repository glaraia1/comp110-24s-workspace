"""ex02 one shot battleship"""

__author__= "730401354"

grid_size: int = 5
secret_row: int = 3
secret_column: int = 2


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

if row_guess == secret_row and column_guess == secret_column:
    print(f"Hit!")
else:
    print (f"Miss!")