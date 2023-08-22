# Python Random Module
'''
Python has a built-in module that you can use to make random numbers.

The random module has a set of methods:

Study link -> https://www.w3schools.com/python/module_random.asp
'''

import random as rd

# random()	Returns a random float number between 0 and 1
print(rd.random())


# randint()	Returns a random number between the given range
print(rd.randint(0,100))


# choice()	Returns a random element from the given sequence
arr = [124,21,3,59,60,57,86]
print(rd.choice(arr))


# shuffle()	Takes a sequence and returns the sequence in a random order
rd.shuffle(arr)
print(arr)


# uniform()	Returns a random float number between two given parameters
print(rd.uniform(10,20))
