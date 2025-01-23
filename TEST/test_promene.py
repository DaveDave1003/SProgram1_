import math

#Načti čísla
A= float(input("Zadej délku strany A: "))
B= float(input("Zadej délku strany B: "))
C= float(input("Zadej délku strany C: "))

#Rozhodnutí o trojúhelníku
if A+B>=C and B+C>=A and A+C>=B:

    #RovnostRAN
    if A == B and B==C:
        print(f"Strany {A}, {B}, {C} tvoří rovnostranný trojúhelník.")

    #RovnoRAM
    elif A == B or B == C or A == C:
        print(f"Strany {A}, {B}, {C} tvoří rovnoramenný trojúhelník.")

    #ObecNY
    else:
        print(f"Strany {A}, {B}, {C} tvoří obecný trojúhelník.")

#NeexistuJE
else:
    print(f"Strany {A}, {B}, {C} netvoří trojúhelník.")