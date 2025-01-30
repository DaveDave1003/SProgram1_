import math

#Zadej číslo
X = int(input("Zadej přirozené číslo: "))
faktorial = 1

if X <= 0:
    print("Zadaná hodnota není přirozené číslo")



else:
    for x in range (1, X+1):
        faktorial*=x
    print(f"Faktoriál čísla {X} je {faktorial}")