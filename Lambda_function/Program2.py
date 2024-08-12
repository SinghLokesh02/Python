# Write a Program to find the sum of list elements using lambda function

Add = lambda lst: sum(lst)
n = int(input("Enter the size of List : "))
list = []
for i in range(n):
    x = int(input())
    list.append(x)

print(f"The sum of {list} is : {Add(list)}")
