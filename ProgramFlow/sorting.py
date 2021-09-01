pangram = 'The quick brown fox jumped over a lazy dog'
letters = sorted(pangram)
print(letters)

numbers = [9, 1.1, 4.5, 6.0, 4, 5.0]
sorted_numbers = sorted(numbers)
print(sorted_numbers)


missing_letter = sorted('The quick brown fox jumped over a lazy dog')
print(missing_letter)

# sort case insensitive
print(sorted(pangram, key=str.casefold))
