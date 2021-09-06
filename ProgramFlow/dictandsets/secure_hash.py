import hashlib

print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)

print()
print()
string = """ for i in range(10):
print(i)
"""

print(string)
original_hash = hashlib.sha256(string.encode("utf-8"))
print(original_hash.hexdigest())

string += '# modify data'

new_hash = hashlib.sha256(string.encode("utf-8"))
print(new_hash.hexdigest())

if original_hash.hexdigest() == new_hash.hexdigest():
    print('Code is not modified')
else:
    print('CODE IS MODIFIED !!!!!')
