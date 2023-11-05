# Basic Python Revision

# Print
print("hello World my name is Lokesh Singh")
print("My father is a great father", end=" ")
print("My brother is a little bit lazy one")

# ****************************** Operator in Python ******************************

# 1 Assignment Operator (=, +=, -=, *=, /=)

num = 10
print(num)

num += 10
print(num)

num -= 10
print(num)

num *= 10
print(num)

num /= 10
# Single / gives answer in decimal
print(num)

num //= 10  # Double // give answer in Integer
print(num)

# Comparison Opeator
a = 10
b = 50

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# Logical Operator

print(a == 10 and b == 40)
print(a == 10 or b == 40)

# Arithmetic Operator (-,+,*,/,%)
n = 10
print(n)

n = n + 10
print(n)

n = n - 10
print(n)

n = n * 10
print(n)

n = n // 10
print(n)

n = n % 10
print(n)


# ********************************** Conditional Statement in Python **********************

age = int(input("Enter Your Age: "))
if age <= 0:
    print("You have entered Invalid Age please reenter you age")
elif age < 6:
    print("Your age is so low enjoy your life")
elif age < 13:
    print("You are growing Up please take of your health")
elif age < 18:
    print("You are minor but start atleast 1 hour a day")
elif age < 25:
    print("Focus on your studies and achieve your goal")
else:
    print("Your are well matured now take your decision")


# *********************** Loops in Python *************************

# For Loop
num = int(input("Enter any Number : "))
for i in range(1, num + 1):
    print(i, end=" ")
print()

# While Loop

num = int(input("Enter any Number : "))
i = 1
while i <= num:
    print(i, end=" ")
    i += 1
print()

#  Functions in Python


# Simple funtion without arguments
def Saysomething():
    print("hey there hello welcome to the world of coding")


Saysomething()

# Write a function to check whether a number is composite or Not

# Definition Of Composite Number -> Composite numbers have more than two positive divisors. They can be divided by 1, themselves, and at least one other positive integer.


def prime(number):
    if number < 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0

    return 1


def Check_composite(number):
    if number < 4:
        return 0
    if prime(number) == 1:
        return 0
    return 1


number = int(input("Enter any number to check Composite : "))
if Check_composite(number):
    print("The Number is Composite Number")
else:
    print("The number is not a composite number")


# ************************************* String *************************************

# ************************************* List  *************************************

""" The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are mutable. Therefore, it is possible to change a list but not a tuple. The contents of a tuple cannot change once they have been created in Python due to the immutability of tuples. """

# ************************************* Dictionary *************************************

# ************************************* Class and Obejcts *************************************

class Student:
    def sum(self,a,b):
        print("The sum of 2 Number is : ", (self.a+self.b))

lokesh = Student()
lokesh.a = 78
lokesh.b  = 2
lokesh.sum(a,b)


# Class to set and get data of the student
class Data:
    name = ""
    email = ""
    roll = 0
    age = 0
    def set_data(self,name,email,age,roll):
        self.name = name
        self.email = email
        self.age = age
        self.roll = roll
    def get_data(self):
        print("The name is : ",self.name)
        print("The Email is : ",self.email)
        print("The Age is : ",self.age)
        print("The Roll Number is : ",self.roll)
        

sonali = Data()
sonali.set_data("Sonali Singh","sonali927@gmail.com",23,58)
sonali.get_data()
lokesh = Data()
lokesh.set_data("Lokesh Singh","lokeshsingh7695@gmail.com",21,25)
lokesh.get_data()


# ************************************* Constructor  *******************************


class newData:
    def __init__(self):
        print("I'm Default Constructor Of this Class")

n = newData()

# Parameterised Constructor
class Data:
    name = ""
    email = ""
    roll = 0
    age = 0
    def __init__(self,name,email,age,roll):
        self.name = name
        self.email = email
        self.age = age
        self.roll = roll
    def get_data(self):
        print("The name is : ",self.name)
        print("The Email is : ",self.email)
        print("The Age is : ",self.age)
        print("The Roll Number is : ",self.roll)
        

sonali = Data("Sonali Singh","sonali927@gmail.com",23,58)
sonali.get_data()
lokesh = Data("Lokesh Singh","lokeshsingh7695@gmail.com",21,25)
lokesh.get_data()


# ************************************* Inheritance *************************************

print("This is the Basic Example of the Inheritance")
class Parent:
    p_money = 100000;

class Child(Parent):
    c_money = 500000
    
    def __init__(self):
        print("The Total money is : ",self.p_money + self.c_money)
    
lokesh = Child()