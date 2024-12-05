import random

print("welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
answer=random.randint(1,100)

hard=5
easy=10
turns=0

level = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
def difficulty():
    if level =='easy':
      return easy
    else:
        return hard

turns=difficulty()
get_answer=True
while get_answer:
    print(f"you have {turns} attempts remaining to guess the number")
    guess=int(input("Make a guess: "))
    def check_answer(guess,answer,turns):
        if guess < answer:
            print("Too low.")
            return turns-1
        elif guess > answer:
            print("Too high.")
            return turns-1
        else:
            print(f"you got the it.The answer was {answer}")

    turns = check_answer(guess, answer, turns)

    if turns==0:
        get_answer=False
        print("you have no attempting remaining you lost!")


