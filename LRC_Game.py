# Left, Right, Center Dice Game
import random

center_pot = 0
players = []


class Player:
    def __init__(self, name):
        self.__name = name
        self.chips = 3

    def __str__(self):
        return f"{self.__name}: {self.chips} chips"

    @property
    def name(self):
        return f"{self.__name}"


def random_name(number):
    dupe_checker = []
    options = open('names.txt').read().splitlines()

    while True:
        name = random.choice(options)
        if name in dupe_checker:
            continue
        else:
            dupe_checker.append(name)

        if len(dupe_checker) >= number:
            break
    return dupe_checker


def assemble_players():
    how_many_players = int(input("how many people will be playing? "))
    for name in random_name(how_many_players):
        players.append(Player(name))
    return


def show_players():
    print("The players are: ")
    print()
    for i in players:
        print(i)
    print()
    print(f"There are {center_pot} chips in the middle.")
    return


def starting_player():
    starting_player = random.choice(players)
    starting_player_index = players.index(starting_player)

    if starting_player_index < 0:
        starting_player_index == len(players)-1
    else:
        starting_player = players[starting_player_index]

    if starting_player_index <= 0:
        left_player = players[-1]
    else:
        left_player = players[starting_player_index-1]

    if starting_player_index == len(players)-1:
        right_player = players[0]
    else:
        right_player = players[starting_player_index+1]

        return starting_player, left_player, right_player


def dice_roll(players):
    global center_pot
    dice = ['left', 'right', 'center', 'O', 'O', 'O']

    current_player, left_player, right_player = starting_player()
    print(f"{current_player.name} will start")

    while True:
        if current_player.chips > 0:
            for _ in range(current_player.chips):
                roll_result = random.choice(dice)
                if roll_result == 'left':
                    current_player.chips -= 1
                    left_player.chips += 1
                if roll_result == 'right':
                    current_player.chips -= 1
                    right_player.chips += 1
                if roll_result == 'center':
                    current_player.chips -= 1
                    center_pot += 1
                if roll_result == 'O':
                    continue

        elif current_player.chips == 0:
            print(
                f"{current_player.name} has no chips, play will proceed to {left_player.name}")
            current_player = players[players.index(current_player)-1]
            left_player = players[players.index(left_player)-1]
            right_player = players[players.index(right_player)-1]

        if check_chips():
            print("The game is over")
            show_players()
            print(
                f"{max((i for i in players), key=lambda x:x.chips)} has won! They take the pot")
            break


def check_chips():
    chip_checker = []
    for i in players:
        if i.chips > 0:
            chip_checker.append(i.chips)
    return len(chip_checker) == 1


def play_game():
    assemble_players()
    show_players()
    dice_roll(players)
    show_players()


play_game()
