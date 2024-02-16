# How To Take Multiple Inputs In Python Using For Loop

# Defining the number of data you want to take input
size = 6

# Creating an Empty list
my_list = []

# Taking input with the help of for loop
for i in range(size):
    x = input(f"Enter data {i+1} : ")
    my_list.append(x)

# Printing the list
for data in my_list:
    print(data,end=' ')


#  Combining inputs with input().split():

store = input("Enter multiple input separated by spaces : ").split()
ans = [data for data in store]
print("The values are : ",ans)



# Method - 3: Using Dictionary to store the data

# Size of Dictionary
size = 5
my_Dict = {}

for i in range(size):
    key = input(f"Enter the {i+1} key : ")
    value = input(f"Enter the {i+1} value : ")
    my_Dict[key] = value

# After taking all the input with the help of loop we are going to print it
print("\nThe input Values are")
for key,values in my_Dict.items():
    print(f"{key} : {values}")



# Method - 4: Repeated input with single-value storage

number_of_inputs = 5
# Variable to store all the inputs
result = 0
for i in range(number_of_inputs):
    result += int(input("Enter Any Number : "))
    

print("The total sum of inputted values is : ", result)
