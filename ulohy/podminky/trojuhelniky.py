import math

#Načti čísla
A= float(input("Zadej délku strany A: "))
B= float(input("Zadej délku strany B: "))
C= float(input("Zadej délku strany C: "))

#Rozhodnutí o trojúhelníku
if A+B>C and B+C>A and A+C>B:

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



#BONUS
if A>B:
    X=A
else:
    X=B

if not X>C:
    X=C

if A**2 + B**2 + C**2 - X**2 == X**2:
    print ("Trojúhelník je pravoúhlý")

elif A**2 + B**2 + C**2 - X**2 < X**2:
    
    print ("Trojúhelník je tupoúhlý")   
else:
    print ("Trojúhelník je ostroúhlý")   
    