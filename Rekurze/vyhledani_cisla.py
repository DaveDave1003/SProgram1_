import random




def hledej_cislo(seznam, nejm,nejv,x):
    if nejv >= nejm:
        stred = nejm + (nejv - nejm) //2
        #Hledane cislo je stred
        if seznam[stred] == x:
            return stred
        #Hledane cislo je vetsi nez stred
        elif seznam[stred] < x:
            return hledej_cislo(seznam, stred + 1, nejv, x)
        #Hledane cislo je jinak mensi nez stred
        else:
            return hledej_cislo(seznam, nejm, stred - 1, x)
    #Cislo v seznamu nebylo
    else:
        return None

seznam = [2, 3, 4, 10, 40]


vysledek = hledej_cislo(seznam, 0, len(seznam)-1, 2)


if vysledek != None:
    print("Hledané číslo je v seznamu na indexu", vysledek)
else:
    print("Hledané číslo v seznamu není")

        

