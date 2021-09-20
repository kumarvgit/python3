from player import Player

from enemy import Enemy, Troll, Vampire, VampireKing

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

ugly_troll = Troll('Pug')
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()
print(brother)
brother.take_damage(5)
print(brother)

another_troll.take_damage(30)
print(another_troll)

vamp = Vampire(name="Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)


dracula = VampireKing("Count Dracula")
print(dracula)

dracula.take_damage(4)
print(dracula)
