'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

# opened = open("lokesh.txt",'a')
# opened.write("Hey There my Name is Lokesh Singh And I am trying to learn Pyhton")
# opened.close()

# # Now read the file
# f = open("lokesh.txt",'r')
# print(f.read())


###   Overwrite the Entire File 
'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

'''

over = open("lokesh.txt",'w')
over.write("Hey There my Name is Lokesh Singh And I am trying to learn Pyhton")
over.close()

# Now read the file
f = open("lokesh.txt",'r')
print(f.read())