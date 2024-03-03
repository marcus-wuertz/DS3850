# Friday Project 2

import random

# Function to generate Powerball numbers
def generate_powerball_numbers():
    # Generating random numbers for Powerball
    white_ball1 = random.randint(1, 69)
    white_ball2 = random.randint(1, 69)
    white_ball3 = random.randint(1, 69)
    white_ball4 = random.randint(1, 69)
    white_ball5 = random.randint(1, 69)
    red_ball = random.randint(1, 26)

    # Constructing the Powerball numbers string with appropriate spacing
    powerball_numbers = f"{white_ball1}  {white_ball2}  {white_ball3}  {white_ball4}  {white_ball5}    {red_ball}"

    # Printing the Powerball numbers string
    print("Here are your Powerball numbers:")
    print(powerball_numbers)

# User input function
def get_powerball_choice():
    while True:
        choice = input("Would you like some Powerball numbers? (Yes/No): ").strip().lower()
        
        if choice == 'yes':
            generate_powerball_numbers()
            break
        elif choice == 'no':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

# Calling the function to get the user's choice
get_powerball_choice()