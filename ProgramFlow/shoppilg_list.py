shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'test']

for i in shopping_list:
    if i != 'spam':
        print('Buy: ' + i)

print('-' * 80)
for i in shopping_list:
    if i == 'spam' or i == 'test':
        continue
    print('Buy: ' + i)
print('-' * 80)
for i in shopping_list:
    if i == 'spam' or i == 'test':
        break
    print('Buy: ' + i)
