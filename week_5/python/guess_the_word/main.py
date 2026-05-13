from constance import GAME_WORDS, ATTEMPTS
import random


def show(size: int) -> None:
    print ("welcome to the game")
    print("you need to enter a letter fot this size of word")
    print(" _ " * size)
    print(f"you have {ATTEMPTS}")

def get_random_word():
    word_index = random.randint(0, len(GAME_WORDS))
    word = GAME_WORDS[word_index]
    return [l for l in word]

def main():
    pass

def guess_match():
    

