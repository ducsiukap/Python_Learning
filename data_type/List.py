# list is mutable
L = []
print(L)
print()

# adding element
# append(element) -> at end of list
L.append(2)
L.append('Duc')
print(L)
# insert(position, element)
L.insert(1, 3 + 2j)
print(L)
# extend(multi element)
L.extend([3, 'k', True])
print(L)
print()

#remove element
p = L.pop() # pop(position) 
print(L, p)
L.remove(2) # remove(element)
print(L)
print()

# copy
l = L # l and L refer to same location
print(l is L)
l.remove(3) # L and l will be changed together
print(l, L)
lL = L.copy() # lL and L refer to differenc location
print(lL is L)
lL.pop(0)
print(lL, L)


'''
some method:
clear()
count(element)
sort()
sum()
max()
min()
len()
ord(chr) -> return unicode
'''