from player import Player

tim = Player('Tim')

print(tim.name)
print(tim.lives)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.level = tim.level + 5
print(tim)

tim.level = tim.level - 2
print(tim)
