# Python programming language provides the following types of loops to handle looping requirements. Python provides three ways for executing the loops. While all the ways provide similar basic functionality, they differ in their syntax and condition-checking time.

# 1 -> For Loop

print("\n\n This is Example of While For In Python")
for i in range(0,100):
    print(i)
    
for i in range(0,100,3):#print every 3rd element from 0-99
    print(i)

# loops in string

str = "Lokesh Singh"
# Example of for-in Loop in python
for character in str:
    print(character)
    
    
# 2 -> While Loop
print("\n\n This is Example of While loop In Python")
i = 0
while(i<=10):
    print(i)
    i = i+1 #Python doesn't support i++