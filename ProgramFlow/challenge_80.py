list_options = ['1. Learn Python', '2. Learn Java', '3. Go Swimming',
                '4. Have dinner', '5. Go to bed', '0. Exit']
answer = -1

for option in range(0, len(list_options)):
    print(list_options[option])
print()
while answer != 0:
    answer = int(input('Enter your choice: '))
    if answer not in range(len(list_options)):
        print('Please choose from options available')
        for option in range(0, len(list_options)):
            print(list_options[option])
    else:
        print('You choose: {}'.format(list_options[answer - 1]))

else:
    print('Have a good day')
