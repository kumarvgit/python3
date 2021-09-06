# Dictionary created from literal
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    # 'roadster': 'Triumph Street Triple' # This is going to replace earlier keys
}

# Insert into dictionary
vehicles['starfighter'] = 'Lockheed F104'
vehicles['learjet'] = 'Bombardier Learjet 75'
vehicles['toy'] = 'Glider'

# change the value in dict
vehicles['virago'] = 'Yamaha XV 535'



my_car = vehicles['fiesta']
print(my_car)

# indexing is faster
print(vehicles['virago'])

# get returns None if key does not exist
learner = vehicles.get('er5')

# inefficient code in cpu and memory
for key in vehicles:
    print('Key: {}  Value: {}'.format(key, vehicles[key]))

# similar to enumerate
for key, value in vehicles.items():
    """
    prior python 3.6 the order was not preserved
    from 3.7 insertion order is maintained
    """
    print(key, vehicles[key], sep=',')

# Remove from dictionary
# del vehicles['starfighter']

#  Another way to remove an item
#  dictionary and list has pop method
vehicles.pop('starfighter')

# This is going to give error since the item does not exist
# Either we choose to handle the error or we return the default value
# if value is not present
ret_val = vehicles.pop('starfighter123', 'No Value')
ret_val = vehicles.pop('starfighter123', None)
print(ret_val)
