# A program that creates a txt file of responses, reads the file then uses the responses to give random answers to yes
# or no questions.
def create_txt_file():

    # Create list of responses
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

    # Create txt file called 8ball_responses and import the list of responses into the file
    # using \n to separate each response onto a new line.
    with open('8ball_responses.txt', 'w') as file:
        file.writelines(f"{response}\n" for response in responses)

# Run the function to create the file
create_txt_file()

# Import the random module
import random

# Create A function to load and read the response file and remove whitespace from the responses
def load_txt_file():
    with open('8ball_responses.txt', 'r') as file:
        responses = file.readlines()
    return [response.strip() for response in responses]

# Create the magic-8-ball
def magic_8ball():

    # Call the load_txt_file function to use
    responses = load_txt_file()

    # Create infinite loop to give a random response to a yes or no question.
    # Break the loop if user types "quit"
    while True:
        question = input("ask a yes or no question or type quit to when finished: ")
        if question.lower() == 'quit':
            break

        # Make a random choice from the list of responses
        print(random.choice(responses))

magic_8ball()