import math

def porovnej_3 (Cislo_1, Cislo_2, Cislo_3):

    #Výpočet hodnot
    if Cislo_1>=Cislo_2 and Cislo_1>=Cislo_3:
        return (f"Největší číslo: {Cislo_1}")

    elif Cislo_2>=Cislo_1 and Cislo_2>=Cislo_3:
        return (f"Největší číslo: {Cislo_2}")

    elif Cislo_3>=Cislo_1 and Cislo_3>=Cislo_2:
        return (f"Největší číslo: {Cislo_3}")





#Zadej 3 libovolné hodnoty
Cislo_1= int(input("Zadej první číslo: "))
Cislo_2= int(input("Zadej druhé číslo: "))
Cislo_3= int(input("Zadej třetí číslo: "))


print(porovnej_3(Cislo_1, Cislo_2, Cislo_3))