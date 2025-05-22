import random
#zákaz použití vestavěných funkcí


#funkce
def zamichej_slovo(slovo):
    
    nove_slovo = ""
    # oznaceni pouzitych pismen
    pouzito = [False] * len(slovo)  
    
    while len(nove_slovo) < len(slovo):
        # michani pismen
        michani = random.randint(0, len(slovo) - 1)  

        if not pouzito[michani]:
            #misto pismena
            nove_slovo += slovo[michani] 
            # pouzito  
            pouzito[michani] = True       
    #vysledek
    return nove_slovo


print(zamichej_slovo("míchání"))