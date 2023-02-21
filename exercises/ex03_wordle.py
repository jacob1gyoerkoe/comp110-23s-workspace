"""Ex03 - Wordle"""

__author__="730551323"

from bs4 import GuessedAtParserWarning


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "codes"


def contains_char(word:str, char:str) -> bool:
    #Checks to see if a word contains a character
    assert len(char) == 1
    guessed_idx: int = 0
    while guessed_idx < len(word):
        if char == word[guessed_idx]:
            return True
        else:
            guessed_idx = guessed_idx + 1
    return False

def emojified(guess:str, secret:str) -> str:
    #Makes the string of emojis for wordle
    assert len(secret) == len(guess)
    guess_idx: int = 0
    emoji_str: str = ""
    while guess_idx < len(secret):
        if secret[guess_idx] == guess[guess_idx]:
            emoji_str = emoji_str + GREEN_BOX
        else:
            if contains_char(secret, guess[guess_idx]):
                emoji_str = emoji_str + YELLOW_BOX
            else:
                emoji_str = emoji_str + WHITE_BOX
        guess_idx = guess_idx + 1
    return emoji_str

def input_guess(expected_length: int) -> str:
    #Make sure that the length of the input guess is correct
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    #The entrypoint of the program and main game loop
    turn: int = 0
    win: bool = False
    while turn <= len(secret) and win == False:
        turn = turn + 1
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if secret == guess:
            win = True
    if win == False and len(secret) <= turn:
        print("X/6 - Sorry, try again tomorrow! ")
    if win == True:
        print(f"You won in {turn}/6 turns!")

if __name__ == "__main__":
    main()