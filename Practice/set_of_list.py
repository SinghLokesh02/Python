list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

# Using set comprehension
set_of_lists = [list(lst) for lst in [list1, list2]]

print(set_of_lists)


# Method - 2

list1 = [1, 2, 3]
list2 = ['Charles', 'Jim', 'Bran','Arya']

# Initializing an empty List
combined = []

# Using append() method
combined.append(list1)
combined.append(list2)

print(combined)