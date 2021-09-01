# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# data = [1104, 1105, 1110, 1120, 1130, 1130, 1150,
#         1160, 1170, 1183, 1185, 1187, 1188, 1191, 1350, 360]

data = []
# del data
# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200
# for index, d in enumerate(data):
#     if d < min_valid or d > max_valid:
#         del data[index]  # this is not going to work since the list is changing

# deleting in ordered set
# process low value
stop = 0
for index, d in enumerate(data):
    if d > min_valid:
        stop = index
        break

del data[:stop]  # strip of the list

# process high value
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
del data[start:]
print(data)
