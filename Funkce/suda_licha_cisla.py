
def vypis_suda_od_do(zacatek,konec):
    if zacatek > konec:
        return

    if zacatek % 2 != 0:
        zacatek = zacatek + 1

    for cislo in range(zacatek, konec + +, 2):
        print(cislo, end=" ")

print(vypis_suda_od_do)