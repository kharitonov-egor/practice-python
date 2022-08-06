# Distance calculator for minecraft coordinates

import math

BASE = [-1597, 103]
# x,z

numberOfCalculations = int(input("Please input number of distance calculated: "))

for i in range(numberOfCalculations):
    x, z = [int(k) for k in input().split()]

    distance = ((x - BASE[0])**2 + (z - BASE[1])**2) ** (1/2)

    print(f"Calculation {i+1}: {distance}")

    