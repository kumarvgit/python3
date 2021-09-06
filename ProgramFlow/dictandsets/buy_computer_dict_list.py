available_parts = {'1': 'Computer',
                   '2': 'Monitor',
                   '3': 'Keyboard',
                   '4': 'Mouse',
                   '5': 'HDMI Cable',
                   '6': 'DVD Drive'
                   }
current_choice = None
while current_choice != '0':
    # iterating over the keys
    if current_choice in available_parts:
        chosen_parts = available_parts[current_choice]
        print(f"Adding {chosen_parts}")
    else:
        print('Menu items')
        for key, value in available_parts.items():
            print(f'{key}: {value}')
        print('0: to finish')
    current_choice = input('> ')
