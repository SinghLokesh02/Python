print("This is tutorial for fibonacci series")

num = int(input("Enter any Number : "))
a = 0
b = 1

start = 0
while(start<num):
    print(a,end=" ")
    c = a+b
    a = b
    b = c
    start = start+1

exit()