import random

cislaUzi = []  # Seznam čísel zadaných uživatelem
cislaGen = []  # Seznam náhodně generovaných čísel

spolecna = []  # Seznam čísel, která jsou v obou seznamech
pocetVetsich = 0  # Počet čísel větších než 50 v uživatelském seznamu
prumer = 0  # Průměrná hodnota generovaných čísel

# Zadání velikosti seznamu od uživatele
velikost = int(input("Zadej velikost seznamu a potem jednotlivy cisla: "))

# Uživatel zadává čísla
for i in range(0, velikost):
    cislo = int(input(("Zadej cislo " + str(i + 1) + ": ")))
    if cislo > 50:
        pocetVetsich += 1  # Počítání čísel větších než 50
    cislaUzi.append(cislo)  # Uložení čísla do seznamu

# Generování náhodných čísel a hledání společných čísel
for i in range(velikost):
    cislo = random.randint(1, 100)  # Náhodné číslo mezi 1 a 100
    for j in cislaUzi:
        if j == cislo and not j in spolecna:
            spolecna.append(cislo)  # Uložení společného čísla
    prumer += cislo  # Přičítání k součtu pro výpočet průměru
    cislaGen.append(cislo)  # Přidání do seznamu generovaných čísel

prumer = prumer / velikost  # Výpočet průměru

# Výpis seznamů
print("Uzivatelsky seznam: ", cislaUzi)
print("Vygenerovaný seznam:", cislaGen)

# Analýza společných čísel
if spolecna != []:
    nejmensi = spolecna[0]
    nejvetsi = 0
    soucet = 0

    for i in spolecna:
        if i < nejmensi:
            nejmensi = i  # Hledání nejmenšího společného čísla
        if i > nejvetsi:
            nejvetsi = i  # Hledání největšího společného čísla
        soucet += i  # Výpočet součtu společných čísel
    
    # Výpis statistik společných čísel
    print("Spolecna cisla: ", spolecna)
    print("Pocet spolecnych cisel: ", len(spolecna))
    print("Nejvetsi spolecne cislo: ", nejvetsi)
    print("Nejmensi spolecne cislo: ", nejmensi)
    print("Soucet spolecnych cisel: ", soucet)
else:
    print("Nejsou zadna spolecna cisla.")

# Výpis finálních statistik
print("Prumer generovaneho seznamu: ", prumer)
print("Pocet cisel vetsich nez 50: ", pocetVetsich)