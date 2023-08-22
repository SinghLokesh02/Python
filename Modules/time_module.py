'''
As the name suggests Python time module allows to work with time in Python. It allows functionality like getting the current time, pausing the Program from executing, etc. So before starting with this module we need to import it. 

Importing time module
The time module comes with Python’s standard utility module, so there is no need to install it externally. We can simply import it using the import statement.


What is epoch?
The epoch is the point where the time starts and is platform-dependent. On Windows and most Unix systems, the epoch is January 1, 1970, 00:00:00 (UTC), and leap seconds are not counted towards the time in seconds since the epoch. To check what the epoch is on a given platform we can use time.gmtime(0).


'''

print("This File Contains the code of time module of python\n")

import time

print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: " , time.asctime())




# Run some code after few seconds
time.sleep(5)
print("\nThis code will start executing after 5 seconds\n")

'''
Getting current time in seconds since epoch

time.time() methods return the current time in seconds since epoch. It returns a floating-point number.
'''
print(time.time())


'''
time.localtime() method
localtime() method returns the struct_time object in local time. It takes the number of seconds passed since epoch as an argument. If the seconds parameter is not given then the current time returned by time.time() method is used.
'''

print(time.localtime())


# Get Formatted time
# print(time.asctime(time.localtime()))


from time import gmtime, strftime   # gmtime() method returns the struct_time object in UTC time. It takes the number of seconds passed since epoch as an argument. If the seconds parameter is not provided then the current time returned by time.time() method is used.
formatted = strftime("%y-%m-%d %H:%M:%S", gmtime())
print(formatted)



# Get the runtime of a  program

def check_while():
    i = 0
    while i < 1000000:
        i += 1

def check_for():
    for i in range(1000000):
        pass


start = time.time() # here we are taking the time before the execution of the program 
check_while()
gettime = time.time()-start # here we are taking the time after the execution of the program and then subtracting the time before the execution of the program from it


start = time.time()
check_for()
end = time.time()

print("Time taken by while loop: ", gettime)
print("Time taken by for loop: ", end - start)