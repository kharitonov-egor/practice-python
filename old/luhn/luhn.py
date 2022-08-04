#EGOR KHARITONOV 18.08.2021
# This program can check if any credit card number could even exist

from time import sleep
cc = input("Enter your credit card number: ")
doubled=[]
cc_doubled_cord=[0,2,4,6,8,10,12,14] #creating list of every number ic cc that should be doubled
cc_notdoubled_cord=[1,3,5,7,9,11,13] # -ll- not doubled
summa=0
ost=0
temp=0
if len(cc)==16:
    for j in cc_doubled_cord:
        if (int(cc[j])*2)<10:
            doubled.append(int(cc[j])*2)
        else:
            temp=str(int(cc[j])*2)#temp = string
            doubled.append(int(temp[0])+int(temp[1])) #adding to doubled
    for k in cc_notdoubled_cord:
        summa+=int(cc[k])
    summa+=sum(doubled)
    ost=summa%10 #ost = last digit of a summa
    if ost==0: 
        if int(cc[15])==0:
            print("Fine!")
            sleep(60)
        else:
            print("Bad!")
            sleep(60)
    else:
        if (10-ost)==int(cc[15]):
            print("Fine!")
            sleep(60)
        else:
            print("Bad!")
            sleep(60)
else:
    print("Your card must contain 16 numbers and must be typed like this XXXXXXXXXXXXXXXX!")
    sleep(60)
    
