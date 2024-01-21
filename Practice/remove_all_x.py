# Take a number input and remove all occurence of that item from the list

my_list = [56, 1, 2, 3, 4, 56, 1, 2, 4, 56, 56, 56, 56, 56, 3, 56, 2, 56]

# Method - 1 (Make a new list and add element if number != x)
num = int(input("\nEnter the number you want to remove from above list : "))

ans = []
for data in my_list:
    if data != num:
        ans.append(data)

print(ans)


# Method - 2 (Using normal loop and in method)

x = int(input("\nEnter a Number you want to remove : "))

while x in my_list:
    my_list.remove(x)
print(my_list)

# Method - 3 (Using list comprehension)

rmve = int(input("\nEnter Element to be removed : "))
ans2 = [data for data in my_list if data != rmve]
print(ans2,"\n")