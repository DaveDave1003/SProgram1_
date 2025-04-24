def je_prvocislo(n):
    """Vrací True, pokud je číslo prvočíslo, jinak False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def je_mocnina_dvou(n):
    """Vrací True, pokud je číslo mocninou dvou, jinak False."""
    # Kontrola, zda je číslo kladné
    if n <= 0:
        return False

    # Opakovaně dělíme číslo dvěma, dokud je to možné bez zbytku
    while n > 1:
        # Pokud je číslo liché (má zbytek po dělení dvěma), není mocninou dvou
        if n % 2 != 0:
            return False
        n = n // 2

    # Pokud se dostaneme až k 1, jedná se o mocninu dvou
    return True


def filtruj_cisla(cisla, kriteria_funkce):

    vysledek = []

    for cislo in cisla:
        if (kriteria_funkce(cislo)):
            vysledek.append(cislo)
    return vysledek


print(filtruj_cisla([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], je_prvocislo))  
# [2, 3, 5, 7]

print(filtruj_cisla([1, 2, 3, 4, 5, 6, 7, 8, 9, 16], je_mocnina_dvou))  
# [1, 2, 4, 8, 16]