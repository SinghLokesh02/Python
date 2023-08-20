'''
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
'''

# Create a file called "new_file.txt":
# f = open("new_file.txt",'x')


# Example for ' a ' mode
f = open("new_file1.txt",'a')
# # Create a file called "new_file1.txt":


# Example for ' w ' mode
f = open("new_file2.txt",'w')
# # Create a file called "new_file2.txt":