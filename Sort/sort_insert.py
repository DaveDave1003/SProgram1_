import random



def insertion_sort(pole):
    
    slozitost = 0


    # začínáme od druhého prvku (index 1),
    # protože první prvek je už "setříděný" (klíč)
    for i in range(1,len(pole)):
        klic = pole[i]
        j = i - 1 #Porovnani s prvkem vlevo
        slozitost += 1

        #Posun všech prvků větších než klíč o 1 doprava
        while j >= 0 and pole[j] > klic:
            slozitost += 1
            pole[j+1] = pole[j]
            j -= 1
        
        pole[j+1] = klic
        
    
    return pole, slozitost






