# Left, Right, Center Dice Game
import random

pot = 0
dice = ['left', 'right', 'center', 'O', 'O', 'O']
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


def player_list():
    print("The players are: ")
    print()
    for i in players:
        print(i)
    print()
    return


def starting_player():
    starting_player = random.choice(players)
    print(f"{starting_player.name} will start")
    return starting_player


def left_player(players, starting_player):
    left_player = players.index(starting_player)-1
    print(f"left {players[left_player].name}")
    return


def dice_roll(players, starting_player):
    global pot, dice
    current_player = starting_player
    left_player = players.index(current_player)-1
    if players.index(current_player) == 0:
        left_player = players[-1]
    right_player = players.index(current_player)+1
    if players.index(current_player) == len(players):
        right_player = players[0]

    if players.chips > 0:
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
                pot += 1
            if roll_result == 'O':
                continue
    elif:
        print(
            f"{current_player.name} has no chips, play will proceed to {left_player.name}")
        return


def play_game():
    assemble_players()
    player_list()
    left_player(players, starting_player())


play_game()
