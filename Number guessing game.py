import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Initialize the user's guess to None
    guess = None
    
    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get the user's guess
            guess = int(input("Take a guess: "))
            
            # Check if the guess is too low, too high, or correct
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print("Congratulations! You guessed the number!")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()