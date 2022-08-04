import time
start_time = time.time()

def bubble(array):
    for i in range(len(array)-1):
        for i in range(len(array)-1):
            temp=0
            if array[i]>array[i+1]:
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
            else:
                continue

    print(array)

b=[]

for i in range(1000,1,-1):
    b.append(i)

bubble(b)

print("--- %s seconds ---" % (time.time() - start_time))
