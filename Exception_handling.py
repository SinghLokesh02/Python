# Exception Handling In python

'''
Difference between Syntax Error and Exceptions
Syntax Error: As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of the program. 

Ex-

# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")


Exceptions: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.
'''

# Basic Example - 1
try:
    a = 5
    b = 0
    x = a/b
    print(x)
except:
    print("Their is a error")


# Basic Example - 2
try:
    a = 5
    b = "Lokesh"
    sum = a+b
    print(sum)
except Exception as e:
    print("We cannot Add string and number together sorrry!!")
    print(e)


'''
Finally Keyword in Python
Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after the normal termination of the try block or after the try block terminates due to some exception.


Raising Exception
The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception)



Advantages of Exception Handling:

Improved program reliability: By handling exceptions properly, you can prevent your program from crashing or producing incorrect results due to unexpected errors or input.
Simplified error handling: Exception handling allows you to separate error handling code from the main program logic, making it easier to read and maintain your code.
Cleaner code: With exception handling, you can avoid using complex conditional statements to check for errors, leading to cleaner and more readable code.
Easier debugging: When an exception is raised, the Python interpreter prints a traceback that shows the exact location where the exception occurred, making it easier to debug your code.



Disadvantages of Exception Handling:

Performance overhead: Exception handling can be slower than using conditional statements to check for errors, as the interpreter has to perform additional work to catch and handle the exception.
Increased code complexity: Exception handling can make your code more complex, especially if you have to handle multiple types of exceptions or implement complex error handling logic.
Possible security risks: Improperly handled exceptions can potentially reveal sensitive information or create security vulnerabilities in your code, so it’s important to handle exceptions carefully and avoid exposing too much information about your program.

'''

#We Generally use finally keyword with functions in python function return from in-between from the function and we have to execute some code after return statement then we use finally keyword


# Example of Finally in python if you didn't use finally here the "Hey Name name is Lokesh Singh" will not executed
def divide(a,b):
    try:
        print(a//b)
        return 1
    except:
        print("The division of Number by 0 is an Error")
        return 0
    
    finally:
        print("Hey Name name is Lokesh Singh")
    

num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2 : "))
divide(num1,num2)