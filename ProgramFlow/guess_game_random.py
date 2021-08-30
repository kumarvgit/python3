import random as ra
low = 1
high = 10
answer = ra.randint(low, high)
guess = ""
while guess != answer:
    guess = int(input('Enter a number between: {} - {}'.format(low, high)))
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
