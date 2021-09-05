vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}
my_car = vehicles['fiesta']
print(my_car)

# indexing is faster
print(vehicles['virago'])

# get returns None if key does not exist
learner = vehicles.get('er5')

for i in vehicles.items():
    print(i)
