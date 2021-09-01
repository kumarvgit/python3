even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(min(even))
print(max(even))

print(min(odd))
print(max(odd))

print(len(odd))

print()
print('mississippi'.count('s'))  # count the letters
print('mississippi'.count('is'))  # count the sequence

numbers = even + odd
print(numbers)

list_obj = list('789156423')
print(list_obj)

# Using constructor
# more_list_object = list(list_obj)

# Using Slice
# more_list_object = list_obj[:]
# Using copy
more_list_object = list_obj.copy()
print(more_list_object)
print(list_obj is more_list_object)  # object comparison
print(list_obj == more_list_object)  # content comparison


