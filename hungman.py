import random

def hangman():
    words = ["python", "hangman", "codealpha", "internship", "programming"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in guessed:
        print("\nWord: " + " ".join(guessed))
        print(f"Attempts left: {attempts}")
        letter = input("Guess a letter: ").lower()

        if letter in guessed_letters:
            print("Already guessed that letter!")
            continue
        guessed_letters.append(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print(f"\nYou won! The word was: {word}")
    else:
        print(f"\nYou lost! The word was: {word}")

hangman()
