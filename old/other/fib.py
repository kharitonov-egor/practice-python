n = int(input())

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-2)+fib(n-1)

digit=fib(n)

digit_return=str(digit%10)

print(digit_return)