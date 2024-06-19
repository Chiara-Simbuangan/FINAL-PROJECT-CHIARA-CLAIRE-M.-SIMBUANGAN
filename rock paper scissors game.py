def display_menu():
    print("\nUnit Conversion Menu:")
    print("1. Millimeters to Centimeters")
    print("2. Feet to Meters")
    print("3. Inches to Centimeters")
    print("4. Pounds to Kilograms")
    print("5. Gallons to Liters")
    print("6. Exit")

def mm_to_cm(mm):
    return mm / 10

def ft_to_m(ft):
    return ft * 0.3048

def in_to_cm(inches):
    return inches * 2.54

def lb_to_kg(lb):
    return lb * 0.453592

def gal_to_l(gallons):
    return gallons * 3.78541

def unit_conversion():
    player_score = 0
    opponent_score = 0

    while player_score < 2 and opponent_score < 2:
        display_menu()
        choice = input("Choose a conversion option (1-6): ")
        
        if choice == '6':
            print("Exiting the program. Goodbye!")
            return

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please select a valid option.")
            continue
        
        try:
            value = float(input("Enter the value to be converted: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

        if choice == '1':
            result = mm_to_cm(value)
            correct_result = value / 10
        elif choice == '2':
            result = ft_to_m(value)
            correct_result = value * 0.3048
        elif choice == '3':
            result = in_to_cm(value)
            correct_result = value * 2.54
        elif choice == '4':
            result = lb_to_kg(value)
            correct_result = value * 0.453592
        elif choice == '5':
            result = gal_to_l(value)
            correct_result = value * 3.78541

        print(f"The result is: {result}")

        # Randomly determine if the player or the opponent wins this round
        from random import choice as random_choice
        winner = random_choice(['player', 'opponent'])

        if winner == 'player':
            player_score += 1
            print("You won this round!")
        else:
            opponent_score += 1
            print("Your opponent won this round.")

        print(f"Score - You: {player_score}, Opponent: {opponent_score}")

    if player_score == 2:
        print("\nCongratulations! You are the winner!")
    else:
        print("\nYour opponent won the game. Better luck next time!")

if __name__ == "__main__":
    unit_conversion()
