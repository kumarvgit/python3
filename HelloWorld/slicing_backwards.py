letters = 'abcdefghijklmnopqrstuvwxyz'

# include the 0th index
backwards = letters[25::-1]
print(backwards)

# this will reverse the string and is common python idiom
backwards = letters[::-1]
print(backwards)

# qpo
backwards = letters[16:13:-1]
print('qpo: ' + backwards)

# edbca
backwards = letters[4::-1]
print('edbca: ' + backwards)

# last 8 letters
backwards = letters[:17:-1]
print('zyxwvuts: ' + backwards)


# Common python idioms
# return last n chars in python, here start and stop value is default
# If it starts with negative value
print(letters[-4:])


# get last chars
print(letters[-1:])
# get first position
print(letters[:1])
