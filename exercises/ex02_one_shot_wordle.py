"""EX02 - One shot wordle."""

__author__ = "730551323"

SECRET_WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_index: int = 0
INDEX: str = ""
guess: str = input(f"What is your {len(SECRET_WORD)}-letter guess? ")
while len(guess) != len(SECRET_WORD):
    guess: str = input(f"That was not {len(SECRET_WORD)} letters! Try again: ")
while guess_index < len(SECRET_WORD):
    if SECRET_WORD[guess_index] == guess[guess_index]:
            INDEX = INDEX + GREEN_BOX  
    else:
        guessed_character: bool = False
        secret_index: int = 0
        while guessed_character != True and secret_index < len(SECRET_WORD):
            if SECRET_WORD[secret_index] == guess[guess_index]:
                guessed_character = True
            else:
                secret_index = secret_index + 1
            if guessed_character != False:
                 INDEX = INDEX + YELLOW_BOX
        else:
            INDEX = INDEX + WHITE_BOX
        guess_index = guess_index + 1
print(INDEX)

if guess == SECRET_WORD:
    print("Woo! You got it!")
else:  #guess != SECRET_WORD
    print("Not quite. Play again soon!")