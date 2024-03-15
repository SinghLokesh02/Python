
def GetLCM():
    a = int(input("Enter Number 1 : "))
    b = int(input("Enter Number 1 : "))
    c = int(input("Enter Number 1 : "))

    maxi = max(a, b, c)
    while(True):
        if(maxi%a ==0 and maxi%b == 0 and maxi%c ==0):
            lcm = maxi
            break
        maxi += 1
    
    print(lcm)
                 


# Main Function
if __name__ == "__main__":
    GetLCM()
