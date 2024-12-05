import random
import os
import platform

from game_data import data
from art import logo

print(logo)

def clear():
    if platform.system()=='windows':
        os.system('cls')

# Format account data into printable format.
def account_data(account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    return f"{account_name}; {account_description}; {account_country}"

account_b=random.choice(data)
score = 0
winning=True
while winning:
    # Generate a random account from the game data.
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"compare A:  {account_data(account_a)}")
    from art import vs
    print(vs)
    print(f"Against B: {account_data(account_b)}")

    # Ask user for a guess.

    # Check if user is correct.
    ## Get follower count.
    ## If Statement

    count_a=int(account_a['follower_count'])
    count_b=int(account_b['follower_count'])

    # Score Keeping.
    # Make game repeatable.

    guess = input("Guess who have more followers. Type 'A' or 'B': ").lower()
    def game(guess_who):
        if count_a > count_b and guess == 'a':
            global score
            score += 1
            print(f"you are correct.your current score is {score}")
        elif count_b > count_a and guess == 'b':
            score += 1
            print(f"you are correct.your current score is {score}")
        else:
            winning = False
            print(f"you lose! Game over.your final score is {score}")
        print(f"your score is {score}")
    game(guess)

    clear()


# Feedback.



# Make B become the next A.

# Clear screen between rounds.