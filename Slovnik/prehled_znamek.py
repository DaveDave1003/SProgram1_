
pocet = int(input("Kolik máme studentů: "))


hodnoceni_studentu = {}


for i in range(pocet):
    jmeno = input("Jméno: ")
    pocet_znamek = int(input("Počet známek: "))
    znamky = []
    
    for j in range(pocet_znamek):
        znamka = int(input("Zadej známku: "))
        znamky.append(znamka)
    

    hodnoceni_studentu[jmeno] = znamky
    
    
   
print("Výsledky: ")



for klic,hodnota in hodnoceni_studentu.items():
    prumer = sum(hodnota) / len(hodnota)
    print(f"{klic} : průměr {prumer}")
