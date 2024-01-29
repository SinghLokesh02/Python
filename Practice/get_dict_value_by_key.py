# Get Dictionary Value by key

# Method - 1 Using Square Method

# Creating a Dictionary
my_dict = {
    "name" : "Lokesh Singh",
    "age" : 21,
    "Roll" : 25,
    "Role" : "Software Trainer"
}

# Retrieve value by key using square brackets
result = my_dict["name"]

# Printing the result
print(f"The value corresponding to key(name) is {result}")


# Method - 2 Using get Method

# Creating a Dictionary
my_dict = {
    "name" : "Lokesh Singh",
    "age" : 21,
    "Roll" : 25,
    "Role" : "Software Trainer"
}

# Retrieve value by key using square brackets
result = my_dict.get("name")

# Printing the result
print(f"The value corresponding to key(name) is {result}")