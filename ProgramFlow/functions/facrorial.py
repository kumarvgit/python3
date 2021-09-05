def factorial(num: int) -> int:
    """
    Calculate factorial of a number

    :param num: the number ad `int`
    :return: factorial of the number
    """
    fact = 1
    if num == 0:
        return 1

    for j in range(1, num):
        fact = fact + fact * j
    return fact


for i in range(0, 36):
    print(i, factorial(i))
