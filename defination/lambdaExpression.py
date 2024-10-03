'''Syntax:
myFunc = lambda args : body'''

print('lambda function with if-else: ')
Max = lambda a, b: a if a > b else b
print(Max(2, 3))

print('lambda function with list: ')
listLambda = [lambda n = x: n << 1 for x in range(1, 5)] # a list of lambda
for lb in listLambda:
    print(lb(), end=' ')
print()

print('lambda with filter: ')
num = [32, 43, 65,23, 4353, 345354, 32,4, 234,563221, 324]
print(f'odd number in list: {list(filter(lambda x: x & 1, num))}')

print('lambda function with map: ')
name = ['Bob', 'aLicE', 'LINDa']
NAME = list(map(lambda Name: Name[0].upper() + Name[1:].lower(), name))
print(NAME)
