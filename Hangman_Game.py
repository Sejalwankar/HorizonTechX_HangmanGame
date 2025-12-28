import random

words = ["apple","banana","python","customer","price","linux"]

secret_word = random.choice(words)

guessed_letters = []

chances = 6

print("Welcome to Hangman Game!")
print("You have 6 chances to guess the words.")

while chances > 0:
    
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + ""
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the correct word.")
        break
    
    guess = input("Enter a letter:").lower()

    if guess in guessed_letters:
        print("You already gussed that letter.")
        continue
    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        chances -=1
        print("Wrong guess!")
        print("Remaining chances:", chances)

    if chances == 0:
        print("\nGame Over!")
        print("The word was", secret_word)
