
def pocet_cislic_v1(cislo):

    cislo = abs(cislo)

    if cislo == 0:
        return 1


    pocet = 0

    while cislo > 0:
        cislo = cislo // 10
        pocet += 1

    return pocet


def pocet_cislic_v2(cislo):
    return len(str(abs(cislo)))



#print(pocet_cislic_v1(0))
print(pocet_cislic_v2(41))