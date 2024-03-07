# How To Check If Json Object Has Empty Value In Python

import json


# Method - 1) Using Len()

# Example of Json Object
# jsonData = '{"key1": "value1", "key2": None}'
# if len(jsonData) == 0:
#     print("The JSON object is empty.")
# else:
#     print("The JSON object is not empty.")


# Method - 2) Using not operator

# jsonData = '{"key1": "value1", "key2": None}'
# if not jsonData:
#     print("The JSON object is empty.")
# else:
#     print("The JSON object is not empty.")


# Method - 3)

# def Check_Empty(data):
#     for value in data.values():
#         if not value:
#             return True
#     return False

# data = {"key1": "value1", "key2": None, "key3": []}

# if Check_Empty(data):
#     print("The JSON object has at least one empty value.")
# else:
#     print("The JSON object has no empty values.")


# Method - 4)





data = {"key1": "value1", "key2": "abc", "key3": "value3"}
if any(not value for value in data.values()):
    print("JSON object has empty values")
else:
    print("JSON object does not have empty values")

# if Check_Empty(data):
#     print("The JSON object has at least one empty value.")
# else:
#     print("The JSON object has no empty values.")
