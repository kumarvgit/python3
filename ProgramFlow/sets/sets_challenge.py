text = """Education is not the learning of facts but the training of the mind to think – Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

word_list = set(text.split(sep=' '))
print(word_list)

print(prepositions.intersection(word_list))

