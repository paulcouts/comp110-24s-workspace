"""Functional Battleship!"""

__author__: str = "730659778"

import random
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(a: int, b: str)-> int:
    #inputs the guess
    assert b == "row" or b == "column"
    if b == "row":
        guess1_int: int = int(input("Guess a row: "))
        while guess1_int < 1 or guess1_int > a:
            guess1_int = int(input(f"The grid is only {a} by {a}. Try again: "))
        return guess1_int
    if b == "column":
        guess2_int: int = int(input("Guess a column: "))
        while guess2_int < 1 or guess2_int > a:
            guess2_int = int(input(f"The grid is only {a} by {a}. Try again: "))
        return guess2_int
    

def print_grid(a: int, guess1_int: int, guess2_int: int, right_guess: bool) -> None:
    if right_guess == True:
        emoji_str: str = RED_BOX
        win = 1
    else:
        emoji_str = WHITE_BOX

    row_int: int = 1

    while row_int <= a:
        emoji_str = ""
        column_int: int = 1
        if guess1_int == row_int:
            while column_int <= a:
                if guess2_int == column_int:
                    emoji_str += RED_BOX if (right_guess == True) else WHITE_BOX
                else:
                    emoji_str += BLUE_BOX
                column_int += 1
        else:
            while column_int <= a:
                emoji_str += BLUE_BOX
                column_int += 1
        print(emoji_str)
        row_int += 1
def correct_guess(secret_row: int, secret_column: int, guess1_int: int, guess2_int: int)-> bool:
    return guess1_int == secret_row and guess2_int == secret_column

def main(a: int, secret_row: int, secret_column: int)-> None:
    turn: int = 1
    win: int = 0
    while turn <= 5 and win == 0:
        print(f"=== Turn {turn}/5 ===")
        guess1_int = input_guess(4,"row")
        guess2_int = input_guess(4,"column")
        right_guess = correct_guess(secret_row,secret_column,guess1_int,guess2_int)
        print_grid(a,guess1_int,guess2_int,right_guess)
        if right_guess == True:
            print(f"Hit! You won in {turn}/5 turns!")
            win = 1
        else:
            print("Miss!")
        if turn == 5:
            print("X/5 - Better luck next time!")
        turn += 1
if __name__ == "__main__":
        a: int = random.randint(3, 5)
        main(a, random.randint(1, a), random.randint(1, a))