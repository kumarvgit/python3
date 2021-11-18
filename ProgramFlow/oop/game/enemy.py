import random


class Enemy:

    """
    Automatically inherits object class from python3
    """

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    def __str__(self):
        return """Name: {0.name}, Lives: {0.lives},Hit points: {0.hit_points} Alive: {0.alive}""".format(self)


class Troll(Enemy):
    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f'{self.name} stomp you')


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 140

    def take_damage(self, damage):
        qtr_damage = damage // 4
        super().take_damage(qtr_damage)