#součet svých dělitelů (kromě sebe), je rovno původnímu číslu
#0-1000, 6= 1+2+3, 28=1+2+4+7+14

import math


for j in range(1,1000):
    soucet = 0
    for i in range(1,j):
        if j % i == 0:
            soucet += i
    if j == soucet:
        print(f"{j} je perfektní číslo")



