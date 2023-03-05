import random


def get_number():
    """ Get number from User

    Try until user gives a proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            user_number = int(input('Guess the number:'))
            break
        except ValueError:
            print('This is not a number!')
    return user_number


def guess_number():
    """ Main game function."""
    user = get_number()
    random_number = random.randint(1,100)
    while user != random_number:
        if user < random_number:
            print('Too small')
        if user > random_number:
            print('Too big')
        user = get_number()
    print('You win game')


if __name__ == '__main__':
    guess_number()
