# Program -1 

age = int(input("Enter your age : "))
if(age>=18):
    print("Yes you can vote ")
else:
    print("You are minor ")
    
# Program -2
marks = int(input("Enter your total marks : "))
if(marks>=90):
    print("You got Grade A")
elif(marks>=70 and marks<90):
    print("You got Grade B")
elif(marks>=40 and marks<70):
    print("You got Grade C")
else:
    print("You are fail")
    

# Program -3
num = int(input("Enter any Number : "))
if(num%2==0):
    print("The number is Even Number")
else:
    print("The number is Odd Number")