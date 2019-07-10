# A variable is a container for a value, which can be of various types
# comments in python are started with hashtags

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""


# NO VAR, NO LET NO CONST keyword NO SEMICOLONS in python!
x = 1  # int
y = 2.5  # float
name = 'Lou'  # string
is_awesome = False  # bool values are UPPERCASE
many_words_long = 'the language uses snake_case!'  # SNAKE CASE


# MULTIPLE ASSIGNMENTS
var1, var2, var3, is_python_freaking_cool = (1, 2, 'apple!', True)


# NO console.log(); instead, print() function
print(var1, var2, var3)  # returns '1 abc apple!'


# basic math
z = x + y
print(z)


# want to check type?
print(type(is_awesome))


# type casting
x = str(x)  # 'casts' x as a string
var2_string = int(var2)  # casts var2 as an int! (you can also cast as float)
print(var2_string)
