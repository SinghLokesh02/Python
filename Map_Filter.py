# Map and filter Methods in Python
# In Python, map and filter are built-in functions that allow you to apply a function to each element of an iterable (like a list) and filter elements based on a condition, respectively.

def checkEven(num):
    return num%2 == 0

lst = [1,2,3,4,5,6,7,89]

# Map Syntax
# map(function, iterable)
ans = list(map(checkEven,lst))
print(ans)

# filter Syntax
# filter(function, iterable)
ans = list(filter(checkEven,lst))
print(ans)