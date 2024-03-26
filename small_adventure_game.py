import time

# Define the game functions
def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious place...")
    time.sleep(2)
    print("Your mission is to find the hidden treasure.")
    time.sleep(2)

def choose_path():
    print("\nWhich path will you choose?")
    print("1. Go left")
    print("2. Go right")
    print("3. Go straight")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    elif choice == '3':
        straight_path()
    else:
        print("Invalid choice. Try again.")
        choose_path()

def left_path():
    print("\nYou chose the left path...")
    time.sleep(2)
    print("Oh no! You fell into a pit and got trapped.")
    time.sleep(2)
    game_over()

def right_path():
    print("\nYou chose the right path...")
    time.sleep(2)
    print("You encountered a ferocious beast!")
    time.sleep(2)
    print("Quickly! What will you do?")
    action = input("Fight or run? (fight/run): ")
    if action.lower() == 'fight':
        print("You fought bravely, but the beast was too strong...")
        time.sleep(2)
        game_over()
    elif action.lower() == 'run':
        print("You managed to escape the beast!")
        time.sleep(2)
        choose_path()
    else:
        print("Invalid action. Try again.")
        right_path()

def straight_path():
    print("\nYou chose the straight path...")
    time.sleep(2)
    print("You stumbled upon a hidden treasure!")
    time.sleep(2)
    print("Congratulations! You win!")
    time.sleep(2)
    play_again()

def game_over():
    print("\nGame Over! Would you like to play again?")
    play_again()

def play_again():
    choice = input("Enter 'yes' to play again, 'no' to quit: ")
    if choice.lower() == 'yes':
        start_game()
    elif choice.lower() == 'no':
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid choice. Try again.")
        play_again()

def start_game():
    intro()
    choose_path()

# Start the game
start_game()
