numbers = (1, 2, 3)

print(numbers)
print(*numbers)  # the tuple of numbers are unpacked and sent to print function
print(1, 2, 3)


def test_args(*args):
    """
    Here any sequence having * in value having makes python to receive the as
    tuple and the same without * is an un packed value.
    hence *args is a packed tuple but args is an packed tuple
    :param args: the any number of param
    :return: None
    """
    print(*args)  # this is a unpacked tuple
    print(args)  # this is an packed tuple

    for x in args:
        print(x)


test_args(1, 2, 3)
