from constance import GAME_WORDS
import random

ATTEMPTS = 10

def show(size: int) -> None:
    print ("welcome to the game")
    print("you need to enter a letter fot this size of a word")
    print(f'"{" _ " * size}"')
    print(f"you have {ATTEMPTS}")

def get_random_word():
    word = random.choice(GAME_WORDS)
    return [l for l in word], ['_' for l in word]

def main():
    attempts = 10
    count = 0
    word, refernce_word = get_random_word()
    show(len(word))
    while attempts > 0:
        count += 1
        user_guess = input("enter your guess: ")
        if not(guess_match(word, refernce_word, user_guess)):
            attempts -= 1
        print("".join(refernce_word))
        if "_" not in refernce_word:
            print(f"you won!! in {count} attempts")
            break
    else:
        print("you lose :(")


def guess_match(secret_word: list, hidden_word: list, letter: str):
    user_right = False
    for i, l in enumerate(secret_word):
        if letter == l:
            hidden_word[i] = l
            user_right = True
    return user_right

if __name__ == "__main__":
    main()