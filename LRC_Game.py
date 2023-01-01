# Left, Right, Center Dice Game
import random

players = []


def pluralizer(number):
    if number == 1:
        return ''
    else:
        return 's'


class Player:
    def __init__(self, name):
        self.__name = name
        self.chips = 3
        self.earnings = 0

    def __str__(self):
        return f"{self.__name}: {self.chips} chip{pluralizer(self.chips)}"

    @property
    def name(self):
        return f"{self.__name}"


def assemble_players():
    how_many_players = int(input("how many people will be playing? "))
    # how_many_players = 5

    for name in random_name(how_many_players):
        players.append(Player(name))
    return


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


def starting_player():
    starting_player = random.choice(players)
    starting_player_index = players.index(starting_player)

    if starting_player_index <= 0:
        left_player = players[-1]
    else:
        left_player = players[starting_player_index-1]

    if starting_player_index == len(players)-1:
        right_player = players[0]
    else:
        right_player = players[starting_player_index+1]

    return starting_player, left_player, right_player


def show_players():
    print("The players are: ")
    print()
    for i in players:
        print(i)
    print()
    return


def rolled_left(current_player, left_player):
    current_player.chips -= 1
    left_player.chips += 1
    return f"{current_player.name} rolled left, gave one chip to {left_player.name}.\n\
        {current_player.name} now has {current_player.chips} chip{pluralizer(current_player.chips)}\n"


def rolled_right(current_player, right_player):
    current_player.chips -= 1
    right_player.chips += 1
    return f"{current_player.name} rolled right, gave one chip to {right_player.name}.\n\
        {current_player.name} now has {current_player.chips} chip{pluralizer(current_player.chips)}\n"


def rolled_center(current_player, center_pot):
    current_player.chips -= 1
    center_pot += 1
    return f"{current_player.name} rolled center, put one chip in the center.\n\
        {current_player.name} now has {current_player.chips} chip{pluralizer(current_player.chips)}\n"


def rolled_O(current_player):
    return f"{current_player.name} rolled O and got to keep a chip.\n\
        {current_player.name} now has {current_player.chips} chip{pluralizer(current_player.chips)}\n"


def check_chips():
    chip_checker = []
    for i in players:
        if i.chips > 0:
            chip_checker.append(i.chips)
    return len(chip_checker) == 1


def dice_roll(players):
    center_pot = 0
    turn_counter = 0
    dice = ['left', 'right', 'center', 'O', 'O', 'O']
    verbose = ""

    current_player, left_player, right_player = starting_player()
    print(f"{current_player.name} will start")

    full_story = input(
        "Would you like to see how the game goes? [Y]es, show me every turn, or, [N]o just show me the results. ")

    while True:
        if check_chips():
            winner = max((i for i in players), key=lambda x: x.chips)
            winner.chips = len(players) * 3
            print(f"The game ended after {turn_counter} turns.")
            print(
                f"{winner.name} has won! They will take the pot.\n")
            if full_story.lower() == 'y':
                print(verbose)
            break

        if current_player.chips > 0:
            turn_counter += 1
            verbose += f"\nTurn {turn_counter}: {current_player.name} to roll.\n"
            roll_count = 0
            for _ in range(current_player.chips):
                roll_count += 1
                roll_result = random.choice(dice)
                if roll_result == 'left':
                    verbose += rolled_left(current_player, left_player)
                if roll_result == 'right':
                    verbose += rolled_right(current_player, right_player)
                if roll_result == 'center':
                    verbose += rolled_center(current_player, center_pot)
                if roll_result == 'O':
                    verbose += rolled_O(current_player)
                if roll_count >= 3:
                    break

            current_player = players[players.index(current_player)-1]
            left_player = players[players.index(left_player)-1]
            right_player = players[players.index(right_player)-1]

        elif current_player.chips == 0:
            turn_counter += 1
            verbose += f"\nTurn {turn_counter}: {current_player.name} to roll.\n"
            verbose += f"{current_player.name} has no chips. Play proceeds to {left_player.name}.\n"
            current_player = players[players.index(current_player)-1]
            left_player = players[players.index(left_player)-1]
            right_player = players[players.index(right_player)-1]


def play_game():
    assemble_players()
    show_players()
    dice_roll(players)
    show_players()


play_game()
