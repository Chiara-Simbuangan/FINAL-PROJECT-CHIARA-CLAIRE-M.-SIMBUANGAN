import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess what it is?")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    while True:
        # Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check the guess
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")
            break

if __name__ == "__main__":
    number_guessing_game()
