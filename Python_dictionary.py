# Python Dictionary

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

mydict = {
    "one" : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five"
}

# print the whole dictionary
print(mydict)

# print value of any key
print(mydict["one"])
print(mydict[4])
print(mydict.get(3))


# Print The length of the dictionary
print(len(mydict))

# Print the type

print(type(mydict))

# Make an empty Dictionary
mydict1 = {}
print(type(mydict1))


# Print the keys of the dictionary
x = mydict.keys()
print(x)


# Add New Item to the dictionary
mydict["six"] = 6
print(x)


# Print all the values of the dictionary
print(mydict.values())

# Manipulate the existing data of the dictionary
mydict["one"] = "changed_one"

print(mydict)


# remove item from the dictionary
mydict.pop("one")

print(mydict)


# Print all the key value pair of the dictionary
for i in mydict: #here i is key
    print(i,mydict[i])