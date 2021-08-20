# week typed language
greetings = 'Hello'
age = 24

# get the type data
print(type(greetings))
print(type(age))

# we can change type of declared variable

greetings = 34
age = 'Hello'
print(type(greetings))
print(type(age))

# Strong typed language, java does an automatic conversion
print('Age is' + greetings)
# TypeError: can only concatenate str (not "int") to str
