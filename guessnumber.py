import random
target=random.randint(1, 100)
while True:
    guess = input("Guess a number between 1 and 100: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    print(f"Target number was: {target}")
    print("Game over. Better luck next time!")
# This code implements a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.
# The user is prompted to enter their guess, and the program provides feedback on whether the guess is too low, too high, or correct.
# The game continues until the user guesses the correct number.