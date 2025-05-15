def nejdelsi_slovo_v1(text):
    slova = text.split()
    
    if not slova:
        return ""
    aktualne_nejvetsi_slovo = slova [0]

    for slovo in slova:
        if len(aktualne_nejvetsi_slovo) < len(slovo):
            aktualne_nejvetsi_slovo = slovo
    
    return aktualne_nejvetsi_slovo


def nejdelsi_slovo_v2(text):
    slova = text.split()

    if not slova:
        return ""
    
    return max(slova, key=len)

# nejdelsi_slovo_v1("ahoj jak se máš")
print(nejdelsi_slovo_v2("ahoj jak se máš"))