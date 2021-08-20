parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

# Challenge
string = "we win"
for i in range(0, len(string)):
    print(string[i])


# negative numbers get from reverse
print(parrot[-1])

# Slice a string
print(parrot[0:6])
print(parrot[:6:2])
print(parrot[-4:-2])  # we can not go backward from start position

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
