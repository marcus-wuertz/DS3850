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

# Notes:
# Welcome statement explaining how the program works
# Prompt the user to provide words for the Mad Libs story
# Prompt the user to input a large object and store it in a variable
# Prompt the user to input plural large objects and store it in a variable
# Prompt the user to input an adjective and store it in a variable
# Prompt the user to input a body part and store it in a variable
# Prompt the user to input a restaurant and store it in a variable
# Prompt the user to input a food and store it in a variable
# Prompt the user to input another food and store it in a variable
# Generating the Mad Libs story using the user-provided inputs
# Construct the story by inserting the user-provided inputs into the story template
# Print the generated Mad Libs story for the user to enjoy

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

# Notes:
# Welcome statement for Friday Project 2
# Import the random module to generate random numbers
# Generating random numbers for Powerball: white balls
# Generating a random integer between 1 and 69 for the first white ball
# Generating a random integer between 1 and 69 for the second white ball
# Generating a random integer between 1 and 69 for the third white ball
# Generating a random integer between 1 and 69 for the fourth white ball
# Generating a random integer between 1 and 69 for the fifth white ball
# Generating random numbers for Powerball: red ball
# Generating a random integer between 1 and 26 for the red ball
# Constructing the Powerball numbers string with appropriate spacing
# Printing the Powerball numbers string

# Friday Project 3

# Welcome statement
print("Welcome to the Quiz Bowl!")
print("Answer the following questions and get instant feedback on your answers.")

# Dictionary of questions and answers
quiz_questions = {
    "What is the capital of France?": "paris",
    "Who wrote 'Romeo and Juliet'?": "shakespeare",
    "What is the powerhouse of the cell?": "mitochondria",
    "What is the chemical symbol for water?": "h2o",
    "What is the largest planet in our solar system?": "jupiter"
}

# Counter to keep track of correct answers
correct_answers = 0

# Loop through each question in the dictionary
for question, answer in quiz_questions.items():
    user_answer = input(question + " ").lower().strip()  # Get user's answer and convert to lowercase

    # Check if the user's answer matches the answer in the dictionary
    if user_answer == answer:
        print("Correct")
        correct_answers += 1
    else:
        print(f"Incorrect, the correct answer was: {answer}")

# Print the total number of correct answers
print(f"\nYou got {correct_answers} out of {len(quiz_questions)} questions correct.")

# Notes:
# Welcome statement for Friday Project 3
# Dictionary of quiz questions and answers
# Counter to keep track of correct answers
# Loop through each question in the dictionary
# Get user's input for the current question and convert it to lowercase
# Check if the user's answer matches the answer in the dictionary
# If the user's answer matches the answer in the dictionary, print 'Correct' and increment the correct_answers counter
# If the user's answer does not match the answer in the dictionary, print 'Incorrect' along with the correct answer
# Print the total number of correct answers
