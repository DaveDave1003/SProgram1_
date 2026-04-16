import random


def unikatni_hodnoty(seznam):
    seznam_unikatnich = []
    for prvek in seznam:

        pocet_stejnych = 0
        for druhy_prvek in seznam:
            if (prvek == druhy_prvek):
                pocet_stejnych += 1

        if (pocet_stejnych == 1):
            seznam_unikatnich.append(prvek)

    return seznam_unikatnich               







X = int(input("Délka seznamu: "))
seznam = []

for i in range(X):
    seznam.append(random.randint(0, int(X / 3)))



print(f"V seznamu {seznam} jsou prvky {unikatni_hodnoty(seznam)} unikátní")

