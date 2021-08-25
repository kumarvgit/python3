for i in range(0, 101):
    if i % 7 == 0:
        print(i)

print('-' * 80)
# using step
for i in range(0, 101, 7):
    print(i)

print('-' * 80)
# This solution uses a slice
for i in range(101)[::7]:
    print(i)

