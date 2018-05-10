# Advanced version of the Rock Paper Scissors game
# Uses 15 different weapons


import random
import csv

# Choices of weapons
choices = {
            1: "Rock",
            2: "Gun",
            3: "Lightning",
            4: "Devil",
            5: "Dragon",
            6: "Water",
            7: "Air",
            8: "Paper",
            9: "Sponge",
            10: "Wolf",
            11: "Tree",
            12: "Human",
            13: "Snake",
            14: "Scissors",
            15: "Fire"
        }


# Name the player
class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# Get a roll, random or chosen
class Roll:
    def __init__(self, roll=None):
        self.roll = roll

    def get_roll(self):
        return self.roll

# Determines if the player has won or lost, or if it's a draw
# self and roll2 are strings
# Checks  what the outcome is in the csv
    def can_defeat(self, roll2):
        with open('battle-table.csv') as fin:
            reader = list(csv.DictReader(fin))
            attackers = {}
            count = 0
            for attacker in reader[0]:
                if attacker == "Attacker":
                    continue
                attackers[attacker] = count
                count += 1

            result = reader[attackers[self.roll]][roll2]

        return result


def print_header():
    print("--------------------------------------")
    print("          ROCK PAPER SCISSORS         ")
    print("           ADVANCED EDITION           ")
    print("--------------------------------------\n")


def get_players_name():
    player_name = input("Please enter your name: ")
    print()
    return player_name


# Roll the dice to get a weapon
def roll_dice():
    dice = random.randint(1, 15)
    roll = choices.get(dice)
    return roll

# User is given a list of weapons to choose from.
# Returns a string of the weapon chosen by entering an int
def player_choice():
    roll = 0
    while not (0 < roll < 16):
        try:
            roll = int(input("Please choose a weapon :\n"
                             "1-Rock\n2-Gun\n3-Lightning\n4-Devil\n5-Dragon\n"
                             "6-Water\n7-Air\n8-Paper\n9-Sponge\n10-Wolf\n"
                             "11-Tree\n12-Human\n13-Snake\n14-Scissors\n15-Fire\n"
                             "Choice: "))
        except ValueError:
            print("Please enter a valid choice. Press Enter to choose again.")
            input()
            continue
        print()
        choice = choices.get(roll)
    return choice

def game_loop(player1, player2):
    done = True
    player_score = 0
    computer_score = 0
    while done:
        p1_choice = player_choice()
        p2_roll = Roll(roll_dice()).get_roll()
        p1_roll = Roll(p1_choice).get_roll()

        outcome = Roll(p1_choice).can_defeat(p2_roll)

        print("{} used {} againt {}, who used {}.\n".format(player1, p1_roll,
                                                        player2, p2_roll))
        print("The result is a {}!\n".format(outcome))
        if outcome == "win":
            player_score += 1
        elif outcome == "loss":
            computer_score += 1
        print(f"The score is: {player1} {player_score} points | {player2} "
              f"{computer_score} points.")

        if player_score == 3 or computer_score == 3:
            break
        print("Time to play another round!\n")

    if player_score == 3:
        print("{} has won the game!\n".format(player1))
    elif computer_score == 3:
        print("{} has won the game!\n".format(player2))

def main():
    done = True
    while done:
        print_header()

        name = get_players_name()

        player1 = Player(name).get_name()
        player2 = Player("The Computer").get_name()

        game_loop(player1, player2)

        print()
        print("Would you like to play another game?")
        another_game = input("Please enter Y or N.").lower()
        if another_game == "y":
            continue
        elif another_game == "n":
            done = False


    print("Thanks for playing!!! Goodbye!")
if __name__ == '__main__':
    main()