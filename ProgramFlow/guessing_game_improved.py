from multiprocessing.connection import answer_challenge

answer = 5

guess = int(input("Enter a guess between 1-10: "))
#
# if guess < answer:
#     print('guess higher')
#     guess = int(input("guess higher: "))
#     if guess == answer:
#         print('you guessed it')
# elif guess > answer:
#     print('guess lower')
#     guess = int(input("guess lower: "))
#     if guess == answer:
#         print('you guessed it')
# else:
#     print('guess right first time')

if guess != answer:
    if guess < answer:
        print('guess higher')
    else:
        print('guess lower')
    guess = int(input('guess a number'))
    if guess == answer:
        print('guessed right second time')
    else:
        print('guessed incorrectly')
else:
    print('guessed correct first time')

