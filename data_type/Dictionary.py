'''
- store element in: [key:value] format
- can not contain duplicate key
- key must be immutable
'''

dict = {} # creating a dictionary
print(f"creating an empty dictionary: {dict}")
print()

# adding element: dict[key] = value
dict['duc'] = True
dict[3] = 'integer'
dict[2.1] = 'float'
dict[-4 + 5j] = 'complex'
print(f'adding some element into dict: {dict}')
print()

# accessing element:
# accessing dict[key] can make an error if key is not included in dictionary
print(f'accessing element which has key is \'3\' use dict[3] : {dict[3]}')
# another way: dict.get(key, default_value) 
# return default_value if key is not in dictionary
print(f'accessing element which has key is \'3\' use dict.get(5) : {dict.get(5, '\'error: not_in_dict\'')}')
print()

#deleting element
del(dict['duc'])
print(f'deleting element with key \'duc\': {dict}')
print()

# some method with dictionary:
print(f'key collection: {dict.keys()}')
print(f'value collection: {dict.values()}')
print(f'all items in dict: {dict.items()}')
print()
