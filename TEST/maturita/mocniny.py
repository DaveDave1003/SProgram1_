import math

#INPUT
Zaklad = int(input("Zadej základ: "))
Exponent = int(input("Zadej mocninu: "))

# Výpočet
X = 1
for x in range(abs(Exponent)):
    X *= Zaklad

    # Pokud je exponent záporný, obrátíme výsledek
if Exponent < 0:
    X = 1 / X

# VÝSLEDEK
print(f"Výsledek {Zaklad} ^ {Exponent} je {X}.")