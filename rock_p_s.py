import random

opts = ["rock", "paper", "scissors"]

to_guess = random.choice(opts)
#print(to_guess)

guess = input("Choose rock, paper, or scissors: ")

#if(to_guess == guess):
  #  print("You lost!")

if(to_guess=="rock"):
    if(guess=="rock"):
        print("You lost!")
    if (guess == "scissors"):
        print("You lost!")
    if (guess == "paper"):
        print("You won!")

if(to_guess=="paper"):
    if(guess=="paper"):
        print("You lost!")
    if (guess == "rock"):
        print("You lost!")
    if (guess == "scissors"):
        print("You won!")


if(to_guess=="scissors"):
    if(guess=="paper"):
        print("You lost!")
    if (guess == "scissors"):
        print("You lost!")
    if (guess == "rock"):
        print("You won!")

if(guess not in opts):
    print("Please type rock, paper, or scissors.")

