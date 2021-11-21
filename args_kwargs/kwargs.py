def print_backwards_without_kwargs(*args, file=None):
    for word in args[::-1]:
        print(word[::-1], end=' ', file=file)


with open("backwards.txt", "w") as backwards:
    print_backwards_without_kwargs("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)


def print_backwards(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)  #, end='\n' specifying end l as kword argument will result in error since it is part of kwargs dict






