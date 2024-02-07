# Deep Copy Vs Swallow Copy

import copy

# Swallow Copy
original_dict = {"a": 1, "b": [1, 2, 3]}
print(original_dict)

swallow_copy = original_dict
print(swallow_copy)

# Changing data in deep copy
swallow_copy["a"] = 4
print(original_dict)
print(swallow_copy)


# Deep Copy
original_dict = {"a": 1, "b": [1, 2, 3]}
print(original_dict)

deep_copy = copy.deepcopy(original_dict)
print(deep_copy)

# # Changing data in deep copy
original_dict["b"][1] = 4
print(original_dict)
print(deep_copy)
