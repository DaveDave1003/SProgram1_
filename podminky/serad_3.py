import math

#Zadej 3 libovolné hodnoty
Cislo_1= float(input("Zadej první číslo: "))
Cislo_2= float(input("Zadej druhé číslo: "))
Cislo_3= float(input("Zadej třetí číslo: "))

#Výpočet hodnot
if Cislo_1>=Cislo_2>=Cislo_3:
    print (f"{Cislo_1} {Cislo_2} {Cislo_3}")
elif Cislo_1>=Cislo_3>=Cislo_2:
    print (f"{Cislo_1} {Cislo_3} {Cislo_2}")
elif Cislo_2>=Cislo_1>=Cislo_3:
    print (f"{Cislo_2} {Cislo_1} {Cislo_3}")
elif Cislo_2>=Cislo_3>=Cislo_1:
    print (f"{Cislo_2} {Cislo_3} {Cislo_2}")
elif Cislo_3>=Cislo_1>=Cislo_2:
    print (f"{Cislo_3} {Cislo_1} {Cislo_2}")
elif Cislo_3>=Cislo_2>=Cislo_1:
    print (f"{Cislo_3} {Cislo_2} {Cislo_1}")