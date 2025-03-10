import random

opts = ["rock", "paper", "scissors"]

to_guess = random.choice(opts)
l_to_guess = to_guess.lower()

guess = input("Choose rock, paper, or scissors: ")
l_guess = guess.lower()

counter = 0


while(counter <= 6):

    if(l_to_guess=="rock"):
        elif(l_guess=="rock"):
            print("You lost!")
        elif (l_guess == "scissors"):
            print("You lost!")
        elif (l_guess == "paper"):
            print("You won!")

    if(l_to_guess=="paper"):
        if(l_guess=="paper"):
            print("You lost!")
        if (l_guess == "rock"):
            print("You lost!")
        if (l_guess == "scissors"):
            print("You won!")


    if(l_to_guess=="scissors"):
        if(l_guess=="paper"):
            print("You lost!")
        if (l_guess == "scissors"):
            print("You lost!")
        if (l_guess == "rock"):
            print("You won!")

    if(l_to_guess not in opts):
        print("Please type rock, paper, or scissors.")

    counter += 1

