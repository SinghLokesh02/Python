# Method - 3 Using Joing

my_list = [32, 45, 67, 78, 43, 21]
print("The items of the list")
print(' '.join(map(str, my_list)))
    
# Method - 1

my_list = [32, 45, 67, 78, 43, 21]
print("The items of the list")
for data in my_list:
    print(data,end=" ")
    
# Method - 2

my_list = [32, 45, 67, 78, 43, 21]
print("The items of the list")
print(*my_list,end=" ")
