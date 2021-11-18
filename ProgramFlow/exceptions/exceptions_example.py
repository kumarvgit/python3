# x = 8 - 5
# y = x / 0


def factorial(n):
    """ defined as n * n-1"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print("{}".format(factorial(1000)))
except RecursionError:
    print("This program can not calculate factorial of that large number")

print("Program terminates")
