def user_number():
    """ Get number from User

    Try until user gives a proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            number = int(input('Please give me the number from 0 to 1000:'))
            break
        except ValueError:
            print('This is not a number!')
    return number


def number_check():
    """ Validate user number

    Try until user gives number between 0 and 1000

    :rtype: int
    :return: provided validated user number as int
    """
    while True:
        number = user_number()
        if 0 <= number <= 1000:
            break
        else:
            print('This is not a number between 1 and 1000')
    return number


def game():
    """ Main function of game """
    low = 0
    high = 1000
    turn = 0
    number = number_check()

    while True:
        computer_number = int(((high - low) / 2) + low)
        turn += 1
        print(f'Is your number is: {computer_number}')
        if number == computer_number:
            print(f'Your number is: {computer_number}! I guess your number in {turn} turns. ')
            break
        if computer_number > number:
            high = computer_number
        if computer_number < number:
            low = computer_number


if __name__ == '__main__':
    game()
