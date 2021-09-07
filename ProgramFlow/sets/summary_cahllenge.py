choice = "-"  # initialise choice to something invalid
while choice != "0":
    # Set is a better choice since it can be hashed
    if choice in set("12345"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()