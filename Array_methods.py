# Array Methods in Python

arr = [1,2,3,4,5,6,7,8,9,10,10]

# Print the array
print(arr)

# Print Array Element using Index
print(arr[0])


# Append a element in the list
arr.append(100)
print(arr)


# Clear the array
arr.clear()
print(arr)


# Print the count of any Element in the array
x = arr.count(10)
print("The count of the element in arr is : ",x)


# Return the index of a given element
print(arr.index(10))


# Remove one Element from the last of the array
print(arr)
arr.pop()
print(arr)


# remove the first item with specified value
print(arr)
arr.remove(10)
print(arr)


# Reverse the array
print(arr)
arr.reverse()
print(arr)


# Sort The array 
print(arr)
arr.sort()
print(arr)


# Print the length of the array
print("The length of the array is : ",len(arr))


# Add element at the specified position
print(arr)
arr.insert(2,17)#Insert 17 at Index 2
print(arr)


# Copy the array
arr2 = arr.copy()
print(arr2)

