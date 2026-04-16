import math


def test_prvociselnosti(cislo):
    
    if cislo <= 0:
        return False
    
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    
    return True






vstup = int(input("Zadej přirozené číslo: "))



print(f"Číslo {vstup} {"je" if test_prvociselnosti(vstup) else "není"} prvočíslo")