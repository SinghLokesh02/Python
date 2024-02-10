# deep vs shallow Copy

import copy

# Shallow Copy for dictionary

dict1 = {1:'one',2:'two',3:'three'}
dict2 = dict1.copy()
print(dict1)
print(dict2)

dict1[1] = 'ONE'
print(dict1)
print(dict2)


person = {'name': 'Alice', 'age': 30, 'address': {'city': 'New York', 'zipcode': 12345}}
shallow_copy = person.copy()
shallow_copy['address']['city'] = 'San Francisco'

print(person)   
print(shallow_copy)


person = {'name': 'Alice', 'age': 30, 'address': {'city': 'New York', 'zipcode': 12345}}
shallow_copy = copy.deepcopy(person)
shallow_copy['address']['city'] = 'San Francisco'

print(person)   
print(shallow_copy)
 