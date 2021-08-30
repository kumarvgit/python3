result = True
another_result = result
print(id(result))
print(id(another_result))

# bool is immutable
result = False
print(id(result))
print(id(another_result))
