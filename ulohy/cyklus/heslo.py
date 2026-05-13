def je_silne_heslo(heslo):
    if len(heslo) < 8:
        return False
    
    obsahuje_male = False
    obsahuje_velke = False
    obsahuje_cislo = False


    for znak in heslo:
        if znak.islower():
            obsahuje_male=True

        elif znak.isupper():
            obsahuje_velke=True

        elif znak.isdigit():
            obsahuje_cislo=True
    
    return obsahuje_male and obsahuje_velke and obsahuje_cislo


print(je_silne_heslo('Heslo123'))