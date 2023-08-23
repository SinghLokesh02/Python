def check_prime(num):
    i=1;
    count = 0
    while(i<=num):
        if(num%i==0):
            count = count+1
        i = i+1

    if(count==2):
        print("It is a Prime Number")
    else:
        print("It is not a prime Number")
        
        
num = int(input("Enter any Number : "));
check_prime(num)