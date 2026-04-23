import math


# INPUT
A = float(input("Zadejte základ: "))
B = int(input("Zadejte exponent: "))

# Výpočet
X = 1
for x in range(abs(B)):
    X *= A

# Pokud je exponent záporný, obrátíme výsledek
if B < 0:
    X = 1 / X

# VÝSLEDEK
print(f"Výsledek {A} ^ {B} je {X}.")


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