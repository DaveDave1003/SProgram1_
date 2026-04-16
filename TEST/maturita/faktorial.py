import math

#INPUT
Hodnota = int(input("Zadej přirozené číslo: "))
faktorial = 1

#NEPŘIROZENÉ
if Hodnota < 0:
    print("Zadaná hodnota není přirozené číslo")

elif Hodnota == 0:
    print(f"Faktoriál čísla 0 je 1")

#VÝPOČET
else:
    for i in range(1, Hodnota + 1):
        faktorial *= i

    print(f"Faktoriál čísla {Hodnota} je {faktorial}")
