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


# Example - 2
# Write a Program to check a string starts with A, a, S, or r.

check = lambda s : (s.startswith("A") or s.startswith("a") or s.startswith("S") or s.startswith("r"))

student_names = [
    "Aarav Sharma", "Vivaan Mehta", "Ananya Gupta", "Diya Verma", "Riya Singh",
    "Ishaan Patel", "Kavya Joshi", "Aryan Nair", "Nisha Kumar", "Siddharth Rao",
    "Sneha Deshmukh", "Tara Kulkarni", "Aditya Ghosh", "Meera Kapoor", "Sahil Jain",
    "Priya Menon", "Harsh Tiwari", "Sanya Chauhan", "Manav Reddy", "Aditi Shah"
]

ans = list(filter(check,student_names))
print(ans)