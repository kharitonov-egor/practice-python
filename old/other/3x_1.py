n = int(input("Random number: "))
print("Starting for n =",n)
while n!=4:
    if n%2==0:
        n=n//2
        print(n)
    else:
        n=n+n+n+1
        print(n)
