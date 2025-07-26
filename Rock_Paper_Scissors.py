import random
print ("Rock, Paper, Scissors...Shoot! You ready?")

# Player's name
while True:
    name = input("Let's start with an introduction. How would you like to be addressed? Enter your name: ")
    if name == "":
        print("Without a name the game ends here...your choice")
    else:
        print(f"Ok, {name} now its my turn.")
        break

#Name me
while True:
    computer = input("What would you like to call me?: ")
    if computer == "":
        print(f"Come on {name}. You can do better than that.")
    elif computer == name:
        print("Playing with yourself? This isn't Rock, Paper, Sadness.")
    else:
        print(f"Hey {name}, I'm {computer}.")
        break

# Are you ready?
while True:
    start_game = input("Ready to lose? (yes/no): ").lower()
    if start_game == "yes":
         print(f"Alright {name} game on!")  
         break
    elif start_game == "no":
        print("I knew you weren't ready")
        exit()
    else:
        print(f"{name} follow directions. You have to type 'yes' or 'no'.")
        
# Game time

player_score = 0
computer_score = 0
game_choices = ["rock", "paper", "scissors"]

while player_score < 3 and computer_score < 3:
    print("\nRock, Paper, Scissors, SHOOT!")

# Player's selection

player_choice = ''
while player_choice not in game_choice:
    player_choice = input(f"{name} (rock, paper, or scissors): ").lower()
    print(f"{name}, that’s not how the game works. Try again.")
        

computer_choice = random.choice(game_choices)
print(f"\n{name} chose: {player_choice}, I chose: {computer_choice}. \n")

# Element relations

if player_choice == computer_choice:
    tie_statement = ["Get out of my head!", 
                    "Bet you can't do that again...", 
                    "Twins!!!"]
    print(random.choice(tie_statement))

elif (player_choice == "rock" and computer_choice == "scissors") or\
    (player_choice == "scissors" and computer_choice == "paper") or\
    (player_choice == "paper" and computer_choice == "rock"):
    win_reactions = {
        "rock": ["...You win this round", 
                "So you're the Hulk now?", 
                "Rock crushes....I should have picked paper."],
        "scissors": ["OUCH!",
                    "Call me confetti",
                    "Good job."],
        "paper": ["Stick a bow on me, cause you wrapped me up",
                "You earned that one",
                "You've been practicing, haven't you?...Don't answer that"]
    }
    print(random.choice(win_reactions[player_choice]))
    player_score += 1
else:
    lose_reactions = {
        "rock": ["I cover yoooouuu!",
                "Paper for the win!",
                f"Point {computer}"],
        "scissors": ["Smash",
                    "Give me a point",
                    "Back to the drawing board for you."],
        "paper": ["You did not make the...CUT!",
                "HA! Try again.",
                "Like a hot knife through butter"]
    }
    print(random.choice(lose_reactions[player_choice]))
    computer_score += 1

# Score Display
print(f"{name} score: {player_score} | {computer} score: {computer_score}")
                
# Keeping Score

if player_choice == computer_choice:
    result = "tie"
elif (player_choice == "rock" and computer_choice == "scissors") or \
    (player_choice == "scissors" and computer_choice == "paper") or \
    (player_choice == "paper" and computer_choice == "rock"):
    result = "player_choice"
else:
    result = "computer_choice"

if result == "player_choice":
    player_score += 1
elif result == "computer_choice":
    computer_score += 1
print(f"{name} score: {player_score} | {computer} score: {computer_score}")

# Outcome

if player_score >= 3 and player_score > computer_score:
    print(f"{name} won!")
elif computer_score >= 3 and computer_score > player_score:
    print(f"{computer}'s the winner!")
else:
    print("No one wins in a tie, let's go again!")

