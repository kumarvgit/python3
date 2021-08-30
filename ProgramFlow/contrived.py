numbers = [1, 45, 31, 12, 60]
for number in numbers:
    if number % 8 == 0:
        #         reject the list
        print("number is un acceptable")
        break
else:
    print("value is acceptable")
