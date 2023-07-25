marks = [3,5,6,"String",12.4,True]
print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

print(marks[-1])

# Print upto given Range in list
print(marks[0:-1])#exclude last i.e -1 index
print(marks[0:3])#exclude last i.e 3 index

if "String" in marks:
    print("Yes it is in marks")
else:
    print("No It is not found")
    
    
# List Methods -> List Manipulation\
    
new_l = [11,1,11,3]
print(new_l);

# Append -> Insert At last
new_l.append(7);
# print(new_l);


# Sort list Ascending
new_l.sort();
# print(new_l)

# Sort List Descending
new_l.sort(reverse=True);
# print(new_l)


new_l.reverse();
print(new_l);

# Give Index of that particular
x = new_l.index(11);
print(x)


# Count number of occurence
print(new_l.count(11))

m = new_l.copy()
print(m)
m[0] = "hey"
print(m)


# Insert at given Index
m.insert(1,899);# insert(index,value)
print(m)


new_l.extend(m);
print(new_l)