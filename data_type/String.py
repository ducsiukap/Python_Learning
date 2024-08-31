# '   ' for one line string
# '''   ''' -> for multiple lines string
str1 = 'hi, im Duc!' # one line str
str2 = '''im 20 yo
im a student
im learning at PTIT
my gpa is 3.29''' # multi lines str
print(str1)
print(str2)
print()

''' str.format() and f-string
f-string is a shorthand of str.format()
example:
    name = 'Duc'
    age = 20
str.format() syntax:
    'my name is {} and im {} yo'.format('Duc', 20)
f-string syntax:
    f'my name is {Duc} and im {age} yo'
'''
name = 'Duc'
age = 20
jobs =  'Deverloper'
# str.format()
print('my name is {}, im {}yo and im a {}!'.format(name, age, jobs)) # default is {0}, {1}, {2}
# pass by index: 'my name is {2}, im {0}yo and im a {1}!'.format(name, age, jobs)
            # => my name is Deverloper, im Ducyo and im a 20!
# assign value: 'my name is {name}, im {}yo and im a {}!'.format(age, name = name, jobs) 
            # => my name is Duc, im 20yo and im a Deverloper

# f-string
print(f'my name is {name}, im {age}yo and im a {jobs}!')
print()

# index, slicing, ...
Duc = 'Pham_Van'
#      [P] [h] [a] [m] [_] [V] [a] [n]
#      [0] [1] [2] [3] [4] [5] [6] [7]
#     [-8][-7][-6][-5][-4][-3][-2][-1]
print(f'Duc[]: {Duc}')
# slicing: str[start:end:step] 
print(f'Duc[3:5]: {Duc[3:5]}')
print(f'Duc[5:3:-1]: {Duc[5:3:-1]}')
print()

# update str
firstName = "Pham Van "
lastName = "Duc"

fullName = firstName + lastName
print(fullName)
fullName = firstName[:5] + lastName
print(fullName)
print()

# ord() and chr()
print(ord('a'))
print(chr(97))
