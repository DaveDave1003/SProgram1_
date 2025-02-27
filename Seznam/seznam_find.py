import math


pocet = int(input("Kolik hodnot bude v seznamu: "))

S = []

for i in range(pocet):
    i = input("Zadej hodnotu do S: ")
    S.append (i)

n = input("Jaké číslo hledáš: ")

for i in range(len(S)):
    if S[i] == n:
        print("Hledané číslo je v seznamu")
        
        
    else:
        print("Hledané číslo v seznamu není")
    
    






print (S)
print(len(S))