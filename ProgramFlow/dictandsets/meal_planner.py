from contents import pantry, recipes


def add_shopping_item(dict_to_add: dict, item_add: str, quantity_add: float):
    """
    Add the items in a dictionary of shopping list

    if item is already present get and add additional value to it

    :param dict_to_add the dictionary to which it is to be added
    :param item_add: the food item `str` to be added to shopping dict
    :param quantity_add: quantity as `float`
    :return: None
    """
    # Good way
    # if item_add in shopping_dict:
    #     mod_quantity = shopping_dict[item_add] + quantity_add
    #     shopping_dict[item_add] = mod_quantity
    # else:
    #     shopping_dict[item_add] = quantity

    # Better way
    '''
    This method gets the item from dict
    if found returns the value
    else initializes to 0
    and set it back to dict
    '''
    dict_to_add[food_item] = dict_to_add.setdefault(food_item, 0) + quantity_add


# Dict comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# print(display_dict)

display_dict = {}

shopping_dict = {}
'''
(
    Generating an index starting 0 which we are incrementing,
    Post this each key from dict is taken as value in enumerate function)
)
this results into a tuple
'''

for index, key in enumerate(recipes):
    # print(f"{index + 1}: {key}")
    display_dict[str(index + 1)] = key

while True:
    # Display Menu
    print('Please choose your recipe')
    print('-------------------------')

    # dict.getItems() returns tuple
    for key, value in display_dict.items():
        print(f'{key} - {value}')

    choice = input(': ')

    if choice == '0':
        break
    elif choice in display_dict:  # returns key in dict
        selected_item = display_dict[choice]
        print(f'You have selected {selected_item}')
        print('Checking ingredients...')
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            # Return an item to 0 if it does not exist
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f'\t{food_item}, {required_quantity} ok')
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f'\tYou don\'t have necessary ingredient:'
                      f'need to buy {quantity_to_buy} of {food_item}')
                add_shopping_item(shopping_dict, food_item, quantity_to_buy)

print(f"{'-' * 10} Shopping List {'-' * 10}")
for item, quantity in shopping_dict.items():
    print(f"{item}: {quantity}")
print()
