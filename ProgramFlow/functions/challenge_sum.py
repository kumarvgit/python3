"""
the class contains the sum of integers
"""


def sum_eo(n, t):
    if t != 'e' and t != 'o':
        return -1
    else:
        sum_num = 0
        if t == 'e':
            start = 2
        else:
            start = 1
        for i in range(start, n, 2):
            sum_num += i
        return sum_num


range_num = int(input("Enter the range"))
oe = input('sum of odd even')

sum_of_num = sum_eo(range_num, oe)
print(sum_of_num)
