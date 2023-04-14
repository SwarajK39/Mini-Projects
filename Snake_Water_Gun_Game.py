# water snake gun game python

import random

# define game rules
rules = {
    "snake": "water",
    "water": "gun",
    "gun": "snake"
}

user_choice = input("Choose snake,water,gun : ").lower()

if user_choice not in rules.keys():
    print("Invalid choice!! Please Choose snake,water,gun")
    exit()

# generate computer choice

computer_choice = random.choice(list(rules.keys()))

# print the choices

print("you chose :- ", user_choice)
print("computer chose :- ", computer_choice)

if user_choice == computer_choice:
    print("It's tie!")

else:
    if rules[user_choice] == computer_choice:
        print("You Win!")

    else:
        print("Computer wins!")
