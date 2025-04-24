def analyzuj_text(text):

    vysledek = {
        "pocet_znaku": 0,
        "pocet_slov": 0,
        "pocet_vet": 0,
        "prumerna_delka_slova": 0,
        "nejdelsi_slovo": "",
        "nejkratsi:slovo": ""
    }    

    if not text:
        return vysledek

    vysledek["pocet_znaku"] = len(text)

    slova = text.split()

    vysledek["pocet_slov"] = len(slova)

    
    text = text.replace("?",".").replace("!",".")
    vety = text.split(".")
    vety = vety[:-1]

    vysledek["pocet_vet"] = len(vety)

    vysledek["nejdelsi_slovo"] = max(slova, key=len)
    vysledek["nejkratsi_slovo"] = min(slova, key=len)

    delka_slova_celkem = 0

    for slovo in slova:
        delka_slova_celkem += len(slovo)

    vysledek["prumerna_delka_slova"] = delka_slova_celkem / vysledek["pocet_slov"]

    return vysledek