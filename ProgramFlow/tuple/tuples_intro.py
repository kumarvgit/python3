t = "a", "b", "c"  # tuples can be without parenthesis
u = ("a", "b", "c")  # tuples can be with parenthesis
print(t)
print(u)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
# tuples are immutable
# metallica[2] = 8  # error
metallica2 = list(metallica)  # create a list from tuple
print(metallica2)

print('*' * 80)
name, artist, year = metallica
print(name)
print(artist)
print(year)

table = ("Coffee Table", 200, 100, 75, 30.99)
print("Area {}".format(table[1] * table[2]))

# Unpack by name
name, length, width, height, price = table
print("Area {}".format(length * width))

print('*' * 80)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))

for album in albums:
    print("Album {} artist {} year {}".format(album[0], album[1], album[2]))
print('*' * 80)

for name, artist, year in albums:
    print("Album {} artist {} year {}".format(name, artist, year))
print('*' * 80)
