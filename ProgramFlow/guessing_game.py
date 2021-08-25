answer = 5

guess = int(input("Enter a guess between 1-10: "))

if guess < answer:
    print('guess higher')
    guess = int(input("guess higher: "))
    if guess == answer:
        print('you guessed it')
elif guess > answer:
    print('guess lower')
    guess = int(input("guess lower: "))
    if guess == answer:
        print('you guessed it')
else:
    print('guess right first time')
