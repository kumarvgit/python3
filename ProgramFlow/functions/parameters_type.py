def func(p1, p2, *args, k, **kwargs):
    print('positional-or-keyword {} {}'.format(p1, p2))
    print("var positional args...{}".format(args))

    print("keyword: {}".format(k))
    print("keyword positional args...{}".format(kwargs))


'''
Here
the first two are the positional parameters 1, 2

now we ran out of positional it will continue with variable number of
parameters until it finds k since that is keyword argument only i.e. 3, 4, 5

once it finds k=6 which is key-only parameter

the last is variable key word args and that is any thing beyond that
here key1 and key2 
'''
func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)

