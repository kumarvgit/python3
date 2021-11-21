def average(*args):
    """
    *args needs to be last positional parameters
    :param args:
    :return:
    """
    print(type(args))
    print("args is {}".format(args))
    # *args is unpacked tuple
    print("*args is ", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    return args


print(average(1, 2, 3, 4))
print("Hello", "World")


