# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Louie'
age = 22

# Concatenation
print('Hello ' + name +
      ', you are ' + str(age) +
      ' years old.')  # cast the int to str


# Arguments by position
print('{}, {}, {}'.format('first', 'second', 'third'))
print('{1}, {0}, {2}'.format('first', 'second', 'third'))


# Arguments by name
print('Hello my name is {name} and I am {age} years old!'.format(
    name=name, age=age))


# f-strings (python3.6+)
print(f'Hello my name is {name} and I am {age} years old!')


'''
STRING METHODS
'''
s = 'hello There cruel world'


# capitalize first letter
print(s.capitalize())


# all uppercase
print(s.upper())


# all lowercase
print(s.lower())


# swapcase
print(s.swapcase())


# get length of str
print(len(s))


# replace series of chars w another
print(s.replace('world', 'everyone'))


# count instances of a char or sequence or chars
print(s.count('e'))


# starts with a char or sequence or chars, returns bool
print(s.startswith('hello'))


# ends with a char or sequence or chars
print(s.endswith('worldz'))


# split into a list
print(s.split())
s2 = 'comma, separated, string'
print(s2.split(', '))


# find position of a char or chars
print(s2.find('r'))


# is all alphanumeric
print(s.isalnum())


# is all alphabetic
print(s.isalpha())


# is all numeric
print(s.isnumeric())
