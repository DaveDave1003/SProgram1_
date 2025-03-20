

pocet = int(input("Kolik lidí bude v seznamu: "))

seznam = {}

for i in range(pocet):
    jmeno = input("Zadej jméno: ")
    cislo = int(input("Zadej číslo: "))

    seznam[jmeno] = cislo



for jmeno,cislo in seznam.items():
    print(f"{jmeno} - {cislo}")





vyhledat_jmeno = input("Koho chceš vyhledat: ")
if vyhledat_jmeno in seznam.keys():
    print(f"Telefonní číslo: {seznam[vyhledat_jmeno]}")





