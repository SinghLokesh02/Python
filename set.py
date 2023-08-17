print("In this we are going to learn about Set")
'''
Questions

1) Write a Set

Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: -> Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets.
Note: -> Sets are unordered, so you cannot be sure in which order the items will appear

Duplicates Not Allowed
Sets cannot have two items with the same value.


'''
# Declare a Set
myset = {1,2,3,45,6,78,3,4}



# Print Type
print(type(myset))



# print the set
print(myset)



# Print the len of set
print(len(myset))



# Add Element in the set
myset.add(567)
print(myset)



# Remove Elements From the set
# Note: If the item to remove does not exist, remove() will raise an error.
myset.remove(1) # It will remove element 1 from the set
print(myset)



# Remove Element From the set By discard Method
# Note: If the item to remove does not exist, discard() will NOT raise an error.
myset.discard(2)
print(myset)



#Remove a random Element From the set
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
myset.pop()
print(myset)


# Convert a list to Set
list1 = [1,2,3,4,5,6,7,8]
print(type(list1),list1)
set_new = set(list1)
print(type(set_new),set_new)



# Access Set Items
for item in myset:
    print(item)
    


# Update in set
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) 




# Check Whether An element Belong to a set or not
print(3 in myset)




# Clear A set
myset.clear()
print(myset)




# Del a set
# The del keyword will delete the set completely:
del myset
# print(myset)