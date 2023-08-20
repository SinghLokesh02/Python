# To open a file for reading it is enough to specify the name of the file:
# f = open("demofile.txt")

# The code above is the same as:
# f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# Note: Make sure the file exists, or else you will get an error.

'''
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

'''



f = open("lokesh.txt","r")
print("\n\n The data in the file is : \n\n")
# The read() function will print all the data of the file
# print(f.read())


# read(5) -> This will print 5 character from the file
# print()
# print(f.read(7))



# Read Lines
# You can return one line by using the readline() method:

# print(f.readline())

# By calling readline() two times, you can read the two first lines:
# print(f.readline())
# print(f.readline())



# By looping through the lines of the file, you can read the whole file, line by line:
for x in f:
    print(x)
    
    
'''
Close Files
It is a good practice to always close the file when you are done with it.
f.close()
'''
