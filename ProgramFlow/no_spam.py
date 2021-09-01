menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


print('Print List')
for meal in menu:
    for item in meal:
        if item != 'spam':
            print(item, end=', ')
    print()

print()
print("*" * 80)
print("Reversed iterator")
for meal in menu:
    top_index = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if item == 'spam':
            del meal[top_index - index]
    print(meal)
