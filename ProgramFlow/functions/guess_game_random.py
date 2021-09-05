import random as ra


def get_integer(prompt):
    """
    Get an integer from standard input (stdin).

    The function keep looping and prompting until a valid
    `int` is entered.

    :param prompt: The string user will see
        when prompted for input
    :return: the `int` user has entered
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print('{} is not a number'.format(temp))


print('-' * 80)
print(get_integer.__doc__)
help(get_integer)
print('-' * 80)

low = 1
high = 10
answer = ra.randint(low, high)
guess = ""
while guess != answer:
    # guess = int(input('Enter a number between: {} - {}'.format(low, high)))
    guess = get_integer('Enter a number between: {} - {}'.format(low, high))
    if guess == -1:
        print('Bye')
        break
    elif guess < answer:
        print('Please guess higher')
    elif guess > answer:
        print('please guess lower')
    elif guess == answer:
        print('you guessed it right')
        break
