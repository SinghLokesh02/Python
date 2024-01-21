# Python Dictionary

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

mydict = {"one": "one", 2: "two", 3: "three", 4: "four", 5: "five"}

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
for i in mydict:  # here i is key
    print(i, mydict[i])


# Add data to the dictionary
mydict[6] = "six"
mydict[7] = "seven"
print(mydict)


# Print all the key value of the dictionary
print("\n\nGoing to print all the key value pairs of dictionary\n\n")
for key, value in mydict.items():
    print(f"The key is {key} ans the value is {value}")


# Remove item From dictionary
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
mydict.popitem()
print(mydict)


# The del keyword removes the item with the specified key name:
del mydict[2]
print("\n Printing the dictionary after removing 2 and its value")
print(mydict)


# Print key and value using normal loop
# Printing the keys
for i in mydict:
    print(i)


# Printing the Values
for i in mydict:
    print(mydict[i])


# Clear all the data of Dictionary
mydict.clear()
print(mydict)


#                               Nested Dictionary
nested_dict = {
    "person1": {
        "name": "John",
        "age": 30,
        "address": {"city": "New York", "zip_code": "10001"},
    },
    "person2": {
        "name": "Alice",
        "age": 25,
        "address": {"city": "San Francisco", "zip_code": "94105"},
    },
}

# Print all the nested_dict
print(nested_dict)

# Print the nested_dict key 1
print(nested_dict["person1"])

# Access the element of the nested dict
add = nested_dict["person2"]["address"]
print(add)

# Be more specific
zip = nested_dict["person2"]["address"]["zip_code"]
print(zip)

city = nested_dict["person2"]["address"]["city"]
print(city)


name = nested_dict["person1"]["name"]
print(name)


# Remove a element from nested Dictionary
nested_dict["person1"].pop("address")
print(nested_dict["person1"])

# Change the Value of Nested Dictionary
nested_dict["person1"]["name"] = "Lokesh Singh"
nested_dict["person1"]["age"] = 21
print(nested_dict["person1"])


# Iterate the dictionary

for key, value in nested_dict.items():
    print(key, " : ", value)


# Iterate data one by one
for person, details in nested_dict.items():
    print(f"Details for {person}:")
    for key, value in details.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for sub_key, sub_value in value.items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")
    print()


# The del keyword can also delete the dictionary completely:
del nested_dict
print(nested_dict)
