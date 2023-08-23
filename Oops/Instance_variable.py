# Instance Variable Vs Class Variable


class Employee:
    company = "Google"
    salary = 100


harry = Employee()  # Instance Variable
rajni = Employee()  # Instance Variable

# Creating instance variable salary for both the objects
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)

harry.company = "YouTube"  # Class Variable
print(harry.company)
print(rajni.company)

print(harry.salary)
print(rajni.salary)


# priority of instance variable is more than class variable
# if instance variable is not present then it will take class variable
# if instance variable is present then it will take instance variable
# if instance variable is not present and class variable is not present then it will give error
