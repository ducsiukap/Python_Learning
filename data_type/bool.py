boolean = True
print(f'type of boolean: {type(boolean)}')
print()

a = 5
b = 5
print(f'{a} == {b}: {a == b}')
a = 10
print(f'{a} == {b}: {a == b}')
print()

# is and ==
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f'list1: {list1}\nlist2: {list2}')
print(f'list1 == list2: {list1 == list2}') # '==' : compare based on value
print(f'list1 is list2: {list1 is list2}') # 'is' : True if 2 variable refer to same object, otherwise is False
# False because List is mutable => difference object
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(f'{tuple1} is {tuple2}: {tuple1 is tuple2}')
# True because Tuple is immutable => same value == same obj
print()

# in : check if item in a set of smth
print(f'3 in list1: {3 in list1}')
print()
