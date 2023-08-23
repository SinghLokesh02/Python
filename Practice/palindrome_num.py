n = int(input("Enter Any Number : "))

temp = n
rev = 0

while(n>0):
    rem = n%10;
    rev = rev*10+rem;
    n = n//10;

if(temp == rev):
    print("The numbers are Palindrome Number");
else:
    print("The numbers are Not a Plaindrome Numbers")