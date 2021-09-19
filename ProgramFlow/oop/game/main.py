from player import Player

from enemy import Enemy, Troll

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

tim.score = 500
print(tim)


print('*' * 80)

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll()
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another troll - {}".format(another_troll))

brother = Enemy("Urg", 23)
print(brother)
