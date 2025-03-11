import random

opts = ["rock", "paper", "scissors"]

print("Hello! Welcome to rock, paper, scissors!\nType 'help' to see the rules!")

score = 0
counter = 0

while counter < 6:
    guess = input("\nChoose rock, paper, or scissors: ")
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
            print("You lost this round!")
        if l_guess == "scissors":
            print("You lost this round!")
        if l_guess == "paper":
            print("You won this round!")
            score += 1

    if l_to_guess=="paper":
        if l_guess=="paper":
            print("You lost this round!")
        if l_guess == "rock":
            print("You lost this round!")
        if l_guess == "scissors":
            print("You won this round!")
            score += 1

    if l_to_guess=="scissors":
        if l_guess=="paper":
            print("You lost this round!")
        if l_guess == "scissors":
            print("You lost this round!")
        if l_guess == "rock":
            print("You won this round!")
            score += 1

    counter += 1
    print("\nYour remaining attempts: " + str(6 - counter)+"\n")

printsc = score * 100
print("Your final score is: " + str(printsc) + "\nSee you next time!")
