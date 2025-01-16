import math

#Zadejte hodnotu
Mez1 = int(input("Zadej hodnotu meze po kterou se bude generovat: "))

#Kontrola přirozeného čísla
if Mez1 <= 0:
    print("Zadaná hodnota není přirozené číslo")
#rozdělení na sudá a lichá    
else:
    #Od 1 po zadanou hodnotu,aby šla i ta vidět
    for x in range(1, Mez1 + 1):
        #Rozdělení do sudých a lichých
        if x % 2 == 0:
            print (f"Číslo {x} je sudé.")

        else:
            print (f"Číslo {x} je liché.")
