# Method -  4 -> Using loop

import time

# For Small List
small_list = [1, 2, 3, 4, 5]

small_set = set()

start = time.time()
for element in small_list:
    small_set.add(element)
end = time.time()

print("The time to convert small list to set : ",round(end - start,5))
print("The set is : ",small_set)

# For Large List

large_list = list(range(1, 1000001))
large_set = set()

start = time.time()
for element in large_list:
    large_set.add(element)
end = time.time()

print("The time to convert large list to set : ",round(end - start,5))


# # Method -  3 -> Using update method

import time

# For Small List
small_list = [1, 2, 3, 4, 5]

small_set = set()

start = time.time()
small_set.update(small_list)
end = time.time()

print("The time to convert small list to set : ",round(end - start),5)
print("The set is : ",small_set)

# For Large List

large_list = list(range(1, 10000001))
large_set = set()

start = time.time()
large_set.update(large_list)
end = time.time()

print("The time to convert large list to set : ",round(end - start,5))


# # Method -  2 -> Using set with unpacking

import time

# For Small List
small_list = [1, 2, 3, 4, 5]

start = time.time()
small_set = set(*[small_list])
end = time.time()

print("The time to convert small list to set : ",round(end - start),5)
print("The set is : ",small_set)

# For Large List

large_list = list(range(1, 10000001))
start = time.time()
large_set = set(*[large_list])
end = time.time()
print("The time to convert large list to set : ",round(end - start,5))


# Method -  1 -> Using Set() Constructor

import time

# For Small List
small_list = [1, 2, 3, 4, 5]

start = time.time()
small_set = set(small_list)
end = time.time()

print("The time to convert small list to set : ",end - start)
print("The set is : ",small_set)

# For Large List

large_list = list(range(1, 10000001))
start = time.time()
large_set = set(large_list)
end = time.time()
print("The time to convert large list to set : ",round(end - start,5))