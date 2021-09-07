list_dup = ['blue', 'red', 'green', 'blue', 'white']
set_rem_dup = set(list_dup)
print(set_rem_dup)

# Preserve the data insertion order
unique_data = list(dict.fromkeys(list_dup))
print(unique_data)

set_rem_dup.remove('red')
print(set_rem_dup)

