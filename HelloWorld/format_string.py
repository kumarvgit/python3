for i in range(1, 13):
    # {0:2} says the width
    print("""No. {0:2} Square is: {1:3} and cube is: {2:4}""".format(i, i ** 2, i ** 3))

print("Left align")
for i in range(1, 13):
    """
    < left align
    > right align
    ^ center align
    """
    print("""No. {0:<2} Square is: {1:<3} and cube is: {2:<4}""".format(i, i ** 2, i ** 3))

print("pi is approximately {0}".format(22 / 7))  # default 15 position, 3.142857142857143

print("pi is approximately {0:12}".format(22 / 7))  # adding f default is 6 places, 3.142857142857143

#     3.142857
print("pi is approximately {0:12f}".format(22 / 7))
"""
here we are specifying 12 as length and also saying 50 as precision
here python decides over precision rather than the width specified
"""
print("pi is approximately {0:12.50f}".format(22 / 7))
print("pi is approximately {0:52.50f}".format(22 / 7))
print("pi is approximately {0:62.50f}".format(22 / 7))


print("pi is approximately {0:<72.50f}".format(22 / 7))
"""
Python has a precision of 51 digits after decimal hence when we specify 54 as after decimal it pads it with 0
"""
print("pi is approximately {0:<72.54f}".format(22 / 7))
