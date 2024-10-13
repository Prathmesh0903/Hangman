import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = ["_"] * len(word)

# Set the limit for incorrect guesses
max_incorrect_guesses = 6

# Initialize the number of incorrect guesses
incorrect_guesses = 0

print("Welcome to Hangman!")
print("You have", max_incorrect_guesses, "chances to guess the word.")

while True:
    # Print the current state of the word
    print(" ".join(guessed_letters))

    # Ask the user for a guess
    guess = input("Guess a letter: ")

    # Check if the guess is in the word
    if guess in word:
        # Reveal the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
    else:
        # Increment the number of incorrect guesses
        incorrect_guesses += 1
        print("Incorrect! You have", max_incorrect_guesses - incorrect_guesses, "chances left.")

    # Check if the user has won or lost
    if "_" not in guessed_letters:
        print("Congratulations! You won!")
        break
    elif incorrect_guesses == max_incorrect_guesses:
        print("Sorry, you lost. The word was", word)
        break