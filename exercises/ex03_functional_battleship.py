"""ex03 functional battleship"""

__author__= "730401354"

def input_guess(grid_size: int, row_column: str) -> int:
    """Returns user row or column guess"""
    assert row_column == "row" or row_column == "column"
    guess: int = int(input(f"Guess a {row_column}: "))
    while guess > grid_size or guess < 1: #while guess is out of bounds
        try_again: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
        guess = try_again
    return guess

def print_grid(grid_size: int, row_guess: int, column_guess: int, check_guess: bool) -> None:
    """Returns a grid of boxes to represent the game board"""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
     
    #defining the result
    if check_guess == True:
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

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Return if the user is correct or not"""
    correct_guess: bool= True
    if secret_row == row_guess and secret_column == column_guess:
        correct_guess = True
        return correct_guess
    else:
        correct_guess = False
        return correct_guess
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Pull together all functions"""
    turn_idx: int = 1
    track: bool = False
    while turn_idx <= 5 and track != True:
        print(f"=== Turn {turn_idx}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int =  input_guess(grid_size, "column")
        verify: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        if verify == True:
            check_guess = True
            print_grid(grid_size, row_guess, column_guess, check_guess)
        else:
            check_guess = False 
            print_grid(grid_size, row_guess, column_guess, check_guess)

        turn_idx += 1
    
    
