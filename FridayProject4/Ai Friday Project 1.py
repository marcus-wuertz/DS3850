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