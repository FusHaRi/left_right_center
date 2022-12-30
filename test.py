import random


def dice_roll(players, starting_player):
    global center_pot, dice
    current_player = players.index(starting_player)
    left_player = players.index(current_player)-1
    if players.index(current_player) == 0:
        left_player = players[-1]
    right_player = players.index(current_player)+1
    if players.index(current_player) == len(players):
        right_player = players[0]

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


if __name__ == "__main__":

    players = ['Wally', 'Charles', 'Carol', 'Astrid', 'Joe']
    starting_player = 'Joe'

    current_player_index = players.index(starting_player)
    current_player = players[current_player_index]

    if current_player_index == 0:
        left_player = players[-1]
    else:
        left_player = players[current_player_index-1]

    if current_player_index == len(players)-1:
        right_player = players[0]
    else:
        right_player = players[current_player_index+1]

    print(
        f"left: {left_player}, starter: {current_player}, right: {right_player}")
