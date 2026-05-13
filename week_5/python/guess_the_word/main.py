from constance import GAME_WORDS
import random


ATTEMPTS = 30


def show(size: int) -> str:
    return f"""
    welcome to the game\n
    you need to enter a letter fot this size of a word\n
    "{" _ " * size}"\n
    you have {ATTEMPTS}
    """

def get_random_word() -> tuple:
    word = random.choice(GAME_WORDS)
    return [l for l in word], ['_' for l in word]


def main() -> None:
    attempts = 30
    count = 0
    word, refernce_word = get_random_word()
    print(show(len(word)))
    while attempts > 0:
        count += 1
        user_guess = input(f"\t[{count}]. enter your guess: \n")
        if not(guess_match(word, refernce_word, user_guess)):
            attempts -= 1
        print("\n\t" , " ".join(refernce_word), '\n')
        if "_" not in refernce_word:
            print(f"\nyou won!! in {count} attempts")
            break
    else:
        print("\nyou lose :(")


def guess_match(secret_word: list, hidden_word: list, letter: str) -> bool:
    user_right = False
    for i, l in enumerate(secret_word):
        if letter == l:
            hidden_word[i] = l
            user_right = True
    return user_right


if __name__ == "__main__":
    main()