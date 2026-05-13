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


import math


class Zlomek:
    def __init__(self, citatel, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        
        if jmenovatel == 0:
            pass

        self = self.zkrat()
        
    def zkrat(self):
        #Nejmenší Společný Dělitel
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        
        self.citatel = self.citatel / nsd 
        self.jmenovatel = self.jmenovatel / nsd 
       
        pass

    
    
    def __str__(self):
       return f"{int(self.citatel)} / {int(self.jmenovatel)}"
        




z = Zlomek(6, 2)
print(z)  # Mělo by vypsat: 3/4
z2 = Zlomek(5, 10)
print(z2)  # Mělo by vypsat: 5/1

