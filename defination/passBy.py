# default is pass by ref
def change(x):
    x[0] = 'change'

L = [1, 2, 3]
print(f'before: {L}')
change(L)
print(f'after: {L}')

# to pass by value, us [:] when calling function
L2 = [3, 4, 5, 6, 7]
print(f'before: {L2}')
change(L2[:])
print(f'after: {L2}')

# broken link:
def broke(x): # reference
    x = [2, 3, 4] # a new object is assigned to x

print(f'befor: {L2}')
broke(L2)
print(f'after: {L2}')

def swap(x, y): return y, x
x, y = 5, 10
x, y = swap(x, y)
print(x, y)