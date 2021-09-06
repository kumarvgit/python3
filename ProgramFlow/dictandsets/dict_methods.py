d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# The values is a dynamic view, refer docs
v = d.values()
print(v)
d[10] = "ten"
print(v)

print("*" * 80)
d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is new three"
}

d.update(d2)
for key, value in d.items():
    print(f"{key}:{value}")

# Creating a dictionary from existing enums
d.update(enumerate(pantry_items))

for key, value in d.items():
    print(f"{key}:{value}")


# creating a dict with a default value
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

keys = d.keys()
print(keys)

for item in d.keys():
    print(item)



