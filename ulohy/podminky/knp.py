def kamen_nuzky_papir(hrac1,hrac2):
    
    if hrac1 == hrac2:
        return "remiza"
    
    elif hrac1 == "kamen" and hrac2 == "nuzky":
        return "hrac1"
    
    elif hrac1 == "kamen" and hrac2 == "papir":
        return "hrac2"
    
    elif hrac1 == "papir" and hrac2 == "kamen":
        return "hrac1"
    
    elif hrac1 == "papir" and hrac2 == "nuzky":
        return "hrac2"
    
    elif hrac1 == "nuzky" and hrac2 == "papir":
        return "hrac1"
    
    elif hrac1 == "nuzky" and hrac2 == "kamen":
        return "hrac2"


print(kamen_nuzky_papir('kamen', 'nuzky'))
print(kamen_nuzky_papir('papir', 'kamen'))
print(kamen_nuzky_papir('kamen', 'kamen'))