'''
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

lambda arguments: expression

Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

'''

# Write a Program to print the square and cube of a number using the lambda keyword

square = lambda x : x**2
cube = lambda x : x**3

num = int(input("Enter a Number : "))
print(f'The Square of a {num} is : {square(num)}')
print(f'The Cube of a {num} is : {cube(num)}')
