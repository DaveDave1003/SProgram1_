import math

#Napiš libovolné hodnoty
vyska = int(input("Zadejte výšku: "))
polomer = int(input("Zadejte poloměr: "))


#Výsledné hodnoty
print (f"Povrch válce: {round (2 * math.pi * polomer * (polomer + vyska), 2)} cm2")
print (f"Objem válce: {round (math.pi * polomer ** 2 * vyska, 2)} cm3")


