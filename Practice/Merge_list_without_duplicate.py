# Python Merge Two Lists Without Duplicates

# Method - 1 Using set Union

list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Converting the list into set
set1 = set(list1)
set2 = set(list2)

# find the union of the sets and converting resultant set to list
ans = list(set1.union(set2))

print("The resultant merged list is ")
print(ans)



# Method - 2 Using loop

list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Resultant list
ans = []

# Traversing the list item one by one 
for data in list1:
    if data not in ans:
        ans.append(data)
        
for data in list2:
    if data not in ans:
        ans.append(data)

print("The resultant merged list is ")
print(ans)



# Method - 3 Using list(set())

list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Resultant list
ans = list(set(list1 + list2))

print("The resultant merged list is ")
print(ans)



# Method - 4 Using list Comprehension

list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Resultant list
ans = list1 + [item for item in list2 if item not in list1]

print("The resultant merged list is ")
print(ans)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

merged_list = list1 + [item for item in list2 if item not in list1]

print(merged_list)