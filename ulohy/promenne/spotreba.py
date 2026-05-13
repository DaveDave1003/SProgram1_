S = int(input("Zadej vzdálenost: "))
F = int(input("Zadej průměrnou spotřebu na 100km: "))
C = int(input("Jaká je cena paliva: "))

#Palivo
Fuel = (S / 100) * F

#Cena paliva
Cost = Fuel * C


print(f"Palivo: {Fuel} l, Cena: {Cost} Kč")
