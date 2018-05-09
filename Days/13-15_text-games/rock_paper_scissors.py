import random

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

    def can_defeat(self, roll2):
        result = ""
        if self.roll == "Rock":
            if roll2 == "Rock":
                result = "Draw"
            elif roll2 == "Paper":
                result = "Loss"
            elif roll2 == "Scissors":
                result = "Win"
        if self.roll == "Paper":
            if roll2 == "Rock":
                result = "Win"
            elif roll2 == "Paper":
                result = "Draw"
            elif roll2 == "Scissors":
                result = "Loss"
        if self.roll == "Scissors":
            if roll2 == "Rock":
                result = "Loss"
            elif roll2 == "Paper":
                result = "Win"
            elif roll2 == "Scissors":
                result = "Draw"
        return result

def print_header():
    print("--------------------------------------")
    print("          ROCK PAPER SCISSORS         ")
    print("--------------------------------------\n")


def get_players_name():
    player_name = input("Please enter your name: ")
    print()
    return player_name


# Roll the dice to get a weapon
def roll_dice():
    dice = random.randint(1, 3)
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    roll = choices.get(dice)
    return roll


def player_choice():
    roll = ""
    while roll != "r" and roll != "p" and roll != "s":
        roll = input("Please choose [P]aper, [R]ock or [S]cissors.").lower()
        print()
        choices = {
            "r": "Rock",
            "p": "Paper",
            "s": "Scissors"
        }
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
        if outcome == "Win":
            player_score += 1
        elif outcome == "Loss":
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