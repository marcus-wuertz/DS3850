# DS3850
# Friday Project 1
# Welcome statement explaining how the program works
print("Welcome to the Mad Libs story generator!")
print("Please provide the following words to create your unique story:")

# Prompting the user for inputs and storing them in variables
large_object = input("Enter a large object: ")  # Stores a large object input by the user
large_objects_plural = input("Enter large objects (plural): ")  # Stores plural large objects input by the user
adjective = input("Enter an adjective: ")  # Stores an adjective input by the user
body_part = input("Enter a body part: ")  # Stores a body part input by the user
restaurant = input("Enter a restaurant: ")  # Stores a restaurant input by the user
food1 = input("Enter a food: ")  # Stores a food input by the user
food2 = input("Enter another food: ")  # Stores another food input by the user

# Generating the Mad Libs story using the user-provided inputs
story = f"I’ve had a very {adjective} day.\n\n" \
        f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n\n" \
        f"Then, at lunch, I went to {restaurant} for their delicious {food1},\n" \
        f"But the waiter brought me {food2}, which I was not hungry for.\n\n" \
        f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

# Printing the generated story
print("\nHere's your Mad Libs story:")
print(story)

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
