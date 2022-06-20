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

randompick = ','.join(random.choices(options))
usrinput = str(input())


def check_valid_input(input):
    if usrinput not in options:
        print("Invalide Input")

input = input("What do you choose: ")
print (check_valid_input())

print("You chose " + input)
print('I choose ', randompick)

#results =
#print(results)