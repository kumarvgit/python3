name = input("What is your name ")
age = int(input("how old are you {}? ".format(name)))
print(age)

# if age >= 18:
#     print("Your are old enough to vote")
#     print("Please put a X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Super human")
else:
    print("Your are old enough to vote")
    print("Please put a X in the box")
