"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__: str = "730659778"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

guess_str: str = input("Pick a secret boat location between 1 and 4: ")
guess1_int: int = int(guess_str)

if guess1_int >= 1 and guess1_int <= 4:
    ship = guess1_int
else:
    if guess1_int < 1:
        print(f"Error! {guess1_int} too low!")
        exit()
    elif guess1_int > 4:
        print(f"Error! {guess1_int} too high!")
        exit()

guess2_str: str = input("Guess a number between 1 and 4: ")
guess2_int: int = int(guess2_str)

if guess2_int >= 1 and guess2_int <= 4:
    if guess2_int == ship:
        result: str = RED_BOX
    else:
        result = WHITE_BOX
    output = ""
    if guess2_int == 1:
        output += result
    else:
        output += BLUE_BOX
    if guess2_int == 2:
        output += result
    else:
        output += BLUE_BOX  # Blue box
    if guess2_int == 3:
        output += result
    else:
        output += BLUE_BOX
    if guess2_int == 4:
        output += result
    else:
        output += BLUE_BOX
    print(output)
    if guess2_int == guess1_int:
        print("Correct! You hit the ship.")
    else:
        print("Incorrect! You missed the ship.")
else:
    if guess2_int < 1:
        print(f"Error! {guess2_int} too low!")
        exit()
    elif guess2_int > 4:
        print(f"Error! {guess2_int} too high!")
        exit()
