parrot = "Norwegian Blue"
letter = input('Enter a char: ')

if letter in parrot:
    print('it is in there')
else:
    print('not there')


activity = input("What would you like to do today? ")
# I want to go to Cinema
if "cinema" not in activity.casefold():  # casefold handles some languages better
    print("But I want to go to the cinema")