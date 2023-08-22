# Python math Module

'''
Python math Module
Python has a built-in module that you can use for mathematical tasks.

The math module has a set of methods and constants.


Study link -> https://www.w3schools.com/python/module_math.asp
'''

import math #->This will import all methods o maths

from math import sqrt # This will import only sqrt method from maths library

# x = int(input("Enter A Number to get Sqrt of that Number : "))
print(sqrt(64))


# math.floor()	Rounds a number down to the nearest integer
print(math.floor(9.8))

print(math.ceil(9.9))


# get the value of pie
pie = math.pi
print(pie)


# Print factorial using python maths library
print(math.factorial(7))


# math.exp()	Returns E raised to the power of x
print(math.exp(2))


# math.fabs()	Returns the absolute value of a number
print(math.fabs(-9))


# math.fmod()	Returns the remainder of x/y
print(math.fmod(3,2))



# math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
arr = [1,2,3,45,5]
tup = (1,2,34,5)
print(math.fsum(arr))
print(math.fsum(tup))


# math.gcd()	Returns the greatest common divisor of two integers
print(math.gcd(6,3))


# math.isfinite()	Checks whether a number is finite or not
# math.isinf()	Checks whether a number is infinite or not
x = 90
print(math.isfinite(x))



# math.pow()	Returns the value of x to the power of y
print(math.pow(2,3))


# math.prod()	Returns the product of all the elements in an iterable
print(math.prod(arr))



# math.trunc()	Returns the truncated integer parts of a number
print(math.trunc(9.99))


# math.radians()	Converts a degree value into radians
print("Converting Degree into radians")
print(math.radians(90))


# math.degrees()	Converts an angle from radians to degrees
print(math.degrees(1.5707963267948966))


# math.e	Returns Euler's number (2.7182...)
print(math.e)


# math.pi	Returns Euler's number (2.7182...)
print(math.pi)


# math.tau	Returns Euler's number (2.7182...)
print(math.tau)

# math.inf	Returns a floating-point positive infinity
print(math.inf)