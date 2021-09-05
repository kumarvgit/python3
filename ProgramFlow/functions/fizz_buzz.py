def fizz_buzz(inp: int) -> str:
    """
    Fizz buss game

    if input is a
        number divisible by 3       - fizz
        number divisible by 5       - buzz
        number divisible by 3 and 5 - 'fizz buzz'
    :param inp: an `int` natural number <= 100
    :return: 'fizz', 'buzz', 'fizz buzz'
    """
    if inp % 3 == 0 and inp % 5 == 0:
        return 'fizz buzz'
    elif inp % 3 == 0:
        return 'fizz'
    elif inp % 5 == 0:
        return 'buzz'
    else:
        return str(inp)
    pass


for i in range(1, 101):
    output = fizz_buzz(i)
    if output is not None:
        print(output)
