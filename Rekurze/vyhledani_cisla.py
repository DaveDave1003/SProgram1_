import random




def hledej_cislo(seznam, nejm,nejv,x):
    if nejv >= nejm:
        stred = nejm + (nejv - nejm) //2

        if seznam[stred] == x:
            return stred
    
        elif seznam[stred] > x: 
            return hledej_cislo(seznam, nejm, stred-1, x)
    
        else:
            return hledej_cislo(seznam, nejm, stred+1, nejv, x)
    else:
        return -1

seznam = [2, 3, 4, 10, 40]
x = 10

vysledek = hledej_cislo(seznam, 0, len(seznam)-1,x)


if vysledek != -1:
    print("Hledané číslo je v seznamu", vysledek)
else:
    print("Hledané číslo v seznamu není")

        

