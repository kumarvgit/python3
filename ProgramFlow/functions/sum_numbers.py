def sum_numbers(*args: float) -> float:
    """
    FUnction to calculate sum of variable arguments

    :param args: numbers passed as string or int
    :return: `int` as summation
    """
    sum_num = 0
    for x in args:
        sum_num += x
    return sum_num


print(sum_numbers(1, 2, 4))
print(sum_numbers(1.1, 2.0, 4))

