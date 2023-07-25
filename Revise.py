# print("This is the assignment file")

# Question - 1 Make a program to add the sum of array Elements
def sum(arr):
  add = 0
  for i in range(0,len(arr)):
    add += arr[i]

  print("The sum of array element is : ",add)

arr = [1,2,3,4,5]
sum(arr)


# Question - 2 Make a program to find the largest number in an array
def maximum(array):
    print("The maximum element in the array is : ",max(arr))
  
n = int(input("Enter the size of arr : "))
arr = []
for i in range(0,n):
  x = int(input())
  arr.append(x)

print(arr)
maximum(arr)


# Question - 3 Make a program to find the smallest number in an array
def minimum(array):
    print("The minimum element in the array is : ",min(arr))
  
n = int(input("Enter the size of arr : "))
arr = []
for i in range(0,n):
  x = int(input())
  arr.append(x)

print(arr)
minimum(arr)


# Question - 4 Make a program that prints second largest element from the array
def second_Max(arr):
  maxi = max(arr)
  second_max = min(arr)
  for i in range(0,len(arr)):
    if(maxi<arr[i]):
      second_max = maxi
      maxi = arr[i]
    else:
      if(arr[i]>second_max and arr[i]!=maxi):
        second_max = arr[i];

  print("Second maximum elements of the array is : ",second_max)
    
  

n = int(input("Enter the size of arr : "))
arr = []
for i in range(0,n):
  x = int(input())
  arr.append(x)

second_Max(arr)


# Question - 5 Make a program that take username as input and that prints the length of the name
def print_len(name):
  print("The length of the given string is : ",len(name))
name = input("Enter your name : ")
print_len(name)


# Question - 6 Make a program that take array as input and prints every alternate elements
def print_alternate(array):
    print("The alternate elements of the array are : \n")
    for i in range(0,len(array),2):
      print(array[i])
  
n = int(input("Enter the size of arr : "))
arr = []
for i in range(0,n):
  x = int(input())
  arr.append(x)
print_alternate(arr)

