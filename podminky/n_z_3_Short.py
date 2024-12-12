import math

#Zadej 3 libovolné hodnoty
Cislo_1= float(input("Zadej první číslo: "))
Cislo_2= float(input("Zadej druhé číslo: "))
Cislo_3= float(input("Zadej třetí číslo: "))

#Výpočet hodnot
if Cislo_1>Cislo_2:
    x=Cislo_1
else:
    x=Cislo_2

if x>Cislo_3:
    print (x)
else:
    print (Cislo_3)