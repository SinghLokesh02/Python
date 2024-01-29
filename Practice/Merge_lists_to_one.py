# How Do I Merge Multiple Lists Into One List?

# Method - 1 : Using + operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Merging the list
merged_list = list1 + list2 + list3

print("The Merged list is")
print(merged_list)



# Method - 2 : Using extend() method

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Merging the list
merged_list = []
merged_list.extend(list1)
merged_list.extend(list2)
merged_list.extend(list3)

print("The Merged list is")
print(merged_list)



# Method - 3 : Using loops
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Merging the list
merged_list = []

# Inserting List 1 data
for data in list1:
    merged_list.append(data)
    
# Inserting List 2 data
for data in list2:
    merged_list.append(data)
    
# Inserting List 3 data
for data in list3:
    merged_list.append(data)

print("The Merged list is")
print(merged_list)


lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

merged_list = []
for sublist in lists:
    merged_list.extend(sublist)

print(merged_list)