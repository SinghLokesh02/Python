print("This program is to give example of armstrong number")

num = int(input("Enter any Number : "))
temp = num

sum = 0
while(num>0):
    rem = num%10
    sum += rem*rem*rem
    num = num//10

if(temp == sum):
    print("The Numbers are Armstrong Numbers")
else:
    print("The Numbers are Not Armstrong Numbers")