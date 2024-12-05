import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = (random.choice(word_list))
num = len(chosen_word)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in chosen_word:
    display.append("_")
print(display)


is_alive = True
while is_alive:
    lives = 6
    guess = input("guess a letter: ").lower()
    for j in range(num):
        if "_" in display:
            pass
        else:
            print("you won!")

        for i in range(num):
            letter = chosen_word[i]
            if guess == letter:
                display[i] = letter 
            else:
                lives -= 1
                pass
        if lives == 0:
            is_alive = False
            print("game over! you lose")
    print(display)
