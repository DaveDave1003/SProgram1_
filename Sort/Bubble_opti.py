import random


def cocktail_sort(pole):
    n = len(pole)
    start = 0
    end = n - 1
    slozitost = 0
    
    
    # cyklus běží, dokud se nezačnou indexy potkávat
    while start < end:
        prohodil_se = False
        
        # průchod zleva doprava – největší prvek doprava
        for i in range(start, end):
            slozitost += 1

            if pole[i] > pole[i + 1]:
                pole[i], pole[i + 1] = pole[i + 1], pole[i]
                prohodil_se = True
        end -= 1 # začátek se posouvá doleva, protože poslední prvek je místě
        
         # pokud se nic neprohodilo, pole je setříděné
        if not prohodil_se:
            break
            
        # průchod zprava doleva – nejmenší prvek doleva
        for i in range(end, start, -1):
            slozitost += 1
            if pole[i] < pole[i - 1]:
                pole[i], pole[i - 1] = pole[i - 1], pole[i]
                prohodil_se = True
        start += 1  # začátek se posouvá doprava, protože první prvek je místě
        
         # pokud se nic neprohodilo, pole je setříděné
        if not prohodil_se:
            break
    
    return pole , slozitost


