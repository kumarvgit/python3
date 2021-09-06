available_parts = {'1': 'Computer',
                   '2': 'Monitor',
                   '3': 'Keyboard',
                   '4': 'Mouse',
                   '5': 'HDMI Cable',
                   '6': 'DVD Drive'
                   }
current_choice = None
computer_parts = {}  # Empty dict

while current_choice != '0':
    # iterating over the keys
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"The dict contains {computer_parts.values()}")
    else:
        print('Menu items')
        for key, value in available_parts.items():
            print(f'{key}: {value}')
        print('0: to finish')
    current_choice = input('> ')
