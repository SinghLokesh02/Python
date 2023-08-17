# A tuple is a collection which is ordered and unchangeable.

# Ordered
# Unchangeable
# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

tup = (1,2,3,4,5)
# tup = (1,)
#  If you are making tuple of size 1 then , is necessary other wise interpreter get confused


# List Are Changable
# list1 = [1,2,3,4,5,6]
# list1[4] = 89
# print(list1)


# Tuple is unchangle

# tup[0] = 11 -> this is not supported
print(type(tup))
print(tup)

# Access Tuple by Index
print(tup[1])
print(tup[2:5])


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

tup1 = (1,2,3,4,5)
l1 = list(tup1)
l1[3] = 98
tup1 = tuple(l1)
print(tup1)


# Add Items in tuple -> First Convert it to list then insert an item in it
tupl = list(tup1)
tupl.append(89)
tup1 = tuple(tupl)
print(tup1)




# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

tup_check1 = (1,2,3)
tup_check2 = ("lokesh",)
tup_check1 += tup_check2
print(tup_check1)


# For Removing item from Tuple you have to convert it to list and then perform remove operation and after that convert it to tuple


# Del keyword in tuple -> delete the whole tuple

print(tup1)
del tup1



# Tuple Methods

# Count a particular element in the tuple

t = (1,2,3,4,5,6,7,8,98,88,8,8)
print(t.count(8))

# Find the index of particular element in tuple
print(t.index(88))
