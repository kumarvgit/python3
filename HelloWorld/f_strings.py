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
print(f'Age is {greetings}')
# we can use f in the beginning of the string and use replacement fields as values
print(f"Pi is: {22 / 7:12.55f}")
