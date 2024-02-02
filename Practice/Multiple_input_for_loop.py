# How To Take Multiple Inputs In Python Using For Loop

# Create a data type primitive data first
data1 = data2 = data3 = data4 = data5 = ""

# Run the for loop upto the number of variable you have
for i in range(5):
    globals()[f"data{i+1}"] = input(f"Enter data {i+1} : ")

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)

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
    
    


    
    