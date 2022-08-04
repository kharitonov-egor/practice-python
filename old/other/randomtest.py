import random
bols=0
ravn=0
men=0

for number in range(1,101):
    for i in range(1,1001):
        x=random.randint(0,1)
        y=random.randint(0,1)

        if x>y:
            bols+=1
        elif x==y:
            ravn+=1
        elif x<y:
            men+=1

    print(number)
    print(bols)
    print(ravn)
    print(men)
    print("======")

    bols = 0
    ravn = 0
    men = 0
