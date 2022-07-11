import random #Importing the random library to use for the dice rolls
import time #importing time to use for sleep functions

print("Welcome to Random Monster Fighter!") #Welcoming the user to my game
time.sleep(2) #The first of many sleep functions. I use sleep functions to pace the output of the code so everything does not print all at once
print("""
   RANDOM              |>>>
    MONSTER             |
     FIGHTER        _  _|_  _
                   |;|_|;|_|;|
                   \.    .  /
                    \:  .  /
                     ||:   |
                     ||:.  |
                     ||:  .|
                     ||:   |
                    _||_   |
            __ ----~        ~`---,            
        --~'                     ~~----_____
""") #Found a text design of a castle online and scaled it down to my liking. Just wanted to add a bit of style to the game
time.sleep(2)
start = input("Fight a monster? (y/n)") #Start variable to gather user input on if they would like to start the game(fight a moster)

monster_names = ('Godzilla', 'King Kong', 'Noseferatu', 'Kraken', 'Hydra') #String list of monster names

min_monster_lvl = 1 #Minimum level a monster could be
max_monster_lvl = 20 #Maximum level a monster could be

min_roll = 1 #Minimum value a dice roll could be
max_roll = 20 #Maximum value a dice roll could be

win_streak = 0 #Initializing the win streak variable

while start == "yes" or start == "y": #While loop to initiate the start of the game
    monster_lvl = random.randint(min_monster_lvl, max_monster_lvl) #Initializing the mosters level with random
    monster_name = random.choice(monster_names) #Initializing the monsters name from the list with random

    print(f"A level {monster_lvl} {monster_name} has been summoned!") #F print to tell the user the monsters level and name that has been summoned
    time.sleep(2)
    print(f"Roll higher than a {monster_lvl} to defeat {monster_name}!") #F print to tell the user how to defeat the monster
    time.sleep(2)
    roll_now = input("Roll your D20? (y/n)") #Varable to gather input from the user on if they would like to roll against the monster
    time.sleep(2)
    if roll_now == "yes" or roll_now == "y": #If statement for if the user inputs yes or y
        roll = random.randint(min_roll, max_roll) #Deciding the users roll with random
        print(f"You rolled a {roll}!") #F print to show what the user has rolled
        time.sleep(2)
        if roll >= monster_lvl: #If statement for if the roll value is higher than the monsters level
            print(f"You have successfully defeated {monster_name}!") #F print to tell the user they have defeated the monster
            time.sleep(2)
            win_streak += 1 #adding 1 to the users win streak
            print(f"Win streak: {win_streak}") #F print to tell the user their current win streak after their battle
        else: #Else statement for if the roll value is less than the monsters level
            print(f"{monster_name} has won the fight!") #F print to tell the user the monster has won the fight
            time.sleep(2)
            win_streak = 0 #Resets the users win streak to 0
            print(f"Win Streak: {win_streak}") #F print to tell the user their win streak
    else: #Else statnent for if the user inputs anything other than yes or y for the roll now variable
        print(f"By forfeiting your roll you have surrendered to {monster_name}.") #F print to tell the user they have surrendered their roll and let the monster win
        time.sleep(2)
        win_streak = 0 #Resets the users win streak to 0
        print(f"Win streak: {win_streak}") #F print to tell the user their win streak
    time.sleep(2)

    start = input("Would you like to fight another monster? (y/n)") #Altering the original start variable to ask if the user would like to play again after their last match
