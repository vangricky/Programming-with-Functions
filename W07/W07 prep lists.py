# THINGS TO REMEMBER:
# ARRAYS: Numberical Data Types - Must all be the same type
# LIST: Store anything - Store any type
# DICTIONARY: Key/Value pairs - Storage order not guaranteed

from array import array

print("EXAMPLE 1")

names = ['Christopher', 'Susan']
scores = []
scores.append(98) #'append' adds item to the END of the list
scores.append(99) #whatever is in the parenthesis, will be added to the end of the (scores) list
print(names)
print(scores)
print(scores[1]) #this will print '99', because in line 4, we added 99 right after we added 98, which means, 98 is in the "second" position, which is 1. because in python it goes: 0, 1, 2, etc

print()
# COMMENT OUT line 3-9 if you will be running the code below!

print("EXAMPLE 2")

scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

print()
# COMMENT EVERYTHING ABOVE, IF RUNNING THE CODE BELOW!

print("EXAMPLE 3")

names = ['Susan', 'Christopher']
print(len(names)) # "len" gets the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort() # Puts the list into alphbetical order, or SMALLEST to BIGGEST
print(names)

print()
# COMMENT EVERYTHING ABOVE, IF RUNNING THE CODE BELOW!

print("EXAMPLE 4")

names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]
# Start and end index
print(names)
print(presenters)

print()

print("DICTIONARY : For Funsies")

person = {'first': 'Christopher'}
person ['last'] = 'Harrison'
print(person)
print(person['first'])