# String in python

name = "Lokesh Singh";
print(name)

name1 = "Hello my father's name is : "
name2 = '''Hello my name is : "Lokesh Singh"'''
print(name1)
print(name2)


# Print any character in python with the help of indexing
print(name[0])

# Printing all the characters with the help for in loop
for character in name:
  print(character,end=" ")

print()
# String slicing in python
name = "Mynameislokesh"
print(name[0:6])#Exclude the last character
print(name[0:])#print from given index up to the last character
print(name[:])#print from begin to the last character

print(name[0::2])#print every second character upto the last if you not define the last by default it prints upto the last character


# String Methods in Python

a = "harsh Singh"
# Length of the strings
print(len(a))

# Print in uppercase -> Converts the string into uppercase
print(a.upper());

# Print in lowercase -> Converts the string into lowercase
print(a.lower());

# Check the string is in lowercase or not return 0 if not otherwise 1
print(a.islower())


# Check the string is in uppercase or not return 0 if not otherwise 1
print(a.isupper())

#Replace the string with the the given string
print(a.replace("harsh","Lokesh"))

#Split method covert the str in list for split your str must have space
a_new ="hey my name is lokesh singh lokesh"
print(a_new.split(" "))

# str capitalize method -> It convert the str first letter capital
print(a_new.capitalize())

#return the count of given  string
print(a_new.count("lokesh"))


# Check string endswith particular substring
print(a_new.endswith("mukesh"))

# Check string startswith particular substring
print(a_new.startswith("hey"))

# return the index of given string
print(a_new.find("my"))


a_new1 = "heythere"
# Check whether string contain alphanumerical values a-z,A-Z,0-9
print(a_new1.isalnum())

# Check whether string contain alphabetical values a-z,A-Z
print(a_new1.isalpha())

# Check whether string contains any space ->return true if string contains only spaces
print(a_new.isspace())
