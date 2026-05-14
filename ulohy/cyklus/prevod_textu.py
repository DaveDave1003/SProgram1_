def prevod_textu(text, rezim):

    vysledek = ""


    if rezim == "velka":
        for znak in text:
            vysledek += znak.upper()
    
    if rezim == "mala":
        for znak in text:
            vysledek += znak.lower()


    return vysledek








print(prevod_textu('Python', 'velka'))
print(prevod_textu('Python', 'mala'))
print(prevod_textu('HeLLo', 'velka'))