current_choice = '-'
computer_parts = []  # create and empty list
computer_available_parts = ['Computer',
                            'Monitor',
                            'Keyboard',
                            'Mouse',
                            'Mouse Pad',
                            'HDMI Cable',
                            'DVD Drive']

# List comprehension
valid_choices = [str(i) for i in range(1, len(computer_available_parts) + 1)]
# print(valid_choices)
while current_choice != '0':
    # if current_choice <= len(computer_available_parts) and current_choice != -1:
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        part_in_list = computer_available_parts[index]
        if part_in_list in computer_parts:
            print('Removing {}'.format(current_choice))
            computer_parts.remove(part_in_list)
        else:
            print('Adding {}'.format(current_choice))
            computer_parts.append(part_in_list)
        print("Your list contains: {}".format(computer_parts))
    else:
        print('Add options from below menu')
        # This is inefficient since the list grows it takes longer time to find the index
        # for part in computer_available_parts:
        #     print('{}. {}'.format(computer_available_parts.index(part) + 1, part))

        # Enumerate returns a list with numbers, it returns pair of value
        for part, number in enumerate(sorted(computer_available_parts), start=1):
            print('{}. {}'.format(part, number))
        print('0. to finish')
    current_choice = input()

print(computer_parts)
