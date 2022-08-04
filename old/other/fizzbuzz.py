import time
start_time = time.time()
summa=0
for i in range(1,100000000):
    summa+=i
print(summa)

print("--- %s seconds ---" % (time.time() - start_time))


