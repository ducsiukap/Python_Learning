'''
base on list with some different:
        List[]          |       Tuple()
- represented by []     |- represented by ()
- mutable               |- immutable
=> can update(adding,   |=> can't update
removing, changing)     |
after created           |
- slower than Tuple()   |- faster than List()
- larger memory than    |- less memory than List[]
Tuple()
'''

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

T = (3, 2, 3, 2, 3, 'Duc')
print(T.count(3))
print(T.index(2))