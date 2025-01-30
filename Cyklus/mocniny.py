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
