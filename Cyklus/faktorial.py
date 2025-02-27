import math

#Zadej číslo
X = int(input("Zadej přirozené číslo: "))
faktorial = 1

if X <= 0:
    print("Zadaná hodnota není přirozené číslo")



else:
    for i in range (1, X+1):
        faktorial*=i
    print(f"Faktoriál čísla {X} je {faktorial}")