#nalezeni prvocisel - hodnoty true a false!!
delka = int(input("Zadejte horni mez: "))

cisla = [True] * delka

cisla[0] = False
cisla[1] = False

#nasobky 2
for i in range(2, delka):
    for j in range(i*2, delka, i):
        cisla[j] = False

for i in range(delka):
    if cisla[i]:
        print(i)


#odebírání ze seznamu
cisla_2 = [x for x in range(delka)]


cisla_2.remove(0)
cisla_2.remove(1)

#nasobky 2
for cislo in cisla_2:
    for i in range(2, int(cisla_2[-1]/cislo+1)):
        nasobek = cislo*i
        if nasobek in cisla_2:
            cisla_2.remove(nasobek)

print(cisla_2)        