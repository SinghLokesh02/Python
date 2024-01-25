# Multiple Values to a variable

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)


# Swap 2 Variable
a, b = 98, 12
a, b = b, a
print(a)
print(b)


# Give Same Values to all variables

n1 = n2 = n3 = "Same"
print(n1, n2, n3)


# List to Values (Unpack Values)
dishes = ["Dal Chawal", "Chicken", "Mutton", "Egg-curry", "Chicken-Tikka"]

d1, d2, d3, d4, d5 = dishes
print(d1, d2, d3, d4, d5)


# Global Variable - Method -1
x = "Python is Global used Language."


def myfunc():
    print(x + " This is amazing na !!")


myfunc()


# Global Variable - Method -2

def myfunction():
    global name
    name = "Lokesh Singh"
    print(f"My name is : {name}")
myfunction()

def run():
    print(f"I'm function 2 But my name is : {name}")
run()


# Datatypes
print("\n Datatypes in Python \n")

num1 = 1
num2 = 1j
num3 = ["one","two",3]
num4 = (1,2,3,4,"last")
num5 = {"name":"Lokesh Singh","role":"Software Trainer","company":"Miracle IT Career Academy"};
num6 = 20.5
num7 = range(30)
num8 = "This is str"

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))
print(type(num6))
print(type(num7))
print(type(num8))


# For else Loop -> If the loop over without any break or by natural condition then else condition will be executed otherwise not

for i in range(11):
    if i==9:
        break
    print(i)
else:
    print("The Loop is successfully Over Now !!")