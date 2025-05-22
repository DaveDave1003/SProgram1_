import random
#zákaz použití vestavěných funkcí


#funkce
def zamichej_slovo(slovo):
    
    nove_slovo = ""
    # oznaceni pismen v seznamu 
    pouzito = [False] * len(slovo)  
    
    while len(nove_slovo) < len(slovo):
        # michani pismen
        index = random.randint(0, len(slovo) - 1)  

        if not pouzito[index]:
            #misto pismena v novem slove
            nove_slovo += slovo[index] 
            # pouzito  
            pouzito[index] = True       
    #vysledek
    return nove_slovo


print(zamichej_slovo("auto"))