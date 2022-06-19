import random

## The first thing destroyes the second thing
RULES = {   "Scissors": "Paper", 
            "Paper": "Rock", 
            "Rock": "Lizard", 
            "Lizard": "Spock",
            "Spock" : "Scissors",
            "Scissors" : "Lizard",
            "Lizard" : "Paper",
            "Paper" : "Spock",
            "Spock" : "Rock",
            "Rock" : "Scissors"
            }

options = [
    'Rock',
    'Paper',
    'Scissors',
    'Lizard',
    'Spock'
]

def check_valid_input(input):
    if input not in options:
        print("Invalide Input")

input = input("What do you choose: ")
return check_valid_input
print("You chose " + input)
print('I choose ', ','.join(random.choices(options)))

#results =
#print(results)