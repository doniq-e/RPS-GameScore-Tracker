import random

opts = ["rock", "paper", "scissors"]

to_guess = random.choice(opts)

guess = input("Choose rock, paper, or scissors.")

if(to_guess == guess):
    print("You lost!")
