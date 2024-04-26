# Update -> Update the set with the union of this set and others
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)



mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# remove element from the set
thisset.remove("banana")
thisset.discard("orange")

print(thisset)


# Remove a random item by using the pop() method:
thisset.pop()


# Erase all the elements of the set
thisset.clear()


# The del keyword will delete the set completely:
del thisset
# print(thisset)

'''Symmetric Difference Update'''
# Remove the items that are present in both sets, AND insert the items that is not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

'''Intersection Update'''

# The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
x.intersection_update(y)
print(x)
print(y)
