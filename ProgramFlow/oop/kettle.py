class Kettle(object):

    # class variable which is going to be same for class and any instance variable it uses
    # We can change this value as well
    power_source = 'Electricity'

    def __init__(self, make, price):
        """
        Constructor for class
        :param make:
        :param price:
        """
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle('Hamilton', 14.55)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# accessing variables via class name
Kettle.switch_on(kenwood)
print(kenwood.on)


# This is an instance variable since only kenwood will know about it but not
# any other instance
kenwood.power = 1.5

print(f'kenwood power: {kenwood.power}')
# Below will result in to error
# print(f'hamilton power: {hamilton.power}')
# AttributeError: 'Kettle' object has no attribute 'power'
# print(f'hamilton power: {hamilton.power}')

print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)
hamilton.power_source = 'Gas'
print(hamilton.power_source)

print('Get all instance variable')
print(Kettle.__dict__)
print(hamilton.__dict__)
print(kenwood.__dict__)


if __name__ == "__main__":
    print('running as main')
else:
    print('running as module')
