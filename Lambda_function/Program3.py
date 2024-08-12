# Write a Program to find the Maximum element of list elements using lambda function

Maximum = lambda lst: max(lst)
n = int(input("Enter the size of List : "))
list = []
for i in range(n):
    x = int(input())
    list.append(x)

print(f"The sum of {list} is : {Maximum(list)}")
