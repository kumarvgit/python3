
# crude way for creating a set
numbers = {*""}

print(type(numbers))

numbers_set = set()

numbers_set.add(1)
print(type(numbers_set))

print(numbers_set)

numbers_set.clear()
while len(numbers_set) < 4:
    numbers_set.add(int(input("Enter a number")))
print(numbers_set)
