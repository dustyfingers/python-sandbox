#
# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#


#  simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple)


# tuple using constructor
fruit_tuple_2 = tuple(('Apple', 'Orange', 'Mango', 'Orange'))
print(fruit_tuple_2)


# get a single value
print(fruit_tuple[1])


# tuple values can not be changed!
# fruit_tuple[2] = 'Persimmon'  # error!


# tuple with one value should have trailing comma! otherwise just returns that value
fruit_tuple_3 = ('Banana',)


# length of tuple
print(len(fruit_tuple))


# delete tuple
del fruit_tuple_3
# print(fruit_tuple_3) # error, is not defined


#
# A Set is a collection which is unordered and unindexed. No duplicate members.
#


# simple set
veggie_set = {'Celery', 'Onion', 'Carrot'}
print(veggie_set)


# no duplicate members in a set!
# veggie_set = {'Celery', 'Onion', 'Carrot',
#               'Celery'}  # 2nd celery doesnt show up
# print(veggie_set)


# check if in set
print('Celery' in veggie_set)


# add to set
veggie_set.add('Broccoli')
print(veggie_set)


# remove from set
veggie_set.remove('Broccoli')
print(veggie_set)


# clear set completely
veggie_set.clear()
print(veggie_set)


# delete set
del veggie_set
