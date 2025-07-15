import random
import csv
import os
import matplotlib.pyplot as plt


            #### GAME LOGIC ####

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
        print("\nYou have 5 rounds to beat the game!\nRemember, rock beats scissors, paper beats rock, and scissors beats paper.\n")
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


            #### FILE IO ####

newUser = [username, print_score]
header = ['Username', 'High Score']
game_scores = []

if not os.path.exists('game_scores.csv'):
    with open('game_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)


with open('game_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    user_found = False
    for row in reader:
        if row['Username'] == username:
            user_found = True
            # access the users score value
            current_score = float(row['High Score'])
            #if new score is greater than existing score then replace with the new score
            if print_score > current_score:
                row['High Score'] = str(print_score)
        game_scores.append(row)

if not user_found:
    game_scores.append({'Username': username, 'High Score': print_score})

with open('game_scores.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(game_scores)


            #### DATA VIS ####

usernames = []
score = []

# Put the usernames and scores into lists
with open('game_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        usernames.append(row['Username'])
        score.append(float(row['High Score']))

# Displays a bar chart
plt.bar(usernames, score)
plt.xlabel("Username")
plt.ylabel("Scores")
plt.title("Leaderboard Ranking")
plt.show()
