# Fibonacci Using Loops

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a,end=" ")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c,end=" ")

fibonacci(10)


# Using recursion

def Fibonacci(n):
    if(n < 1):
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fib_series = Fibonacci(n-1)
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series
        
ans = Fibonacci(10)
print(ans)