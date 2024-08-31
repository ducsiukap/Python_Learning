''' set:
- unordered
- iterable and mutable
- no duplicate element
'''

# creating a set
s = set() # or s = {element} 
print(f'\ncreating a set: {s}')
print()

# adding element
s.add(3) # 1 element in one time
s.update(['quang', 3, 5, 2, 1,'duc', 'nam'])
print(f'adding element to s: {s}')
print()

# accessing element
print(f'3 in s: {3 in s}')
print()
# access all: for item in s:

# removing element:
s.discard(1) # isnt making an error if element is not included in set
# s.pop()
# s.clear()
print(f'removing some element: {s}')
print()

''' Some method with set:
.union(set) : merge 2 set -> return a new set
.difference(set) : difference element of 2 set -> return a new set
.difference_update(set) : remove all element of another set in this set
.intersection(set)
.intersection_update(set) 
.isdisjoin(set) -> True if null intersection
.issubset(set)
.issupperset(set)
'''