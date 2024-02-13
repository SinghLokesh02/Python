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


# Method - 3 Using Loops

# Creating a Dictionary
my_dict = {
    "name" : "Lokesh Singh",
    "age" : 21,
    "Roll" : 25,
    "Role" : "Software Trainer"
}

for key in my_dict:
    if key == "name":
        print(f"The value key {key} is : {my_dict[key]}")



# Method - 4 Using List Comprehension

# Creating a Dictionary
my_dict = {"name": "Lokesh Singh", "age": 21, "Roll": 25, "Role": "Software Trainer"}
key_item = "name"
result = [my_dict[key] for key in my_dict if key == key_item]
print(f"The value key {key_item} is : {result}")
