# Number Guessing Game

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {number}.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()