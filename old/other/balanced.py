n=int(input("Input a number: "))

number_digits=len(str(n))

central_digit=0

if number_digits % 2 != 0:
    central_digit = (number_digits//2) + 1
    n=str(n)
    central_def = n[central_digit]
    sum1 = 0

    for i in n:
        if int(n[i])<int(central_def):
            sum1+=n[i]

    print(sum1)

    print(sum1)
else:
    print("not!")