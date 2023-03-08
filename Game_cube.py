import random
import re

DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")

games_cube = (
    '3',
    '4',
    '6',
    '8',
    '10',
    '12',
    '20',
    '100'
)


def game(cube_code):
    """ Calculate dice roll from dice pattern.

    :param str cube_code: game cube pattern ex. `7D12-5`
    :rtype: int, str
    :return: game cube roll value for proper dice pattern
    """

    match = DICE_PATTERN.search(cube_code)
    if not match:
        return 'Wrong input'

    multiply, dice, modifier = match.groups()
    if dice not in games_cube:
        return "Wrong Input"

    multiply = int(multiply) if multiply else 1
    dice = int(dice)
    modifier = int(modifier) if modifier else 0

    return sum([random.randint(1, dice) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(game("2D10+10"))
    print(game("D6"))
    print(game("2D3"))
    print(game("D12-1"))
    print(game("DD34"))
    print(game("4-3D6"))
