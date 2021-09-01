shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'test']
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]  # concatenating the list
print(id(shopping_list))
print(id(another_list))
