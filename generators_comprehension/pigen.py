def oddnumbers():
    start = 1
    while True:
        yield start
        start +=2


def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += 4 / next(odds)
        yield approximation
        approximation -= 4 / next(odds)
        yield approximation

# oddnumbers = oddnumbers()
# for _ in range(100):
#     print(next(oddnumbers))


approx_pi = pi_series()
for _ in range(1000000):
    print(next(approx_pi))
