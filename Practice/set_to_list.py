# # Method - 1

import time

# for small set
small_set = {1, 2, 3, 4, 5}

start = time.time()
small_list = list(small_set)
end = time.time()
print("Small Set to List Time:", end - start)

# for Large set
large_set = set(range(1, 1000001))

start_time = time.time()
large_list = list(large_set)
end_time = time.time()
print("Large Set to List Time:", end_time - start_time)



# Method - 2 Using Extend
import time

# For small set
s_set = {1, 2, 3, 4, 5}

start = time.time()
my_list = []
my_list.extend(s_set)
end = time.time()
print(my_list)
print("Small Set to List Time:", round(end - start,6))

# For large set
l_set = set(range(1, 1000001))

start = time.time()
my_list2 = []
my_list2.extend(l_set)
end = time.time()
print("\nLarge Set to List Time:", round(end - start,6))


# Method - 3 Using List Comprehension
s_set = {1, 2, 3, 4, 5}

start = time.time()
my_list = [i for i in s_set ]
end = time.time()
print("Newly Created list : ",my_list)
print("Small Set to List Time:", round(end - start,6))

# For large set
l_set = set(range(1, 1000001))

start = time.time()
my_list2 = [item for item in l_set ]
end = time.time()
print("\nLarge Set to List Time:", round(end - start,6))



