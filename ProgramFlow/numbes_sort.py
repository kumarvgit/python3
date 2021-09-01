even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# combining the list
even.extend(odd)

print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
