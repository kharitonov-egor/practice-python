#EGOR KHARITONOV
#CREATED 08.05.2021
#EDITED 29.10.2021

a=float(input("Введите коэффицент a: "))
b=float(input("Введите коэффицент b: "))
c=float(input("Введите коэффицент c: "))
D= (b**2) - (4*a*c)

x1 = 0
x2 = 0

if D<0:
    print('Корней нет!')

if D==0:
    x1= (-b) / (2*a)
    print(f"Корень: {x1}")
    print(x1)

if D>0:

    x1= ((-b) + (D**(1/2))) / (2*a)
    x2= ((-b) - (D**(1/2))) / (2*a)

    print(f"Ваши корни: {x1},{x2}")