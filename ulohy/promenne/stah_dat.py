import math

#Napiš libovolné hodnoty
Objem_dat = float(input("Zadej objem dat v MB: "))
Rychlost_stahovani = float(input("Zadej rychlost stahování v Mbit/s: "))

doba= (Objem_dat * 8) / (Rychlost_stahovani)

print(f"Doba stahovani: {round(doba,2)}")