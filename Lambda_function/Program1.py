# Write a lambda method to find the Average of 3 Numbers


# Taking 3 Integer Input
x, y, z = map(int, input("Enter three Numbers : ").split())
Avg = lambda a, b, c: (a + b + c) / 3
print(f"The Average of {x,y,z} is {Avg(x,y,z)}")


# Write a Program to Add 3 strings
s1, s2, s3 = input("Enter 3 strings : ").split()
sumOfStrings = lambda s1, s2, s3: s1 + s2 + s3
print(f"The Sum of {s1,s2,s3} is {sumOfStrings(s1,s2,s3)}")
