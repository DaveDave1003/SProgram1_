text = input("Zadejte text: ")

pocet = {}
pomoc_pocet = text.split()

print(text)
print(pomoc_pocet)

for slova in pomoc_pocet:
    if slova in pocet.keys():
        pocet[slova] += 1
    
    else:
        pocet[slova] = 1


print("vysledky: ")

for klic, hodnota in pocet.items():
    print(f"{klic} - {hodnota} x krát")
