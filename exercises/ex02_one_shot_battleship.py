"""EX02 - a Shot Battleship."""

__author__: str = "730659778"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
GRID_SIZE: int = 4
secret_row: int = 3
secret_column: int = 2
x: int = 0

guess1_int: int = int(input("Guess a row: "))
while guess1_int < 1 or guess1_int > GRID_SIZE:
    guess1_int = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))

guess2_int: int = int(input("Guess a column: "))
while guess2_int < 1 or guess2_int > GRID_SIZE:
    guess2_int = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))

if guess1_int == secret_row and guess2_int == secret_column:
    emoji_str: str = RED_BOX
else:
    emoji_str = WHITE_BOX

row_int: int = 1

while row_int <= GRID_SIZE:
    emoji_str = ""
    column_int: int = 1
    if guess1_int == row_int:
        while column_int <= GRID_SIZE:
            if guess2_int == column_int:
                emoji_str += RED_BOX if (guess1_int == secret_row and guess2_int == secret_column) else WHITE_BOX
            else:
                emoji_str += BLUE_BOX
            column_int += 1
    else:
        while column_int <= GRID_SIZE:
            emoji_str += BLUE_BOX
            column_int += 1
    print(emoji_str)
    row_int += 1
if guess1_int == secret_row and guess2_int == secret_column:
    print("Hit!")
elif guess1_int == secret_row and guess2_int != secret_column:
    print("Close! Correct row, wrong column.")
elif guess1_int != secret_row and guess2_int == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")