# A List is a collection which is ordered and changeable. Allows duplicate members.
# basically an array


# create a list
# numbers = [1, 2, 3, 4, 5]


# using a constructor
numbers = list((1, 2, 3, 4, 5))
print(type(numbers))


# get value by index
fruits = ['apples', 'oranges', 'grapes', 'pears']
print(fruits[0])
print(fruits[1])


# get length
print(len(fruits))


# append to list
fruits.append('Mangos')
print(fruits)


# remove from list
fruits.remove('grapes')
print(fruits)


# insert element into position
fruits.insert(2, 'Strawberries')
print(fruits)


# remove element from position
fruits.pop(3)
print(fruits)


# reverse list
fruits.reverse()
print(fruits)


# sort list
fruits.sort()
print(fruits)


# sort list reverse
fruits.sort(reverse=True)
print(fruits)
