# Now we are Going to see the function in Python

# Function 1 print "hello"
def print_hello():
    print("Hello Everyone")
    
print_hello()


# Function - 2 Check a number is Even or Odd
def check(num):
    if(num%2==0):
        print("The Number is Even Number")
    else:
        print("The given Number is Odd Number")
    
x = int(input("Enter any Number : "))
check(x)



# Function-3 Check Prime

def check_prime(num):
    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count += 1
    if(count==2):
        print("The given Number is Prime Number")
    else:
        print("The given Number is Not Prime Number")
    
x = int(input("Enter any Number : "))
check_prime(x)



# Function - 4 Print the largest Name Among the array of names
def largest_name(names):
    max = names[0]
    for i in range(1,len(names)):
        if(len(names[i])>len(max)):
            max = names[i]
    return max

names = ["Rajesh","Ramesh","Raj","Rajesh Kumar"]
print("The largest Name is : ",largest_name(names))


# Function - 5 print the table of a given Number
def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
    
num = int(input("Enter Any Number for Print their Table : "))
table(num)



# Function - 6  Print the second largest element from the array

# Method - 1
def second_largest(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>max):
            max = arr[i]
    arr.remove(max)
    max = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>max):
            max = arr[i]
    return max

# Method -2
def second_largest(arr):
    maxi = max(arr)
    ans = 0
    for i in range(0,len(arr)):
        if(arr[i]>maxi):
            ans = maxi
            maxi = arr[i]
        elif(arr[i]>ans and arr[i]!=maxi):
            ans = arr[i]
    return ans


arr =[1,2,3,4,5,6,7,8,9,10,11,23,456,787,78,87,6]
print(second_largest(arr))