import random




def hledej_cislo(seznam, nejm,nejv,x):
    if nejv >= nejm:
        stred = nejm + (nejv - nejm) //2
        #Hledane cislo je stred
        if seznam[stred] == x:
            return stred
        #Hledane cislo je vetsi nez stred
        elif seznam[stred] < x:
            nejm = stred + 1
        #Hledane cislo je jinak mensi nez stred
        else:
            nejv = stred - 1
    #Cislo v seznamu nebylo
    else:
        return None

seznam = [2, 3, 4, 10, 40]
x = 10

vysledek = hledej_cislo(seznam, 0, len(seznam)-1, 10)


if vysledek != None:
    print("Hledané číslo je v seznamu", vysledek)
else:
    print("Hledané číslo v seznamu není")

        

