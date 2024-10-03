def myFunc(arg1 = 'arg1', arg2 = 'arg2', arg3 = 'arg3'): # default arguments
    print(f'arg1: {arg1}\narg2: {arg2}\narg3: {arg3}')
    print()

print('default argument: ')
myFunc()

print('named argument: ')
myFunc(arg1='Duc', arg3=20, arg2='Hanoi')

''' ARBITRARY KEYWORD ARGS: dont know how many args will be passed
*args: a list
**args: a list of dictionary
'''
def makePizza(*toppings): 
    for topping in toppings:
        print(f'added {topping} into ur pizza!')
    print('make pizza successfully!')
    print()

makePizza('pho mai', 'ngo', 'ca chua', 'xuc xich')


def studentInfor(**infors):
    infors['fname'] = 'Pham Van'
    infors['lname'] = 'Duc'
    return infors

print(studentInfor(age = 20, id = 'B22DCCN243', address = 'Hanoi'))