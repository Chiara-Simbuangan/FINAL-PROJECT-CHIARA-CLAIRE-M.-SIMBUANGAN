import random

def roll_dice():
    """Simulates rolling a dice and returns a number between 1 and 6."""
    return random.randint(1, 6)

def play_round():
    """Plays a single round of dice rolling and returns the winner."""
    player1_roll = roll_dice()
    player2_roll = roll_dice()
    
    print(f"Player 1 rolls: {player1_roll}")
    print(f"Player 2 rolls: {player2_roll}")
    
    if player1_roll > player2_roll:
        print("Player 1 wins this round!\n")
        return 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!\n")
        return 2
    else:
        print("It's a tie!\n")
        return 0

def main():
    player1_wins = 0
    player2_wins = 0
    rounds_played = 0

    while player1_wins < 2 and player2_wins < 2 and rounds_played < 3:
        rounds_played += 1
        print(f"Round {rounds_played}")
        
        winner = play_round()
        
        if winner == 1:
            player1_wins += 1
        elif winner == 2:
            player2_wins += 1
        
        print(f"Current score - Player 1: {player1_wins}, Player 2: {player2_wins}\n")

    if player1_wins == 2:
        print("Player 1 wins the game!")
    elif player2_wins == 2:
        print("Player 2 wins the game!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    main()
