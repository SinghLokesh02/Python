# Sets in Python -> it does not have duplicate items

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

myset = {"apple","banana",1,1,12,3,4}
# print the set
print(myset)

# print the type of set
print(type(myset))

# print the length of the set
print(len(myset))


# print the data of the set
for elements in myset:
    print(elements)
    

# check if the item is present in the set or not
# print(1 in myset) print true
print(10 in myset) #print false



# add elements to the set
print(myset)#before adding elements
myset.add("orange") 
print(myset)#after adding elements



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
myset.pop()


# Erase all the elements of the set
thisset.clear()


# The del keyword will delete the set completely:
del thisset
print(thisset)
    