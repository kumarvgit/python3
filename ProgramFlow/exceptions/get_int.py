import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Not an integer number")
        except EOFError:
            print('EOFError')
            sys.exit(1)
        finally:
            print("Finally clause always executes")


first_number = get_int("Enter first number")
second_number = get_int("Enter Second number")
try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Can not divide by zero")
    sys.exit(2)
else:  # this will be executed after try executes properly
    print("Division performed successfully")
finally:
    print("Terminating...")
