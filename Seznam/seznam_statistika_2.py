import random

# Načtení délky seznamu od uživatele
delka = int(input("Zadej délku seznamu: "))

# Vytvoření prázdného seznamu
cisla = []

# Naplnění seznamu náhodnými čísly
for i in range(delka):
    cislo = random.randint(1, 100)
    cisla.append(cislo)

# Výstup seznamu
print("Vygenerovaný seznam:", cisla)


#zjisteni nejmensiho cisla
nejmensi = 101

for cislo in cisla:
    if cislo < nejmensi:
        nejmensi = cislo

print(f"Nejmensi nalezene cislo je {nejmensi}");

#zjisteni nejvetsiho cisla
nejvetsi = cisla[0]

for cislo in cisla:
    if cislo>nejvetsi:
        nejvetsi = cislo

print(f"Nejmensi nalezene cislo je {nejvetsi}");


soucet = 0

for cislo in cisla:
    soucet += cislo

prumer = soucet / len(cisla)

print(f"Prumer cisel je: {prumer}")


