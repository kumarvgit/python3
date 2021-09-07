small_ints = set(range(21))
print(small_ints)

# Does not raises an exception if key not present is set
small_ints.discard(100)

# Raises an exception if key is not present
small_ints.remove(100)
print(small_ints)
