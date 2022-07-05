import random
import time

print("Welcome to Random Monster Fighter!")
time.sleep(2)
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
""")
time.sleep(2)
start = input("Fight a monster? (y/n)")

monster_names = ('Godzilla', 'King Kong', 'Noseferatu', 'Kraken', 'Hydra')

min_monster_lvl = 1
max_monster_lvl = 20

min_roll = 1
max_roll = 20

win_streak = 0

while start == "yes" or start == "y":
    monster_lvl = random.randint(min_monster_lvl, max_monster_lvl)
    monster_name = random.choice(monster_names)

    print(f"A level {monster_lvl} {monster_name} has been summoned!")
    time.sleep(2)
    print(f"Roll higher than a {monster_lvl} to defeat {monster_name}!")
    time.sleep(2)
    roll_now = input("Roll your D20? (y/n)")
    time.sleep(2)
    if roll_now == "yes" or roll_now == "y":
        roll = random.randint(min_roll, max_roll)
        print(f"You rolled a {roll}!")
        time.sleep(2)
        if roll >= monster_lvl:
            print(f"You have successfully defeated {monster_name}!")
            time.sleep(2)
            win_streak += 1
            print(f"Win streak: {win_streak}")
        else:
            print(f"{monster_name} has won the fight!")
            time.sleep(2)
            win_streak = 0
            print(f"Win Streak: {win_streak}")
    else:
        print(f"By forfeiting your roll you have surrendered to {monster_name}.")
        time.sleep(2)
        win_streak = 0
        print(f"Win streak: {win_streak}")
    time.sleep(2)

    start = input("Would you like to fight another monster? (y/n)")
