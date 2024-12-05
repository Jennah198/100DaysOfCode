print("welcome to paper , rock , scissors game!")
import random

list = ["rock","paper","scissors"]
ran = random.choice(list)
print(ran)

user=input("choose one.Rock,Paper,Scissors: ").lower()
if user == ran:
    print("draw")
elif user == "paper" and ran == "rock":
    print("you won!")
elif user == "scissors" and ran == "paper":
    print("you won!")
elif user == "rock" and ran == "scissors":
    print("you won!")
else:
    print("you lose!")