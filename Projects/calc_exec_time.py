from time import time

start = time()

list = []
n = int(input("Enter the size of the List : "))
print("Enter the Elements of the List")
for i in range(0,n):
    x = int(input())
    list.append(x)
    
    
print("\n\n The Items in the list are \n")
for i in list:
    print(i);



end = time()

# rounded_number = round(number, ndigits)
print("The Execution time of Program is : ",round(end-start,5),end="")
print("s")