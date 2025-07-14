import random
import csv
import os

opts = ["rock", "paper", "scissors"]

print("Hello! Welcome to rock, paper, scissors!\nType 'help' to see the rules!")

score = 0
counter = 0

username = input("Please enter your name: ")

while counter < 5:
    guess = input("\nChoose 'rock', 'paper', 'scissors', or 'help': ")
    l_guess = guess.lower()

    to_guess = random.choice(opts)
    l_to_guess = to_guess.lower()

    if l_guess == "help":
        print("\nYou have 6 rounds to beat the game!\nRemember, rock beats scissors, paper beats rock, and scissors beats paper.\n")
        continue

    if l_guess not in opts:
        print("\nPlease type rock, paper, or scissors.")
        continue

    print("Your opponent says: " + l_to_guess)

    if l_to_guess == "rock":
        if l_guess == "rock":
            print("It's a tie this round!")
            # IF IT'S A TIE THE PLAYER GETS 0.5 POINTS
            score += 0.5
        if l_guess == "scissors":
            print("You lost this round!")
        if l_guess == "paper":
            print("You won this round!")
            score += 1

    if l_to_guess=="paper":
        if l_guess=="paper":
            print("It's a tie this round!")
            score += 0.5
        if l_guess == "rock":
            print("You lost this round!")
        if l_guess == "scissors":
            print("You won this round!")
            score += 1

    if l_to_guess=="scissors":
        if l_guess=="paper":
            print("You lost this round!")
        if l_guess == "scissors":
            print("It's a tie this round!")
            score += 0.5
        if l_guess == "rock":
            print("You won this round!")
            score += 1

    counter += 1
    print("\nYour remaining attempts: " + str(5 - counter)+"\n")

print_score = score * 100
print("Final score for "+ username +": " + str(print_score) + "\nSee you next time!")

newUser = [username, print_score]
header = ['Username', 'High Score']

if not os.path.exists('game_scores.csv'):
    with open('game_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

with open('game_scores.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(newUser)

with open('game_scores.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#usernames = []
#score = []


