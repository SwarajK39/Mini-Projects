import random

# define game rules
rules = {
    "rock": "sessior",
    "paper": "rock",
    "sessior": "paper"
}

user_choice = input("Choose rock,paper,sessior : ").lower()


if user_choice not in rules.keys():
    print("Invalid choice!! Please Choose rock,paper,sessior")
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
