# Načtení délky prvního seznamu 
delka1 = int(input("Zadej délku prvního seznamu: "))
seznam1 = []

for i in range(delka1):
    num = int(input(f"Zadej číslo {i + 1} pro první seznam: "))	
    seznam1.append(num)

# Načtení délky druhého seznamu
delka2 = int(input("Zadej délku druhého seznamu: "))
seznam2 = []
for i in range(delka2):
     num = int(input(f"Zadej číslo {i + 1} pro druhý seznam: ")) 
     seznam2.append(num)


# Slučování seznamů střídavě
slouceny_seznam = []
min_length = min(delka1, delka2)
for i in range(min_length): 
    slouceny_seznam.append(seznam1[i]) 
    slouceny_seznam.append(seznam2[i])

# Přidání zbývajících prvků
slouceny_seznam.extend(seznam1[min_length:])
slouceny_seznam.extend(seznam2[min_length:])
print("Výsledný seznam:", slouceny_seznam)