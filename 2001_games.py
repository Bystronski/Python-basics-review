from Game_cube import game


def points_add(points):
    """ Calculate points

    :rtype: int
    :return: new_points
    """

    roll = game('2D6')
    if roll == 7:
        points /= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points


def game_2001():
    """ Game 2001 """
    user_points = 0
    computer_points = 0

    input('Press ENTER to next turn')
    user_points += game("2D6")
    computer_points += game("2D6")

    while user_points < 2001 and computer_points < 2001:
        print(f'User points: {user_points}\nComputer points: {computer_points}')
        input('Press ENTER to next turn')
        user_points += int(points_add(user_points))
        computer_points += int(points_add(computer_points))

    print(f'User points: {user_points}\nComputer points: {computer_points}')
    if computer_points > user_points:
        print('Computer win')
    elif user_points > computer_points:
        print('You win')
    else:
        print('Draw')


if __name__ == '__main__':
    game_2001()