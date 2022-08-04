array = [] #creating array

n = int(input("Please input number of numbers in list: "))

for i in range(n): #input of numbers in array
    array.append(input())

for i in range(len(array)-1): #global loop
    for i in range(len(array)-1): #local loop
        temp=0
        if array[i]>array[i+1]: #change variables algorithm
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
        else:
            continue

print(array) #printing array at the of the program



