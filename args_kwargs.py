print("In this we are going to learn *args and **kwargs in python")

# Normal way to pass aregument
# The code you provided is showing an error because you have defined two functions with the same name sum, but with different numbers of arguments. Python does not support function overloading like some other programming languages, where you can have multiple functions with the same name but different parameter lists.

def sum(a,b,c):
    print("The sum of given numbers is : ",a+b+c)
    
def add(a,b,c,d):
    print("The sum of given numbers is : ",a+b+c+d)
    
sum(1,2,3)
add(1,2,3,6)

# Better way to do the above program

def get_sum(*args):
    sum = 0
    for i in range(0,len(args)):
        sum += args[i]

    print("The sum of given Numbers is : ",sum)
    
get_sum(1,2,3,7,8)


# If we want to pass Normal argument then you can do it in the following ways

####### The syntax of doing it is : (normal paramter,*args,**kwargs) #####

def print_student(normal,*student,**dict):
    # We can also Print list of *args by index as well
    # print(student[6])
    
    print(normal)
    for i in student:
        print(i)
    
    print("\n Now the name and Post of person in my class are : \n")
    for key,value in dict.items():
        print(f"{key} is {value}")
s = "The name of students in my class are : "
stu = ["lokesh","diwakar","Aniket","Ritik","Akshay","Risabh","Nayan"]


# **Kwargs in Python
dict = {
    "Lokesh" :"IT Trainer",
    "Diwakar" :"Top Coder",
    "Aniket" :"Full Stack Dveloper",
    "Akshay" :"Software Engineer",
    "Ritik" :"Coder cum Developer",
    "Nayan" :"Backend Developer",
    "Tanmay" :"python Developer" 
    
}

print_student(s,*stu,**dict)



# Clear The concept of kwargs
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
