num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

if(num1>num2 and num1>num3):
    print(num1," is greatest")
elif(num2>num1 and num2>num3):
    print(num2," is greatest");
else:
    print(num3," is greatest");


# Print Even Odd Numbers

num = int(input("Enter any Number : "))
start = 1   
while(start<=num):
    if(start%2==0):
        print(start)
    start = start+1

 
