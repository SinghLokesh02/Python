# Given a List of Element Remove the Odd Element

num = int(input("Enter the size of List : "))
lst = []
for i in range(num):
    x = int(input(f"Enter element {i} : "))
    lst.append(x)

# Removing the odd index element without using additional array
print("The List before deletion")
print(lst)
count = 1
remove = num//2
for i in range(remove):
    lst.pop(count)
    count+=1
    

print("The List before deletion")
print(lst)