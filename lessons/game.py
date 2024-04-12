"""guess the number"""

from random import randint #import random number from nowhere

SECRET: int = randint(1,100)

x = 0

while x != 1: #basically can be done with a bool
    guess: int = int(input("make a guess now: "))
        
    if guess == SECRET:
        print(f"good job, {guess} is correct")
        x = 1 #value for the loop to end
    else:
        if guess <= SECRET:
            print(f"{guess} was too low smh")
        elif guess >= SECRET:
            print(f"{guess} was too high")
        print("guess again lil bro: ")