import math


delka = int(input("Kolik hodnot bude v seznamu: "))

S = []

for i in range(delka):
    i = input("Zadej hodnotu do S: ")
    S.append (i)

print(S)


hledana_hodnota = input("Jaké číslo hledáš: ")

for i in range(len(S)):
    if S[i] == hledana_hodnota:
        print(f"Hledané číslo je v seznamu na pozici {i}")
        
indexy = []        
for i in range(len(S)):
    if S[i] == hledana_hodnota:
        indexy.append(i)

if len(indexy) > 0:
    print(f"hledana hodnota ze seznamu se objevila na indexu {indexy}")
else:
    print("hledana honota nebyla nalezena")