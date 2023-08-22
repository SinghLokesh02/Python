# Walrus Operator
'''
the biggest change is the addition of assignment expressions. Specifically, the := operator gives you a new syntax for assigning variables in the middle of expressions. This operator is colloquially known as the walrus operator.
'''

# Example 
a = True
# print(a=False) This will give me a error

print(a:=False)

# Example - 2
arr = [1,2,3,4,5]
while (n:=len(arr)>0):
    print(arr.pop())

print(arr)


# Example - 3
foods = list()
while(food := input("What food do you like? ")!="quit"):
    foods.append(food)

print(foods)