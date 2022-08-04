import sys

#testingresd
#test2

def without():

    AGE_OF_STARTING = int(input("Please enter the age when you start to save money: "))
    AGE_OF_RETIREMENT = int(input("Please enter the age when you want to retire: "))

    AMOUNT_OF_MONTHS = (AGE_OF_RETIREMENT - AGE_OF_STARTING) * 12

    if AMOUNT_OF_MONTHS == 0:
        print("Age of starting and retirement can not be identical")
        exit

    INTEREST_RATE_PROCENT = float(input("Please input interest rate (in procent): "))

    INTEREST_RATE = 1 + INTEREST_RATE_PROCENT / 100

    FINAL_MONEY = float(input("Please input final amount of money that you want to have (any currency): "))

    MONTHY_SAVING_FLOAT = FINAL_MONEY / (((INTEREST_RATE ** AMOUNT_OF_MONTHS) - 1) / (INTEREST_RATE - 1))

    MONTHY_SAVING = int(MONTHY_SAVING_FLOAT)

    print(f"You have to save {MONTHY_SAVING} every month!")

def with2():

    AGE_OF_STARTING = int(input("Please enter the age when you start to save money: "))
    AGE_OF_RETIREMENT = int(input("Please enter the age when you want to retire: "))

    AMOUNT_OF_MONTHS = (AGE_OF_RETIREMENT - AGE_OF_STARTING) * 12

    if AMOUNT_OF_MONTHS == 0:
        print("Age of starting and retirement can not be identical")
        exit

    INTEREST_RATE_PROCENT = float(input("Please input interest rate (in procent): "))
    MONTHY_INCREASE_PROCENT = float(input("Please input monthy inrease of savings rate (in procent): "))

    INTEREST_RATE = 1 + INTEREST_RATE_PROCENT/100
    MONTHY_INCREASE = 1+ MONTHY_INCREASE_PROCENT/100

    FINAL_MONEY = float(input("Please input final amount of money that you want to have (any currency): "))

    MONTHY_SAVING_FLOAT = FINAL_MONEY / (AMOUNT_OF_MONTHS * (INTEREST_RATE**(AMOUNT_OF_MONTHS-1)))

    MONTHY_SAVING = int(MONTHY_SAVING_FLOAT)

    print(f"You have to save {MONTHY_SAVING} every month!")

def main():

    print("Magic of compound interest!")

    DECISION = int(input("Type 1 for calculation without increasing monthy saving, 2 with inresaing monthy saving \n"))

    if DECISION==1:
        without()
    elif DECISION==2:
        with2()

if __name__ == "__main__":
    sys.exit(main())



