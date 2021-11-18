class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Wee this is fun')
        elif self.ratio == 1:
            print("This is hard work but i am flying")
        else:
            print("I think i will just walk")


class Duck(object):

    def __init__(self):
        # Give ducks a wing
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle Waddle Waddle !")

    def swim(self):
        print('Come on in, water is lovely')

    def quack(self):
        print('Quack quack')

    def fly(self):
        self._wing.fly()


class Mallard(Duck):
    pass


class Penguin(object):

    def __init__(self):
        # Mapping a function to another one
        # here we are assigning variable to a function and then it will be called
        self.fly = self.aviate

    def walk(self):
        print('Waddle, waddle, i waddle too')

    def swim(self):
        print("Come on in, but it's chilly this far south ")

    def quack(self):
        print('Are you avin a larf? i am penguin')

    def aviate(self):
        print("I won a lottery and bought a learjet")


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # if type(duck) is Duck:  # this is not pythonic cause python says if it flies like a duck its a duck
        # if isinstance(duck, Duck):  #his is not pythonic cause python says if it flies like a duck its a duck
        fly_attr = getattr(duck, "fly", None)  # this is pythonic
        if callable(fly_attr):
            self.flock.append(duck)
        else:
            raise TypeError("can not non duck to flock" + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down")
                # raise AttributeError
                problem = e
        # Raising a problem
        if problem:
            raise problem
# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    # Here we have the same behaviour for duck and penguin
    # so both are same in dynamically typed language
    # percy = Penguin()
    # test_duck(percy)
