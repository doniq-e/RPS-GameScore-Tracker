import random
import csv
import os
import plotly.express as px


            #### GAME LOGIC ####

opts = ["rock", "paper", "scissors"]

print("Hello! Welcome to rock, paper, scissors!\nType 'help' to see the rules!")

score = 0
counter = 0

# Input a name
username = input("Please enter your name: ")

while counter < 5:
# Input a Guess
    guess = input("\nChoose 'rock', 'paper', 'scissors', or 'help': ")
    l_guess = guess.lower()

    to_guess = random.choice(opts)
    l_to_guess = to_guess.lower()

# Help Menu
    if l_guess == "help":
        print("\nYou have 5 rounds to beat the game!\nRemember, rock beats scissors, paper beats rock, and scissors beats paper.\n")
        continue
# Invalid Guess
    if l_guess not in opts:
        print("\nPlease type rock, paper, or scissors.")
        continue

    print("Your opponent says: " + l_to_guess)

# If the input is Rock
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

# If the input is Paper
    if l_to_guess=="paper":
        if l_guess=="paper":
            print("It's a tie this round!")
            score += 0.5
        if l_guess == "rock":
            print("You lost this round!")
        if l_guess == "scissors":
            print("You won this round!")
            score += 1

# If the input is Scissors
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

# Calculates your final score
print_score = score * 100
print("Final score for "+ username +": " + str(print_score) + "\nSee you next time!")


            #### FILE I/O ####

newUser = [username, print_score]
header = ['Username', 'High Score']
game_scores = []

# Creates the header of the csv file
if not os.path.exists('game_scores.csv'):
    with open('game_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

# Determines if the username already exists and thus only the score should be updated for that username, if needed
# If the username does not exist, then the new username and score will be added to the CSV
with open('game_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    user_found = False
    for row in reader:
        if row['Username'] == username:
            user_found = True
            # access the users score value
            current_score = float(row['High Score'])
            #If the new score is greater than existing score then replace it with the new score
            if print_score > current_score:
                row['High Score'] = str(print_score)
        game_scores.append(row)

if not user_found:
    game_scores.append({'Username': username, 'High Score': print_score})

# Adds score to CSV (if applicable)
with open('game_scores.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(game_scores)


            #### DATA VISUALIZATION ####

usernames = []
score = []

# Put the usernames and scores into lists
with open('game_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        usernames.append(row['Username'])
        score.append(float(row['High Score']))

# Create a bar chart using plotly
leaderboard = px.bar(
    x=usernames,
    y=score,
    title='🏆 Leaderboard 🏆',
    labels={'x': 'Username', 'y': 'Score'},
    color=score,
    text=score
)

# Customize the bar chart
leaderboard.update_layout(
    xaxis=dict(
        title_font=dict(size=18, weight='bold'),
    ),
    yaxis=dict(
        title_font=dict(size=18, weight='bold')
    ),
    title=dict(
        text='🏆 Leaderboard 🏆',
        font=dict(size=25, weight='bold'),
        x=0.5,
        xanchor="center"
    ),
    plot_bgcolor='#F1E7F8'
)

# Show the chart
leaderboard.show()
