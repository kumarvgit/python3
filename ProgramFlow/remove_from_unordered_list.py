"""
Removing items from backwards does not messes up with the
indexes
"""

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# Reverse iteration using range
# for i in range(len(data) - 1, -1, -1):
#     if data[i] < min_valid or data[i] > max_valid:
#         del data[i]

# Reverse iteration using function
top_index = len(data) - 1
for index, d in enumerate(reversed(data)):
    if d < min_valid or d > max_valid:
        print(top_index - index, d)
        del data[top_index - index]

print(data)
