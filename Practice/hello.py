print("Hello EveryOne")

age = int(str(input("Enter Your age : ")))

if(age<0):
    print("Entered Invalid Age")
elif(age>0 and age<18):
    print("You are a minor you can't drive");
else:
    print("Yes ! You can Drive");