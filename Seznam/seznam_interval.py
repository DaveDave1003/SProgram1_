import math




delka = int(input("Kolik hodnot bude v seznamu: "))
cisla = []

for i in range(delka):
    i = int(input("Zadej hodnotu do S: "))
    cisla.append (i)


dolni_mez = int(input("Dolní mez intervalu: "))
horni_mez = int(input("Horní mez intervalu: "))

pocet = 0

for cislo in cisla:
    if dolni_mez <= cislo <= horni_mez:
        pocet += 1

print(f"V zadaném rozmezí leží {pocet} cisla")
    


print()