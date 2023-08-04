# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

name = input("Enter your name : ")
print(name) # The name inputed by the user is by default a string

# To convert the string into integer we use int() function
num = input("Enter any Number : ")
print(type(num)) # So it belongs to str class

num = int(num) #Now it is type casted to the integer class
print(type (num))

string = str(num)
print(string ," The type of the data is : ",type(string))


f = float(1) #int value type casted to float
print(f)

x = int(6.89) #Float value is type casted to int
print(x)