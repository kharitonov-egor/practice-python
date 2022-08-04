#EGOR KHARITOBOV 19.11.2021

print("This program can solve ferma last theorem")

till_counter = int(input(f"Please enter till what integer you will be calculating: "))
degree = int(input(f"Please enter degree of equation: "))

for x in range(1,till_counter+1):
    for y in range(1, till_counter + 1):
        for z in range(1, till_counter + 1):
            if x**degree + y**degree == z**degree:
                print(x,y,z)