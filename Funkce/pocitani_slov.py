def pocitani_slov(text, min_delka = 3):

    vysledek = {}

    slova = text.lower().split()

    for slovo in slova:

        if slovo[-1] in ",.!?;-:":
            slovo = slovo[:-1]

        if len(slovo) >= min_delka:
            if slovo in vysledek:
                vysledek[slovo] += 1
            else:
                vysledek[slovo] = 1
    
    return vysledek

print(pocitani_slov("Python je skvělý, Python jemocný programovací jazyk"))