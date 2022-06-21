import random

## The first thing destroyes the second thing
rules = {   "Scissors": ["Paper", "Lizard"], 
            "Paper": ["Rock", "Spock"], 
            "Rock": ["Lizard", "Scissors"], 
            "Lizard": ["Spock", "Paper"],
            "Spock" : ["Scissors", "Rock"],
            }

options = [
    'Rock',
    'Paper',
    'Scissors',
    'Lizard',
    'Spock'
]

restart = True
while restart == True:
    restart = False
    usrinput = input("What do you choose: ")
    randompick = ','.join(random.choices(options))


    if usrinput not in options:
        print("Invalide Input")
        restart = True

    else:
        print("You chose " + usrinput)
        print('I choose ', randompick)
        restart = False    
        if usrinput in ','.join(rules.get(randompick)):
            print("You LOSE")
        else:
            if randompick == usrinput:
                print("DRAW")
            else:
                print("You WIN")
    restart = True