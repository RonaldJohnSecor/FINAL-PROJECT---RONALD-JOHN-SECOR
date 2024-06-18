import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        # Player's choice
        print("\nChoose one: rock, paper, scissors")
        player_choice = input().lower()

        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        # Determine the winner of this round
        if player_choice in choices:
            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                 (player_choice == 'paper' and computer_choice == 'rock') or \
                 (player_choice == 'scissors' and computer_choice == 'paper'):
                print("You win this round!")
                player_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1
        else:
            print("Invalid choice. Please choose again.")
            continue

        # Check if someone has won the game
        if player_score == 2:
            print("\nCongratulations! You won the game!")
            break
        elif computer_score == 2:
            print("\nSorry, you lost the game.")
            break

        print(f"\nScore - You: {player_score}, Computer: {computer_score}")

# Start the game
play_game()