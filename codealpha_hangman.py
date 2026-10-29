import random

words = ["python", "apple", "cricket", "laptop", "gaming"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

else:
    print("\nGame Over!")