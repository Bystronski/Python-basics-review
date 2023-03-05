import random


def get_number():
    """ Get number from User

    Try until user gives a proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            user_number = int(input('Get the number from 1 to 49:'))
            break
        except ValueError:
            print('This is not a number!')
    return user_number


def add_to_list():
    """ Add to list user number

    Try to add to list if user number meets condition.

    :rtype: list
    :return: given list of six number by user
    """
    result = []
    while len(result) != 6:
        number = get_number()
        if 1 <= number <= 49:
            if number not in result:
                result.append(number)
            else:
                print('The same number in your list!')
        else:
            print('This is not a number between 1 to 49!')
    return result


def print_numbers(numbers):
    """Print given numbers with ascending order.

    :param list numbers: list of numbers
    """
    print(", ".join(str(number) for number in sorted(numbers)))


def lotto_simulator():
    """ Main function of game """
    user_numbers = sorted(add_to_list())
    computer_numbers = sorted([random.randint(1, 49) for i in range(1, 6)])
    hit_number = 0
    for user_number in user_numbers:
        if user_number in computer_numbers:
            hit_number += 1
    print('Your numbers:')
    print_numbers(user_numbers)
    print('Lotto numbers:')
    print_numbers(computer_numbers)
    print(f'You hit {hit_number} numbers!')


if __name__ == '__main__':
    lotto_simulator()
