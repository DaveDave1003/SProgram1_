def citac_slov(slova):
    vysledek = {}


    for slovo in slova:
        if slovo in vysledek:
            vysledek[slovo] += 1

        else:
            vysledek[slovo] = 1


    return vysledek








print(citac_slov(['jablko', 'hruška', 'jablko']))
# → {'jablko': 2, 'hruška': 1}
print(citac_slov(['a', 'b', 'a', 'c', 'b', 'a']))
# → {'a': 3, 'b': 2, 'c': 1}
print(citac_slov([]))
# → {}    