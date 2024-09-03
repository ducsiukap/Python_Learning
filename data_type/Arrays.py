# store multiple item of the same type, like array in almost programming language

# syntax to create an Arrays:
import array
arr = array.array('i',[3, 4, 5]) # array.array('type', value_list)
print(f'creating an array: {arr}')
print()
''' 'type' in array.array('type', value_list):
- b, B for character
- u for unicode character
- h, H for short
- i, I for int
- l, L for long
- q, Q for long long
- f, F for float
- d, D for double
* note: lower/upper ~ signed/unsigned
'''

# adding element:
arr.append(-1)
arr.insert(2, 9)
print(f'adding some new elements: {arr}')
print()


# accesing: by index: arr[i] for ith element

# removing: 
arr.remove(3) # .remove(value)
arr.pop(2)    # .pop([index])
print(f'remove some elements: {arr}')
print()
