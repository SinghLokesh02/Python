# Print the intersection of two list

list1 = [1, 23, 43, 45, 56, 67]
list2 = [43, 45, 65, 76, 78, 1]

# Method - 1 -> Convert the list into set and find intersection by intersection method

st1 = set(list1)
st2 = set(list2)

ans = list(st1.intersection(st2))
print('\nIntersection by Method 1 : ',end="")
print(ans)

# Method - 2 (Using list Comprehension)
for item in list1:
    result = [item for item in list1 if item in list2]

print('\nIntersection by Method 2 : ',end="")
print(result)


# Method - 3 (Normal function)

out = []
for data in list1:
    if data in list2:
        out.append(data)
print('\nIntersection by Method 3 : ',end="")
print(out)


# Method 4 - (Using double loops)
list3 = []
for i in list1:
    for j in list2:
        if(i==j):
            list3.append(i)

print('\nIntersection by Method 4 : ',end="")
print(list3)
print()

            