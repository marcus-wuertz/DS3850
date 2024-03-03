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