data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# Convert to ASCII chars
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> int:
    """
    return value of the kry
    :param k: the key
    :return: `int if found else None`
    """
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)

keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    print(key, h)

    # add in hash keys
    keys[h] = key
    values[h] = value

print(keys)
print(values)

print()
print(get('lemon'))

